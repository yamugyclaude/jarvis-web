<!-- 본부지침 -->
> 🚨 규칙: 대화의 맨 첫 응답에만 아래 한 줄을 출력한다. 이미 출력한 뒤에는 반복하지 않는다.
> 📋 본부 지침 읽어옴 | 적용 스킬: ponytail-coding, project-log

---

## 시스템 구조

- **jarvis-web** (현재 레포): 웹 UI + 스킬 정의. 작업 기록은 `PROJECT_LOG.md`에 쌓인다.
- **일지 저장 레포**: `yamugyclaude/javis`, 브랜치 `claude/stoic-goldberg-an2fq8` (운영 브랜치 — 변경 시 `index.html`의 `REF` 값도 함께 수정 필요)
- **일지 파일 경로**: `diary/YYYY/MM/YYYY-MM-DD.md`

## 스킬 사용 기준

| 상황 | 스킬 |
|---|---|
| 출퇴근, 개인 일지, 하루 기록 | `jarvis-log` |
| 코딩 작업 완료, 커밋, 배포 | `project-log` |

## jarvis-log 구현 방법

AI는 `git push` 대신 **GitHub MCP 도구**로 javis 레포에 직접 파일을 쓴다.

```
도구: mcp__github__create_or_update_file
레포: yamugyclaude/javis
브랜치: claude/stoic-goldberg-an2fq8
경로: diary/YYYY/MM/YYYY-MM-DD.md
```

파일이 이미 있으면 `mcp__github__get_file_contents`로 SHA를 먼저 조회한 뒤 업데이트한다.

