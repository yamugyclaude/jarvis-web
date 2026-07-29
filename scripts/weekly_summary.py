import os
import re
import json
from datetime import datetime, timezone, timedelta

KST = timezone(timedelta(hours=9))

# 수동 재실행 시 기준일 지정 가능 (workflow_dispatch input). 없으면 오늘(KST).
ref_env = os.environ.get("REF_DATE", "").strip()
now_date = datetime.strptime(ref_env, "%Y-%m-%d").date() if ref_env else datetime.now(KST).date()

# 직전(완료된) 주: 지난주 월~일. 매주 월요일 아침에 돌아가므로 now_date가 월요일이면
# this_monday == now_date, start/end는 그 앞주 월~일이 된다.
this_monday = now_date - timedelta(days=now_date.weekday())
start = this_monday - timedelta(days=7)
end = this_monday - timedelta(days=1)
iso_year, iso_week, _ = start.isocalendar()
week_label = f"{iso_year}-W{iso_week:02d}"
days = [start + timedelta(days=i) for i in range(7)]


def diary_path(d):
    return f"diary/{d.year}/{d.month:02d}/{d.strftime('%Y-%m-%d')}.md"


def parse_frontmatter(text):
    fm = {}
    m = re.match(r'^---\n(.*?)\n---', text, re.S)
    if m:
        for line in m.group(1).split('\n'):
            mm = re.match(r'^(\w+):\s*"?([^"]*)"?\s*$', line)
            if mm:
                fm[mm.group(1)] = mm.group(2).strip()
    return fm


def hhmm(s):
    try:
        h, mn = s.split(':')
        return int(h) * 60 + int(mn)
    except Exception:
        return None


SECTION_RE = re.compile(r'^##\s+(.+?)\s*$')
BULLET_RE = re.compile(r'^-\s+(?:(\d{1,2}:\d{2})\s+)?(.+)$')
PLACE_RE = re.compile(r'^>\s*📍\s*\d{1,2}:\d{2}\s*[—–-]\s*(.+?)\s*(도착|떠남|출근|퇴근)')

work_days = 0
total_min = 0
places = {}
meals = []
notes = []
fuel_lines = []

for d in days:
    p = diary_path(d)
    if not os.path.exists(p):
        continue
    with open(p, encoding='utf-8') as f:
        text = f.read()
    fm = parse_frontmatter(text)
    ti, to = fm.get('time_in', '').strip(), fm.get('time_out', '').strip()
    if ti:
        work_days += 1
        if to:
            a, b = hhmm(ti), hhmm(to)
            if a is not None and b is not None:
                diff = b - a
                if diff <= 0:
                    diff += 24 * 60  # 자정 넘긴 퇴근 보정
                total_min += diff

    cur_section = None
    for raw in text.split('\n'):
        s = raw.strip()
        ms = SECTION_RE.match(s)
        if ms:
            cur_section = ms.group(1)
            continue
        mp = PLACE_RE.match(s)
        if mp and mp.group(2) == '도착':
            name = re.sub(r'\s*\(.*\)$', '', mp.group(1)).strip()
            places[name] = places.get(name, 0) + 1
            continue
        mb = BULLET_RE.match(s)
        if mb:
            txt = mb.group(2).strip()
            dstr = d.strftime('%m-%d')
            if cur_section in ('점심 식사', '저녁 식사'):
                meals.append((dstr, cur_section.replace(' 식사', ''), txt))
            elif cur_section in ('메모함', '오늘 한 일', '일상', '잘 된 것', '아쉬운 것 / 배운 것', '내일 할 것'):
                notes.append((dstr, txt))

if os.path.exists('fuel.json'):
    try:
        with open('fuel.json', encoding='utf-8') as f:
            fuel_data = json.load(f)
        s0, e0 = start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d')
        for vname, vdata in fuel_data.get('vehicles', {}).items():
            for r in vdata.get('records', []):
                rd = r.get('date', '')
                if s0 <= rd <= e0:
                    eff = r.get('efficiency')
                    line = f"{rd} {vname} {r.get('liters')}L {r.get('cost')}원"
                    if eff is not None:
                        line += f" → {eff}km/L"
                    fuel_lines.append(line)
    except Exception:
        pass

lines = []
lines.append(f"# 📅 {week_label} 주간 요약")
lines.append("")
lines.append(f"기간: {start.strftime('%Y-%m-%d')} ~ {end.strftime('%Y-%m-%d')}")
lines.append("")
lines.append("## 🏢 근무")
lines.append(f"- 근무일수: {work_days}일")
if total_min:
    lines.append(f"- 총 근무시간: {total_min // 60}시간 {total_min % 60}분")
else:
    lines.append("- 총 근무시간: 기록 없음")
lines.append("")
lines.append("## 📍 방문 장소")
if places:
    for name, cnt in sorted(places.items(), key=lambda x: -x[1]):
        lines.append(f"- {name} {cnt}회")
else:
    lines.append("- 기록 없음")
lines.append("")
lines.append("## 🍚 끼니")
if meals:
    for dstr, kind, txt in meals:
        lines.append(f"- {dstr} {kind}: {txt}")
else:
    lines.append("- 기록 없음")
lines.append("")
lines.append("## 📝 메모 / 한 일")
if notes:
    for dstr, txt in notes:
        lines.append(f"- {dstr} {txt}")
else:
    lines.append("- 기록 없음")
lines.append("")
lines.append("## ⛽ 주유")
if fuel_lines:
    for fl in fuel_lines:
        lines.append(f"- {fl}")
else:
    lines.append("- 기록 없음")
lines.append("")
lines.append("---")
lines.append(f"자동 생성 (집계) · {datetime.now(KST).strftime('%Y-%m-%d %H:%M')} KST")

os.makedirs("weekly", exist_ok=True)
out_path = f"weekly/{week_label}.md"
with open(out_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')

summary = f"🗓 주간요약 생성: {week_label} (근무 {work_days}일, 장소 {len(places)}곳, 끼니 {len(meals)}건)"
print(summary)

github_env = os.environ.get("GITHUB_ENV")
if github_env:
    with open(github_env, "a", encoding="utf-8") as f:
        f.write(f"WEEKLY_SUMMARY={summary}\n")
