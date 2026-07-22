# Project Log — jarvis-web

작업 완료 시 project-log 스킬이 자동으로 여기에 기록을 추가한다.

---

## 형식

### YYYY-MM-DD — 작업 제목
- 내용
- 결과

---

<!-- 아래부터 기록 -->

## 2026-06-27 성공
### 작업 내용
- 기록 시스템 정비 + 버전 표기 형식 변경 + GitHub Pages 배포

### 결과
- 성공: jarvis-log 스킬 MCP 직접 쓰기 방식으로 명시, CLAUDE.md 운영 맥락 추가, PROJECT_LOG.md 초기 생성, 버전 표기 `v날짜.카운트` 형식 도입 후 main 배포

### 배운 것 / 반복하면 안 되는 실수
- 기획비서 보고 후 사용자 OK 없이 실행비서까지 자동 진행 — 원칙 위반. 기획비서는 계획만, 실행은 사용자 승인 후 실행비서가 따로 담당.

### 성공 루틴 (재사용 가능한 방법)
- 기획비서 → 사용자 OK → 실행비서 → 배포 순서 준수
- 버전: 날짜 바뀌면 카운트 리셋 (예: v2026.06.28.1), 같은 날 수정은 카운트 증가

### 배포 이력
- 버전: v2026.06.26 → v2026.06.27.1
- 배포 일시: 2026-06-27

## 2026-06-30 성공
### 작업 내용
- 일지 조회 데이터 수정/삭제 불가 버그 수정
- 일지 조회 날짜 범위 확대(날짜 선택기) + 과거 날짜 항목 추가 기능

### 결과
- 성공: PUT에 `branch: REF` 누락으로 main에 잘못 쓰여 sha 불일치(409)나던 문제 해결. javis 저장소 직접 확인으로 근본 원인 확정(데이터는 claude/stoic-goldberg-an2fq8 브랜치). 409 재시도 6회 지수백오프 보강. 조회에 오늘/어제/그제+날짜선택기 추가, 조회창에서 그 날짜에 항목 추가(파일 없으면 스크립트와 동일 템플릿으로 새 일지 생성). 백엔드 무수정, index.html만 변경 후 main 배포.

### 배운 것 / 반복하면 안 되는 실수
- 배포(main 반영) 후 PROJECT_LOG 배포 이력 기록을 빠뜨림 — 배포 시 버전·일시를 반드시 함께 남길 것.
- GitHub Pages는 main에서 서비스 → 피처 브랜치 커밋만으로는 실서비스 반영 안 됨. 배포 = main 병합까지.

### 성공 루틴 (재사용 가능한 방법)
- 원인 추정이 2회 빗나가면 추측 멈추고 실제 데이터 저장소를 직접 조회해 확정.
- 배포 직후 footer 버전 갱신 + PROJECT_LOG 배포 이력 동시 기록.

### 배포 이력
- 버전: v2026.06.27.5 → v2026.06.30.1
- 배포 일시: 2026-06-30
- 커밋: 7b7a4dc(branch fix) → 12cdf4e(재시도 보강) → 642861e(날짜선택·과거추가)

## 2026-06-30 추가배포 성공
### 작업 내용
- 과거 항목 추가 카테고리에 '📍 이동' 추가

### 결과
- 성공: 추가 박스 섹션 선택에 이동 추가. 이동은 섹션 밖 `> 📍 HH:MM — 내용` 형식으로 삽입(시각 비우면 00:00). 나머지 섹션은 기존대로 `- 항목`. index.html만 변경 후 main 배포.

### 배포 이력
- 버전: v2026.06.30.1 → v2026.06.30.2
- 배포 일시: 2026-06-30

## 2026-07-07 배포 성공
### 작업 내용
- 위치 기록 카드 삭제, 일지 조회 카드를 최상단으로 이동

### 결과
- 성공: 위치 기록 카드(HTML/CSS/JS) 완전 제거, 일지 조회 카드를 메모 기록·장소 기록보다 위로 재배치. index.html만 변경 후 main 배포.

### 배포 이력
- 버전: v2026.07.02.1 → v2026.07.07.1
- 배포 일시: 2026-07-07

## 2026-07-07 추가배포 성공
### 작업 내용
- 일지조회 결과창을 일지조회 카드 바로 아래로 이동 (기존엔 장소 기록 카드 아래에 있었음)

### 결과
- 성공: diaryView 블록을 일지조회 카드 바로 뒤로 이동, 중복 블록 제거. index.html만 변경 후 main 배포.

### 배포 이력
- 버전: v2026.07.07.1 → v2026.07.07.2
- 배포 일시: 2026-07-07

## 2026-07-07 무드 테마 추가
### 작업 내용
- 애플 스타일 무드 테마 추가 (비서·자비스·조용에 이은 4번째)

### 결과
- 성공: `data-theme="apple"` CSS 변수(-apple-system 폰트, 파란 액센트, 20px 라운드, iOS 스타일 그림자) 추가, 무드바에 '애플' 버튼, 히어로 위젯(#hero-apple) 추가, fillDates/updateStatus에 날짜·상태 연동. index.html만 변경 후 main 배포.

### 배포 이력
- 버전: v2026.07.07.2 → v2026.07.07.3
- 배포 일시: 2026-07-07

## 2026-07-08 장애 조사 + 결과 토스트 상단 고정
### 작업 내용
- 사장님 보고: "오늘 텔레그램도 안 오고 기록도 안 됨" 조사

### 결과
- GitHub Actions(`location-log.yml`) 실행 기록 확인 결과, 2026-07-07T11:43:08Z 이후 workflow_dispatch가 전혀 발생하지 않음(클라이언트에서 요청 자체가 GitHub에 도달 안 함). index.html 문법·배포·`data`브랜치 스크립트(log_location.py)는 모두 정상 확인.
- 일지 조회(읽기)는 정상, 기록(쓰기)만 실패 → **토큰 만료/무효화**로 추정. 사장님이 토큰을 재발급(`repo`+`workflow` 스코프)해서 재입력.
- **해결 확인**: 2026-07-08T09:16:53Z 새 토큰으로 workflow_dispatch 성공 — 일지 기록 → git 커밋/푸시 → 텔레그램 알림 4단계 전부 success. 정상화 완료.
- 부가로 발견한 실제 UX 결함 수정: 결과 메시지(`#result`)가 화면 맨 아래(position:relative)에 있어 오류가 나도 스크롤 안 하면 못 보는 구조였음 → `position:fixed`로 화면 상단 고정 토스트로 변경. 로직(`showResult()`) 변경 없음, CSS만 수정.

### 배운 것 / 반복하면 안 되는 실수
- 결과/오류 메시지는 항상 스크롤 없이 바로 보이는 위치에 둘 것 — 화면 하단 배치는 실패를 조용히 숨기는 결과를 낳음.
- 진단 중간에 "fine-grained 토큰 Actions 권한 부족"으로 추정했었으나 실제로는 토큰 자체 만료/무효화였음(스코프는 `repo`+`workflow`로 정상). 확정 안 된 추정은 사장님 확인 전까지 "추정"으로만 전달할 것 — 이번엔 그렇게 전달해서 문제 없었음.

### 배포 이력
- 버전: v2026.07.07.3 → v2026.07.08.1
- 배포 일시: 2026-07-08

## 2026-07-08 결과 토스트 자동 사라짐 추가
### 작업 내용
- 상단 고정 토스트로 바뀐 `#result` 메시지가 자동으로 사라지지 않아 다음 메시지가 뜨기 전까지 계속 화면에 떠 있던 문제 수정

### 결과
- 성공: `showResult()`에 3.5초 후 자동 숨김 추가. 전역 타이머 변수(`_resultTimer`) 하나로 이전 타이머를 매번 `clearTimeout` 후 재설정해 연속 호출 시 깜빡임 없이 정상 동작. CSS·다른 함수는 변경 없음. `<script>` 추출 후 `node --check`로 문법 검증 통과.

### 배포 이력
- 버전: v2026.07.08.1 → v2026.07.08.2
- 배포 일시: 2026-07-08

## 2026-07-08 재발 — 장소기록·자동정리 422 오류 근본 수정
### 작업 내용
- 사장님 재보고: "메모기록 오류, 장소기록 오류, 텔레그램 안옴, 자동기록 안됨" — 토큰 재발급 이후에도 재발

### 결과
- 사장님이 실제 오류 문구(`오류 422: unexpected inputs provided: category`)를 확인해줘서 원인 확정: 토큰 문제가 아니라 **코드 버그**.
  - `confirmCategory()`(신규 장소 카테고리 기록)가 `category` 입력을 dispatch로 보내는데, `.github/workflows/location-log.yml`의 `workflow_dispatch.inputs`에 `category`가 선언되어 있지 않아 GitHub가 요청 자체를 422로 거부(run이 아예 안 생김).
  - `organizeToday()`("오늘 일지 정리")도 마찬가지로 `organize` 입력이 미선언 상태라 422. 게다가 백엔드(`scripts/log_location.py`)에 organize 처리 로직이 원래 전혀 없었음 — 프론트 확인 문구만 있고 기능 자체가 미구현이었음.
  - 텔레그램 미수신은 위 422로 인해 run 자체가 안 생겨서 스크립트가 안 도는 것의 결과 — 별도 원인 아님.
  - 메모 기록(`note`+`section`)은 원래도 정상 선언된 입력이라 422 사유 없음 — 코드상 문제 없는 것으로 결론.
- 조치:
  - `.github/workflows/location-log.yml` (data 브랜치 — 실제 dispatch가 참조, main 사본도 동기화)에 `category`, `organize` 입력 선언 + env 매핑(`CATEGORY`, `ORGANIZE`) 추가.
  - `scripts/log_location.py`에 `ORGANIZE=true` 처리 로직 신규 구현: 메모함 항목을 기존 `auto_classify()`(키워드+시간대)로 재분류해 대상 섹션으로 이동. 로컬에서 케이스별(이동 있음/없음/기존 메모·장소 기록 회귀) 테스트 완료.
  - 실제 GitHub Actions로 organize 워크플로를 직접 트리거해 검증: 422 없이 큐잉→실행→success, 텔레그램 알림도 정상 발송 확인 (run 28945928569).

### 배운 것 / 반복하면 안 되는 실수
- "토큰 문제"로 보이는 증상(dispatch가 서버에 안 닿음)이 실제로는 **선언 안 된 input 파라미터로 인한 422**일 수 있음 — 다음부턴 프론트가 보내는 dispatch inputs와 워크플로 YAML의 `inputs` 선언을 먼저 대조할 것.
- 프론트에 버튼/UI만 만들고 백엔드 처리 로직을 빠뜨린 채 배포된 기능("오늘 일지 정리")이 있었음 — 새 dispatch 액션 추가 시 워크플로 입력 선언 + env 매핑 + 스크립트 로직 3곳을 항상 세트로 확인할 것.

### 배포 이력
- 커밋: data 브랜치 5f76c63, main 브랜치 3d0b5bd
- 배포 일시: 2026-07-08 (index.html 버전 변경 없음 — 백엔드/워크플로만 수정)

## 2026-07-08 위치 자동기록만 계속 실패 — 아이폰 단축어 토큰 미갱신

### 작업 내용
- 위 422 수정 이후에도 사장님이 "오늘 메타정보(출퇴근 시각)가 기록 안 됨" 재지적. 비서가 처음엔 "어제 삭제한 위치 기록 UI 카드 때문"으로 잘못 진단했으나, 사장님이 정정: 위치 기록은 index.html UI 버튼이 아니라 **아이폰 단축어(Shortcuts)가 GitHub API에 직접 dispatch를 보내는 별도 자동화**임.

### 결과
- 위치 자동기록이 멈춘 시각이 이전 토큰 만료 시각과 정확히 일치. 원인 확정: 사장님이 토큰을 재발급했을 때 **웹앱(브라우저 localStorage) 토큰만 갱신하고 아이폰 단축어 쪽 토큰은 갱신을 놓침** — 그래서 조회·메모·장소 기록은 정상화됐지만 단축어가 호출하는 위치 자동기록만 계속 실패. 사장님이 단축어 토큰을 직접 교체하기로 함.

### 배운 것 / 반복하면 안 되는 실수
- **(운영) 토큰은 최소 2곳에 독립 저장됨** — 웹앱 브라우저 localStorage, 아이폰 단축어(Shortcuts). 토큰 재발급/교체 시 반드시 두 곳 다 갱신할 것. 한쪽만 갱신하면 "일부 기능은 되고 일부만 계속 실패"하는 헷갈리는 증상이 남 — 다음엔 **"특정 기능만 골라서 안 된다" 증상이 보이면 토큰을 쓰는 경로가 여러 곳인지, 그중 일부만 갱신됐는지부터 의심**할 것.
- **(코드/구조) 위치 자동기록은 index.html UI와 무관하게 아이폰 단축어가 GitHub Actions(location-log.yml)를 독립적으로 호출하는 별도 경로**임 — UI 카드를 지우거나 바꿔도 이 경로엔 영향 없음. 앞으로 이 앱 관련 조사를 할 때는 이 전제를 먼저 깔고 시작할 것(비서가 이번에 이걸 몰라서 오진단했음).

## 2026-07-09 출퇴근 현황표 페이지 신규 추가

### 작업 내용
- diary 프런트매터(time_in/time_out)를 월 단위로 모아 보여주는 새 페이지 `attendance.html` 추가, index.html "일지 조회" 카드에 진입 링크 1줄 추가.

### 결과
- 성공: `attendance.html` 신규 생성(월 이동, 요약 통계, 달력 뷰) — index.html과 동일한 4테마 CSS·토큰 배너·GitHub Contents API 읽기 패턴 재사용, 백엔드/워크플로 변경 없음(순수 읽기 전용 프런트엔드 추가).
- 핵심 로직(`parseFrontmatter`, `buildDayInfo`, 요일/일수 계산, 월 이동 연도 경계)을 Node로 격리해 정상/근무중/미출근/음수시간/연도 경계 등 11개 케이스 테스트 전부 통과. `<script>` 문법 검사(`node --check`)도 통과.
- 실제 브라우저·GitHub 토큰을 통한 라이브 fetch 검증은 builder 환경에서 불가 — 비서가 별도로 실제 diary 데이터 대조 검증 예정.

### 배운 것 / 반복하면 안 되는 실수
- 없음(계획대로 순조롭게 진행).

### 배포 이력
- 버전: v2026.07.08.2 → v2026.07.09.1
- 배포 일시: 2026-07-09

## 2026-07-09 출퇴근 현황표 날짜 클릭 → 일지 조회/수정 연결

### 작업 내용
- 사장님 요청: 출퇴근 현황표에서 날짜를 클릭하면 그날의 행적이 나오고 수정도 가능하게.
- index.html의 기존 "일지 조회" 기능(`loadDiary()` — GitHub diary 파일 조회, 항목별 수정/삭제, 신규 항목 추가까지 이미 완성)을 그대로 재사용하기로 설계. attendance.html에 편집 로직을 중복 구현하지 않음.

### 결과
- 성공: `attendance.html`의 `renderDayCell(d, info, isToday)` → `renderDayCell(d, dateStr, info, isToday)`로 시그니처 변경(연/월 조합한 `dateStr`을 `renderCalendar`에서 그대로 전달), 각 날짜 셀에 `onclick="location.href='index.html?date=YYYY-MM-DD'"` 추가 + `.cal-cell{cursor:pointer}` CSS 추가. 빈 채움 칸(`cal-empty`)은 별도 렌더링 경로라 자동으로 클릭 제외됨. 근무일 여부 상관없이 모든 날짜 클릭 가능(데이터 없는 날은 `loadDiary`가 404를 "기록 없음, 추가 가능"으로 정상 처리).
- `index.html` 초기화 스크립트 끝에 `?date=` 쿼리 파라미터를 읽어 있으면 `loadDiary(date)`를 자동 호출하는 3줄 추가. `loadDiary` 내부에서 이미 토큰 체크를 하므로 토큰 없을 때도 배너만 뜨고 안전하게 종료.
- 두 파일 모두 `<script>` 추출 후 `node --check` 통과. 실제 브라우저·GitHub 토큰을 통한 클릭→이동→조회 라이브 검증은 builder 환경에서 불가 — 비서가 별도로 진행.

### 배운 것 / 반복하면 안 되는 실수
- 없음(계획대로 순조롭게 진행, 기존 안정화된 로직 재사용으로 리스크 최소화).

### 배포 이력
- 버전: v2026.07.09.1 → v2026.07.09.2
- 배포 일시: 2026-07-09

## 2026-07-11 차량 관리 / 연비 페이지 신규 추가

### 작업 내용
- 사장님 요청: 주유(리터/금액/키로수) 기록으로 연비를 계산해주는 신규 페이지. 여러 차량 지원, 연비는 "이번 주유량으로 직전 주유 이후 주행거리를 나눔" 방식으로 계산.
- `data` 브랜치 `scripts/log_location.py`에 `elif vehicle and liters and odometer:` 분기 추가 — `fuel.json`에 차량별 기록 append, 직전 기록 odometer와 비교해 `km_driven`/`efficiency` 계산(첫 기록이거나 주행거리가 0 이하면 `null`로 안전 처리).
- `data`+`main` 양쪽 브랜치의 `.github/workflows/location-log.yml`에 `vehicle`/`liters`/`cost`/`odometer` 4개 입력을 `inputs:`와 위치 기록 스텝 `env:`에 전부 선언(과거 두 번 422 장애 원인 재발 방지), `git add`에 `fuel.json` 추가.
- 신규 `vehicle.html`(main): index.html의 dispatch 인프라 + attendance.html의 GitHub Contents API 읽기 패턴을 조합. 차량 선택(+새 차량 추가 토글), 주유 기록 입력, 연비 이력(평균 연비·총 비용·총 횟수 통계 포함) 3개 카드로 구성.
- `index.html`에 "⛽ 차량 관리" 카드 추가(장소 기록 카드 다음), 버전 3곳 갱신.

### 결과
- 성공: `log_location.py` `python3 -m py_compile` 통과. 격리 테스트 3케이스 전부 기대대로 동작 — ①첫 기록: `km_driven`/`efficiency` 둘 다 `null` ②정상 2회차(78000→78480km, 30L): `efficiency=16.0` ③주행거리 역행(78480→78400km): `efficiency=null`, 크래시 없음.
- `location-log.yml`(data/main 양쪽) YAML 문법 검사(`yaml.safe_load`) 통과.
- `vehicle.html`, `index.html` 각각 `<script>` 추출 후 `node --check` 통과.
- 실제 브라우저/토큰을 통한 라이브 fetch, 실제 GitHub Actions dispatch(422 여부) 검증은 builder 환경에서 불가 — 비서가 별도로 진행.

### 배운 것 / 반복하면 안 되는 실수
- `main` 브랜치에도 `location-log.yml` 사본이 존재(실제 dispatch는 `data` 브랜치 워크플로 정의를 참조하지만 main 사본도 존재) — 두 브랜치 모두에 입력 선언을 동기화해야 함을 재확인. main 사본은 이전부터 TG_TOKEN 정제 로직 등 일부 항목이 `data`보다 오래된 상태였는데, 이번 작업 범위(차량 입력 4개 동기화)를 벗어나므로 임의로 손대지 않음.

### 배포 이력
- 버전: v2026.07.09.2 → v2026.07.11.1
- 배포 일시: 2026-07-11

## 2026-07-12 출퇴근 근무시간 계산 자정 넘김 보정

### 작업 내용
- 백엔드(`data` 브랜치 `log_location.py`)가 자정 넘긴(새벽 2시 이전) 퇴근/출근을 전날 diary 파일에 기록하도록 바뀌면서, 같은 날짜 파일에 `time_in`(예: 08:00)과 `time_out`(예: 00:13, 다음날 새벽)이 함께 저장되는 경우가 생김. `attendance.html`의 `buildDayInfo(fm)`가 두 시각을 단순히 그날 분(分) 단위로 빼기만 해서 음수가 나오고 근무시간이 "-"(계산불가)로 잘못 표시되던 버그 수정.

### 결과
- 성공: `buildDayInfo(fm)`에서 `mins`가 0 이하이면 24*60(1440)을 더해 자정 넘김을 보정하도록 3줄 수정. 테스트 3케이스 확인 — ①정상 당일(09:00~18:00): 9.0시간 ②자정 넘김(08:00~00:13): 16.2166...시간(보정 전엔 음수→null) ③입퇴근 동일(09:00~09:00, 예외적 극단값): 24.0시간, 크래시 없음. `<script>` 블록 `node --check` 통과.
- `index.html` 공용 버전 3곳(title/brand/footer) 갱신.

### 배운 것 / 반복하면 안 되는 실수
- 백엔드 시간 기록 방식(자정 넘김 → 전날 파일 귀속)이 바뀌면 프론트 계산 로직도 같이 검토해야 함. 이번엔 프론트만 대응 지연되어 근무시간 오표시 발생.
- `mins<=0` 보정은 "자정 넘김"과 "입력 오타로 인한 시간 역전"을 구분 못 함 — 예를 들어 `time_in=14:00, time_out=09:00`(오타로 순서가 뒤바뀐 데이터)도 자정 넘김으로 오인해 19시간으로 계산됨(전엔 "-"로 걸러졌음). 개인용 도구라 감수하기로 함 — 나중에 비정상적으로 큰 근무시간이 보이면 오타 가능성부터 의심할 것.

### 배포 이력
- 버전: v2026.07.11.1 → v2026.07.12.1
- 배포 일시: 2026-07-12

## 2026-07-13 일지 메타정보 필드 지우기 기능 추가

### 작업 내용
- 사장님 요청: 일지 조회 메타정보(출근/퇴근/귀가/장소/에너지/기분) 수정창에 "지우기" 버튼 추가. 예를 들어 사무실에 가긴 했지만 출근한 게 아닌 날 잘못 찍힌 `time_in`처럼, 다른 값으로 바꾸는 게 아니라 아예 빈 값으로 없애고 싶은 경우 지원. 기존 `saveMetaField()`는 입력값이 비어 있으면 저장을 막아서 이 용도로 못 씀.
- `startMetaEdit()`의 버튼 줄에 "저장"과 "취소" 사이 "지우기" 버튼 추가(`--err-text` 색상으로 시각 구분, 새 CSS 변수는 만들지 않음).
- `saveMetaField()` 바로 아래에 신규 함수 `clearMetaField(field)` 추가 — 로직은 `saveMetaField`와 동일하되 입력값을 읽지 않고 무조건 `""`로 저장.

### 결과
- 성공: `<script>` 블록 `node --check` 통과. `clearMetaField`가 쓰는 정규식 치환 로직을 Node로 직접 테스트 — ①필드가 이미 있는 경우(`time_in: 09:30` → `time_in: ""`) ②필드가 frontmatter에 아예 없는 경우(닫는 `---` 앞에 `field: ""` 삽입) 둘 다 기대대로 동작.
- `index.html` 버전 3곳(title/brand/footer) 갱신. 기존 `saveMetaField`, `commitDiaryChange`, `renderDiaryMetaReadonly` 등은 손대지 않음.

### 배운 것 / 반복하면 안 되는 실수
- 없음(기존 `commitDiaryChange`의 sha 충돌 재시도 로직을 그대로 재사용해 리스크 최소화).

### 배포 이력
- 버전: v2026.07.12.1 → v2026.07.13.1
- 배포 일시: 2026-07-13

## 2026-07-14 장소 기록 지도(Leaflet + OpenStreetMap) 팝업 추가

### 작업 내용
- 사장님 요청: 저장된 장소들(`places.json`, 위/경도 포함)을 지도에 마커로 확인하고 싶다는 요구. API 키가 필요 없는 OpenStreetMap 타일 + Leaflet.js(CDN)로 구현. 별도 페이지가 아니라 `index.html` 위에 기존 `.overlay`/`.popup` 패턴을 재사용한 모달 팝업으로 처리.
- `<head>`에 Leaflet CSS, `</body>` 안 앱 스크립트 직전에 Leaflet JS CDN 추가.
- "장소 기록" 카드에 "🗺 지도로 보기" 버튼(`.view-btn`) 추가, `openMapPopup()` 연결.
- `#catOverlay`와 같은 구조로 `#mapOverlay`/`#placeMap` 오버레이 신설, 바깥 클릭 시 닫히는 이벤트도 기존 패턴 그대로 적용.
- `openMapPopup()`/`closeMapPopup()`/`renderPlaceMarkers()` 신규 함수 추가. 이미 메모리에 있는 전역 `_placeDB`(페이지 로드 시 `loadPlacesFromGitHub()`가 채워둠)를 그대로 사용 — 별도 fetch 없음. 위/경도가 없는 장소는 마커에서 자동 제외(크래시 없이 스킵).

### 결과
- 성공: 앱 `<script>` 블록 `node --check` 통과. `mapOverlay`/`placeMap` id 중복 없음, 기존 `noteOverlay`/`catOverlay`와 동일한 오버레이 구조 확인.
- `index.html` 버전 3곳(title/brand/footer) 갱신.

### 배운 것 / 반복하면 안 되는 실수
- 없음. Leaflet 컨테이너는 `display:none`이 아닌 상태에서 초기화해야 크기 계산이 정상 동작하므로, 오버레이가 `.show`로 표시된 직후 `setTimeout(...,50)`으로 지연 초기화하도록 했음(그대로 유지 필요).

### 배포 이력
- 버전: v2026.07.13.1 → v2026.07.14.1
- 배포 일시: 2026-07-14

## 2026-07-14 지도 팝업에 장소 리스트 + 바로가기/기록 버튼 추가

### 작업 내용
- 사장님 요청: 지도 팝업 안에 저장된 장소 이름 리스트를 두고, 이름 클릭 시 지도가 해당 위치로 이동(마커 팝업 오픈), "기록" 버튼 클릭 시 그 장소 방문을 오늘 일지에 바로 기록.
- `#placeMap` 높이를 `60vh` → `42vh`로 줄이고 그 아래 스크롤 가능한 `#placeList` 컨테이너 신설.
- `renderPlaceMarkers()`가 마커 생성 시 전역 `_placeMarkers[name]`에 저장하도록 수정(재실행 시 `_placeMarkers = {}`로 초기화 후 다시 채움), 함수 끝에서 `renderPlaceList()` 호출.
- `renderPlaceList()` 신규: `_placeDB`를 순회해 각 장소를 DOM 요소로 직접 생성(이름 텍스트는 `textContent`, 클릭 핸들러는 클로저로 연결) — onclick 문자열에 이름을 넣지 않아 이름에 따옴표가 들어가도 안전. 좌표 없는 장소는 흐리게 표시하고 이름 클릭 시 이동 스킵(단, "기록" 버튼은 좌표 유무와 무관하게 항상 동작).
- `flyToPlace(name)` 신규: `_leafletMap.flyTo`로 해당 좌표 이동 + `_placeMarkers[name].openPopup()`.
- `recordPlaceVisit(name)` 신규: 기존 `sendPlace()`와 동일한 `{place, lat, lng}` 형태로 `dispatch()` 호출(이미 워크플로에 선언된 입력이라 422 위험 없음).

### 결과
- 성공: 앱 `<script>` 블록 `node --check` 통과. `placeList` id 중복 없음, `renderPlaceMarkers`/`renderPlaceList`/`flyToPlace`/`recordPlaceVisit` 함수 정의 각 1회. `_placeMarkers` 재실행 시 초기화 확인.
- `index.html` 버전 3곳(title/brand/footer) 갱신.

### 배운 것 / 반복하면 안 되는 실수
- 없음. 사용자 데이터(장소 이름)를 HTML 문자열에 끼워 넣는 대신 `textContent` + 클로저 이벤트 핸들러로 처리해 이스케이프 문제를 원천 차단.

### 배포 이력
- 버전: v2026.07.14.1 → v2026.07.14.2
- 배포 일시: 2026-07-14

## 2026-07-14 지도 모달 안에서 기록 시 토스트 가림 수정
### 작업 내용
- 위 "지도 팝업 장소 리스트" 기능 검토 중 비서가 발견: 지도 팝업(`#mapOverlay`, `.overlay` z-index:100) 안에서 "기록" 버튼을 누르면 뜨는 결과 토스트(`#result`, 기존 z-index:100)가 모달 뒤에 가려 안 보임. 두 요소가 같은 z-index인데 오버레이가 DOM에서 뒤에 있어(275행+ vs 269행) 오버레이가 위로 쌓임.

### 결과
- 성공: `#result` z-index를 100 → 200으로 올려 모달 위로 토스트가 뜨도록 수정(CSS 한 줄). 이전엔 모달을 띄운 상태에서 기록하는 UX 자체가 없어 문제 안 됐으나, 이번 지도 리스트 기록 기능으로 처음 드러난 케이스. `<script>` 블록 `node --check` 통과.

### 배운 것 / 반복하면 안 되는 실수
- 새로 "모달/오버레이 안에서 결과 토스트를 띄우는 동작"을 추가할 때는 토스트의 z-index가 오버레이보다 위인지 확인할 것.

### 배포 이력
- 버전: v2026.07.14.2 → v2026.07.14.3
- 배포 일시: 2026-07-14

## 2026-07-14 지도 탭으로 새 장소 등록 기능 추가

### 작업 내용
- 사장님 요청: 지도에서 원하는 지점을 탭해 그 좌표로 새 장소(이름+카테고리)를 바로 등록.
- 기존 "장소 기록" 카드의 카테고리 팝업(`#catOverlay`) 흐름을 그대로 재사용: `confirmCategory()`가 GPS 대신 미리 지정된 좌표(`_pendingCoord`)가 있으면 그걸 쓰고, 없으면 기존과 동일하게 `getGPS()`를 쓰도록 최소 수정 — 정상 장소 기록 흐름은 100% 그대로 유지(회귀 없음).
- 지도 팝업에 "📍 지도 찍어 새 장소 추가" 버튼과 이름 입력 바(`#mapPickBar`) 추가. 버튼 클릭 시 `startMapPick()`으로 픽 모드 진입 → 지도 탭 시 `onMapClick()`이 좌표를 `_pendingCoord`에 저장하고 임시 마커 표시 → 이름 입력 후 "다음"(`confirmMapPick()`)으로 기존 카테고리 팝업을 염(이후 흐름은 `confirmCategory()`가 처리).
- `_leafletMap.on('click', onMapClick)`은 `openMapPopup()`의 `if (!_leafletMap)` 최초 초기화 블록 안에 등록해 지도를 여러 번 열어도 핸들러 중복 등록 안 됨. `onMapClick`은 픽 모드가 아니면 즉시 리턴해 평소 지도 클릭(마커 팝업 등)에 영향 없음.
- `closeCatPopup()`에도 `_pendingCoord = null` 리셋 추가(취소 시 다음 일반 기록에 엉뚱한 좌표가 남는 것 방지).

### 결과
- 성공: 앱 `<script>` 블록 `node --check` 통과. 신규 id(`mapPickBtn`/`mapPickBar`/`mapPickNameInput`), 신규 함수(`startMapPick`/`onMapClick`/`confirmMapPick`/`cancelMapPick`) 각 1회 정의 확인. `confirmCategory()`의 `_pendingCoord` null 분기가 기존 GPS 흐름과 동일함을 코드로 확인. 지도 클릭 핸들러가 `if (!_leafletMap)` 블록 안에 있어 중복 등록 안 됨을 확인.
- `index.html` 버전 3곳(title/brand/footer) 갱신.
- 실제 브라우저에서의 지도 탭·마커·dispatch 동작은 이 환경에서 직접 확인 불가 — 문법 검사와 코드 리뷰로 대체.

### 배운 것 / 반복하면 안 되는 실수
- 없음. 기존 카테고리 팝업 흐름을 재사용해 새 UI 경로를 추가하되, 공용 함수(`confirmCategory`)의 기존 동작(좌표 없을 때 GPS 사용)을 깨지 않도록 "미리 지정된 값이 있으면 우선, 없으면 기존 로직" 패턴으로 안전하게 확장.

### 배포 이력
- 버전: v2026.07.14.3 → v2026.07.14.4
- 배포 일시: 2026-07-14

## 2026-07-14 지도 찍기 중단 시 좌표 누수 수정
### 작업 내용
- 위 "지도 탭 새 장소 등록" 기능 검토 중 비서가 엣지 케이스 버그 발견: 지도에서 위치를 찍어 `_pendingCoord`가 설정된 상태에서 "다음/취소"를 안 누르고 ✕나 바깥 클릭으로 지도 팝업을 닫으면, `_pendingCoord`가 남아 다음 일반 장소 기록(GPS로 잡아야 하는)에 엉뚱한 지도-탭 좌표가 조용히 붙는 문제.

### 결과
- 성공: `closeMapPopup()`(✕·바깥클릭 경로)이 픽 상태를 완전히 리셋(`_mapPickMode`/`_pendingCoord`/임시마커/바·버튼 표시)하도록 `resetMapPick()` 헬퍼 추가. 정상 진행 경로인 `confirmMapPick()`은 `closeMapPopup()`을 부르지 않고 지도 오버레이만 직접 숨겨 `_pendingCoord`를 살린 채 카테고리 팝업으로 넘어가도록 분리. `cancelMapPick()`도 `resetMapPick()` 재사용으로 정리. `<script>` `node --check` 통과.

### 배운 것 / 반복하면 안 되는 실수
- 모달을 여러 경로(확정/취소/✕/바깥클릭)로 닫을 수 있을 때, 각 경로가 임시 상태(여기선 `_pendingCoord`)를 올바르게 정리하는지 전부 따져볼 것 — "확정"만 생각하고 "그냥 닫기"를 빠뜨리면 상태가 다음 동작에 새어 들어감.

### 배포 이력
- 버전: v2026.07.14.4 → v2026.07.14.5
- 배포 일시: 2026-07-14

## 2026-07-14 지도 엔진을 카카오맵으로 교체 + 장소 검색 기능 추가

### 작업 내용
- 사장님 요청: 지도 팝업 엔진을 Leaflet+OpenStreetMap에서 카카오맵으로 교체(한국 지명·상호 검색이 목적). 좌표 저장 포맷(`_placeDB`의 `{lat,lng}`)과 `_pendingCoord`→`confirmCategory()` 연동 흐름은 지도 엔진과 무관하므로 그대로 두고, Leaflet API 호출만 카카오 API로 1:1 치환.
- `<head>` Leaflet CSS 제거, `</body>` 앞 Leaflet JS를 카카오 지도 SDK(`libraries=services`, `autoload=false`)로 교체. `_leafletMap` → `_kakaoMap`, `L.marker`/`L.tileLayer`/`fitBounds` → `kakao.maps.Marker`/`kakao.maps.Map`/`LatLngBounds`, `bindPopup` → `kakao.maps.InfoWindow`(`openPlaceInfo` 헬퍼로 재사용, 장소명은 `textContent`로 넣어 XSS 안전).
- `openMapPopup()`에 SDK 미로드 가드 추가 — `kakao` 전역이 없으면(키 미설정 상태) 토스트 안내만 뜨고 앱이 깨지지 않음.
- 신규: 지도 팝업에 장소·주소 검색창(`#mapSearchInput`) 추가. `searchPlaces()`가 `kakao.maps.services.Places().keywordSearch()`로 검색 → `renderSearchResults()`가 결과 리스트 렌더 → 결과 클릭 시 `pickSearchResult(name, lat, lng)`가 지도 이동+임시마커+`_pendingCoord` 설정+이름 자동 입력까지 하고 기존 `#mapPickBar`→"다음"→`confirmMapPick()`→카테고리 팝업 흐름에 그대로 얹음(신규 등록 경로 재사용, 별도 dispatch 로직 없음).
- `resetMapPick()`에 검색 결과 리스트 초기화(비우기+숨김) 한 줄 추가 — 픽 취소/모달 닫기 시 이전 검색 결과가 남아 혼란 주지 않도록.
- **선행 조건(사장님 액션 필요)**: 카카오 개발자(developers.kakao.com)에서 앱 생성 → JavaScript 키 발급 → 플랫폼에 `https://yamugyclaude.github.io` 도메인 등록 → 카카오맵 사용 ON. 이 3가지가 끝나야 지도가 실제로 뜬다. **현재 `index.html`의 appkey는 `YOUR_KAKAO_JS_KEY` 플레이스홀더 상태 — 키를 실제 값으로 교체하기 전까지는 지도 팝업만 비활성(안내 토스트만 뜸)이고 나머지 앱 기능(일지/장소기록/차량/출퇴근표)은 정상 작동.**

### 결과
- 성공: 앱 `<script>` 블록 `node --check` 통과. `grep -i "leaflet\|L\.map\|L\.marker\|L\.tileLayer\|_leafletMap\|instanceof L\." index.html` 0건으로 Leaflet 잔재 완전 제거 확인. 신규 함수(`searchPlaces`/`renderSearchResults`/`pickSearchResult`/`openPlaceInfo`) 각 1회 정의, 신규 id(`mapSearchInput`/`mapSearchResults`) 중복 없음 확인. 좌표 순서 코드 리뷰: `kakao.maps.LatLng(위도, 경도)` 순 일관, 검색 결과 `y`=위도(lat)/`x`=경도(lng) parseFloat 처리 정확. 기존 `confirmCategory`/`_pendingCoord`/`closeCatPopup` 흐름은 손대지 않음(지도 엔진 교체와 무관).
- `index.html` 버전 3곳(title/brand/footer) 갱신.
- 실제 지도 렌더링/검색 동작은 카카오 키 발급·도메인 등록 후에만 확인 가능하므로 이 환경에서는 문법 검사+Leaflet 잔재 제거 확인+좌표 순서 코드 리뷰로 검증 대체.

### 배운 것 / 반복하면 안 되는 실수
- 외부 지도 SDK를 `autoload=false`로 붙일 때는 `kakao.maps.load(cb)` 콜백 안에서 초기화해야 하고, 키가 아직 플레이스홀더인 배포 단계에서도 앱이 깨지지 않도록 `typeof kakao === 'undefined'` 가드를 반드시 넣을 것.

### 배포 이력
- 버전: v2026.07.14.5 → v2026.07.14.6
- 배포 일시: 2026-07-14

## 2026-07-22 카카오맵 승인 게이트로 중단 — Leaflet+OSM 원복 + Nominatim 검색 도입

### 작업 내용
- 카카오맵 키 발급·`https://yamugyclaude.github.io` 도메인 등록·[카카오맵] 사용설정 ON·SDK 스크립트 태그까지 전부 정상 확인했으나, 실제 페이지(referer=github.io)에서 SDK를 부르면 **서버 단에서 거부**됨. SDK URL 직접 접근은 정상 응답하는데 페이지 컨텍스트로만 막히는 것으로 보아 원인은 카카오 계정/앱의 **카카오맵 호출 권한 승인 게이트**(신규 앱·계정 내 2번째 이상 앱은 별도 심사 필요, 며칠 소요)로 판단 — 코드로 해결 불가.
- 목적(장소 검색)을 살리기 위해 지도 엔진을 직전 정상 커밋 `8576c94` 기준 **Leaflet + OpenStreetMap**으로 원복. `<head>` Leaflet CSS 복원, 카카오 SDK `<script>` 자리를 Leaflet JS로 교체. `_kakaoMap`→`_leafletMap`, `_placeInfoWindow`/`openPlaceInfo` 삭제 후 `bindPopup`/`openPopup`으로 대체. `openMapPopup`/`renderPlaceMarkers`/`flyToPlace`/`onMapClick`/`resetMapPick`/`confirmMapPick`을 Leaflet API로 원복.
- 검색은 키·카드·승인이 전혀 필요 없는 **OSM Nominatim**으로 교체. `searchPlaces()`가 `nominatim.openstreetmap.org/search`(countrycodes=kr, accept-language=ko)를 호출하고, `renderSearchResults()`가 `{display_name, lat, lon}` 배열을 `textContent`로 안전하게 렌더(이름=`display_name` 첫 조각, 부제=전체), 클릭 시 `pickSearchResult(name, lat, lng)`가 지도 이동+임시마커+`_pendingCoord` 설정+이름 자동 입력 후 기존 `#mapPickBar`→"다음"→`confirmMapPick()`→카테고리 팝업 흐름에 그대로 얹음. 검색 UI(`#mapSearchInput`/`#mapSearchResults`)와 `_pendingCoord`→카테고리 등록 흐름은 손대지 않음.
- `<meta name="referrer" content="no-referrer-when-downgrade">`는 유지(Nominatim 요청 식별에 도움).

### 결과
- 성공: 앱 `<script>` 블록 `node --check` 통과. `grep -iE "kakao|dapi\.kakao|_kakaoMap|kakao\.maps|openPlaceInfo" index.html` 0건으로 카카오 잔재 완전 제거 확인. `L.map`/`L.marker`/`L.tileLayer`/`_leafletMap` 참조 복원 확인. 좌표 순서 리뷰: Leaflet은 `[lat,lng]` 배열 일관, Nominatim은 `lat`=위도/`lon`=경도로 `parseFloat` 처리 정확(카카오의 `x`=경도/`y`=위도와 반대이므로 뒤바뀌지 않게 재확인). 신규/변경 함수(`searchPlaces`/`renderSearchResults`/`pickSearchResult`) 각 1회 정의.
- `index.html` 버전 3곳(title/brand/footer) 갱신.
- Nominatim 한계(정직히 기록): 주소·행정구역·큰 시설은 잘 찾으나, OSM 데이터에 등록 안 된 작은 식당·상호는 검색 결과에 안 나올 수 있음.
- 실제 지도 렌더링/검색 라이브 동작은 이 환경에서 확인 불가(코드 검증만 가능) — 배포 후 사장님 직접 확인 필요.

### 배운 것 / 반복하면 안 되는 실수
- 키·도메인·설정이 코드상 전부 정상이어도, 외부 지도 SDK는 계정/앱 단위의 **서버 측 승인 절차**가 별도로 걸릴 수 있다는 것을 미리 감안할 것. 승인 지연이 확인되면 코드로 붙잡고 있지 말고 즉시 대안(키 불필요한 오픈 서비스)으로 전환 판단할 것.

### 배포 이력
- 버전: v2026.07.15.2 → v2026.07.15.3
- 배포 일시: 2026-07-22
