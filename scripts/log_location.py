import os
import json
from datetime import datetime, timezone, timedelta

# 환경변수
location = os.environ.get("LOCATION", "")
event = os.environ.get("EVENT", "arrive")
custom_time = os.environ.get("TIME", "")
place = os.environ.get("PLACE", "")
lat = os.environ.get("LAT", "")
lng = os.environ.get("LNG", "")
note = os.environ.get("NOTE", "")
section = os.environ.get("SECTION", "memo")
category = os.environ.get("CATEGORY", "")

# ── 자동 분류 (section이 memo일 때만 적용) ──────────────────────
def auto_classify(note, time_str):
    if not note:
        return "memo"
    n = note.lower()
    # 시간 파싱
    hour = -1
    try:
        hour = int(time_str.split(":")[0])
    except:
        pass

    lunch_words = ["점심", "밥", "식사", "먹었", "먹음", "먹어", "국밥", "냉면", "라면", "김밥", "떡볶이", "피자", "짜장", "짬뽕", "초밥", "파스타", "샌드위치", "도시락"]
    dinner_words = ["저녁", "회식", "술", "고기", "삼겹살", "장어", "치킨", "야식"]
    work_words = ["완료", "마침", "완성", "끝냄", "작업", "회의", "미팅", "출장"]

    if any(w in n for w in lunch_words) and 10 <= hour <= 15:
        return "lunch"
    if any(w in n for w in dinner_words) and (hour >= 17 or hour <= 2):
        return "dinner"
    if any(w in n for w in work_words):
        return "work"
    return "memo"
summary = ""

# 섹션 키 -> 일지 헤더 매핑
section_headers = {
    "memo": "## 메모함",
    "work": "## 오늘 한 일",
    "life": "## 일상",
    "lunch": "## 점심 식사",
    "dinner": "## 저녁 식사",
    "good": "## 잘 된 것",
    "learn": "## 아쉬운 것 / 배운 것",
    "tomorrow": "## 내일 할 것",
}

# 한국 위치명 매핑
location_names = {
    "home": "집",
    "office": "사무실",
    "warehouse": "창고"
}

# 현재 날짜/시간 (KST = UTC+9)
KST = timezone(timedelta(hours=9))
now = datetime.now(KST)
today = now.strftime("%Y-%m-%d")
year = now.strftime("%Y")
month = now.strftime("%m")
current_time = custom_time if custom_time else now.strftime("%H:%M")

# 일지 파일 경로
diary_dir = f"diary/{year}/{month}"
diary_path = f"{diary_dir}/{today}.md"
os.makedirs(diary_dir, exist_ok=True)

# 파일 없으면 생성
if not os.path.exists(diary_path):
    content = f"""---
date: {today}
location: {location or place or ""}
time_in: ""
time_out: ""
time_home: ""
energy: ""
mood: ""
---

## 메모함

## 오늘 한 일

## 일상

## 점심 식사

## 저녁 식사

## 잘 된 것

## 아쉬운 것 / 배운 것

## 내일 할 것
"""
    with open(diary_path, "w", encoding="utf-8") as f:
        f.write(content)

# 파일 읽기
with open(diary_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# ── 일과 메모 기록 (NOTE가 있을 때) ──────────────────────
if note:
    if section == "memo":
        section = auto_classify(note, current_time)
    header = section_headers.get(section, section_headers["memo"])
    bullet = f"- {current_time} {note}\n"

    # 헤더 위치 찾기
    header_idx = None
    for i, line in enumerate(lines):
        if line.strip() == header:
            header_idx = i
            break

    if header_idx is None:
        # 헤더 없으면 파일 끝에 새 섹션 추가
        lines.append(f"\n{header}\n\n{bullet}")
    else:
        # 이 섹션의 끝(다음 '## ' 헤더 또는 '> 📍' 로그 또는 EOF) 찾기
        end_idx = len(lines)
        for j in range(header_idx + 1, len(lines)):
            s = lines[j].strip()
            if s.startswith("## ") or s.startswith("> 📍"):
                end_idx = j
                break
        # 섹션 끝쪽 빈 줄들을 건너뛰어 마지막 내용 다음에 삽입
        insert_at = end_idx
        while insert_at - 1 > header_idx and lines[insert_at - 1].strip() == "":
            insert_at -= 1
        lines.insert(insert_at, bullet)

    with open(diary_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    section_label = header.replace("## ", "")
    summary = f"✅ [{section_label}] {note} ({current_time})"
    print(f"✅ 기록 완료: {today} | {section_label}: {note}")

# ── 임시 장소 기록 (PLACE가 있을 때) ──────────────────────
elif place:
    coord_str = f" ({float(lat):.5f}, {float(lng):.5f})" if lat and lng else ""
    log_line = f"\n> 📍 {current_time} — {place} 도착{coord_str}\n"
    lines.append(log_line)

    with open(diary_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    # locations.json 자동 학습
    loc_file = "locations.json"
    if os.path.exists(loc_file):
        with open(loc_file, "r", encoding="utf-8") as f:
            loc_data = json.load(f)
    else:
        loc_data = {"locations": {}, "events": {"arrive": "도착", "depart": "출발"}}

    # 키 생성 (한글 -> 소문자 영문 또는 그대로)
    place_key = place.lower().replace(" ", "_")

    if place_key not in loc_data["locations"]:
        loc_data["locations"][place_key] = {
            "name": place,
            "address": "",
            "lat": round(float(lat), 5) if lat else None,
            "lng": round(float(lng), 5) if lng else None,
            "radius_m": 50
        }
        print(f"✅ 새 위치 등록: {place} ({lat}, {lng})")
    else:
        if lat and lng:
            loc_data["locations"][place_key]["lat"] = round(float(lat), 5)
            loc_data["locations"][place_key]["lng"] = round(float(lng), 5)
        print(f"✅ 위치 갱신: {place}")

    with open(loc_file, "w", encoding="utf-8") as f:
        json.dump(loc_data, f, ensure_ascii=False, indent=2)

    # places.json (장소-카테고리 동기화)
    places_file = "places.json"
    if os.path.exists(places_file):
        with open(places_file, "r", encoding="utf-8") as f:
            places_data = json.load(f)
    else:
        places_data = {"places": {}}
    if "places" not in places_data:
        places_data["places"] = {}

    lat_val = round(float(lat), 6) if lat else None
    lng_val = round(float(lng), 6) if lng else None

    if place not in places_data["places"]:
        places_data["places"][place] = {
            "cat": category or "기타",
            "lat": lat_val,
            "lng": lng_val,
            "created_at": now.strftime("%Y-%m-%d %H:%M")
        }
        print(f"✅ 새 장소 등록: {place} → {category or '기타'} ({lat_val}, {lng_val})")
    else:
        if category:
            places_data["places"][place]["cat"] = category
        if lat_val is not None and lng_val is not None:
            places_data["places"][place]["lat"] = lat_val
            places_data["places"][place]["lng"] = lng_val
        print(f"✅ 장소 갱신: {place}")

    with open(places_file, "w", encoding="utf-8") as f:
        json.dump(places_data, f, ensure_ascii=False, indent=2)

    summary = f"✅ {place} 도착 기록됨 ({current_time})"
    print(f"✅ 기록 완료: {today} | {place} 도착 {current_time}{coord_str}")

# ── 고정 위치 기록 (LOCATION이 있을 때) ──────────────────────
elif location:
    new_lines = []
    fm_count = 0

    for line in lines:
        stripped = line.strip()

        if stripped == "---":
            fm_count += 1
            new_lines.append(line)
            continue

        if fm_count == 1:
            if event == "arrive":
                if line.startswith("location:"):
                    line = f"location: {location}\n"
                elif line.startswith("time_in:") and location != "home":
                    line = f"time_in: {current_time}\n"
                elif line.startswith("time_home:") and location == "home":
                    line = f"time_home: {current_time}\n"
            elif event in ("depart", "commute_out"):
                if line.startswith("time_out:") and location != "home":
                    line = f"time_out: {current_time}\n"

        new_lines.append(line)

    loc_name = location_names.get(location, location)
    event_labels = {"arrive": "도착", "depart": "떠남", "commute_in": "출근", "commute_out": "퇴근"}
    event_label = event_labels.get(event, event)
    if event in ("commute_in", "commute_out"):
        log_line = f"\n> 📍 {current_time} — {event_label}\n"
    else:
        log_line = f"\n> 📍 {current_time} — {loc_name} {event_label}\n"
    new_lines.append(log_line)

    with open(diary_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    if event in ("commute_in", "commute_out"):
        summary = f"✅ {event_label} 기록됨 ({current_time})"
    else:
        summary = f"✅ {loc_name} {event_label} 기록됨 ({current_time})"
    print(f"✅ 기록 완료: {today} | {event_label} {current_time}")

# ── 텔레그램 알림용 요약을 GITHUB_ENV에 기록 ──────────────────
if not summary:
    summary = "⚠️ 기록할 내용이 없습니다 (location/place 누락)"

github_env = os.environ.get("GITHUB_ENV")
if github_env:
    with open(github_env, "a", encoding="utf-8") as f:
        f.write(f"SUMMARY={summary}\n")
