---
name: jarvis-log
description: >
  개인 자비스 기록 비서. 사용자의 자유로운 입력을 구조화된 일지로 저장하고 git push까지 자동 처리.
  다음 중 하나라도 해당되면 즉시 실행:
  - "출근", "퇴근" 언급 시
  - "오늘", "일지", "기록해줘", "적어줘" 언급 시
  - 하루 마무리 대화 시
---

# Jarvis Log — 개인 기록 비서

자유롭게 말하면 구조화된 파일로 저장하고 자동으로 git push한다.

---

## 파일 경로 규칙

```
diary/YYYY/MM/YYYY-MM-DD.md
```

예: `diary/2026/06/2026-06-24.md`

---

## 파일 형식

```markdown
---
date: YYYY-MM-DD
location: office  # home 또는 office
time_in: HH:MM    # 출근 시간 (모를 경우 생략)
time_out: HH:MM   # 퇴근 시간 (모를 경우 생략)
energy: 7         # 오늘 에너지 1-10 (말 안 하면 생략)
mood: 8           # 오늘 기분 1-10 (말 안 하면 생략)
---

## 오늘 한 일
- 

## 잘 된 것

## 아쉬운 것 / 배운 것

## 내일 할 것
```

---

## 저장 방법 — GitHub MCP 직접 쓰기

git push 대신 `mcp__github__create_or_update_file` 도구로 javis 레포에 직접 저장한다.

```
레포:   yamugyclaude/javis
브랜치: claude/stoic-goldberg-an2fq8
경로:   diary/YYYY/MM/YYYY-MM-DD.md
```

**파일 신규 생성 시**: `sha` 파라미터 생략  
**기존 파일 업데이트 시**: `mcp__github__get_file_contents`로 SHA 먼저 조회 후 `sha` 파라미터에 전달

---

## 처리 규칙

### 출근 기록
"출근" 또는 출근 관련 말이 나오면:
1. 오늘 날짜 파일 확인
2. 없으면 위 형식으로 신규 생성 (time_in 기록)
3. mcp__github__create_or_update_file 로 저장, commit message: 출근 기록 YYYY-MM-DD

### 퇴근 기록
"퇴근" 또는 퇴근 관련 말이 나오면:
1. 오늘 날짜 파일 열기 (없으면 생성)
2. time_out 추가 또는 업데이트
3. mcp__github__create_or_update_file 로 저장, commit message: 퇴근 기록 YYYY-MM-DD

### 일지 기록
자유로운 대화 내용을 해당 섹션에 정리해서 추가:
1. 기존 파일 있으면 내용 추가 (덮어쓰기 금지)
2. 없으면 신규 생성
3. mcp__github__create_or_update_file 로 저장, commit message: 일지 YYYY-MM-DD

### 조회 요청
"오늘 어땠어?", "이번 주", "지난번에" 등 조회 요청 시:
- 해당 파일(들) 읽어서 자연스럽게 요약 응답
- 파일이 없으면 "기록 없음" 안내

---

## 자동화 원칙

- 사용자가 따로 "저장해줘"라고 말하지 않아도 기록·push 자동 실행
- push 완료 후 한 줄만 보고: `✅ 기록완료 diary/YYYY/MM/YYYY-MM-DD.md`
- 오류 시 원인 한 줄 + 해결 방법 안내
