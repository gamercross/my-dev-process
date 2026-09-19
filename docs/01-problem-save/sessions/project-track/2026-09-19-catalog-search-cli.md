요약: `docs/catalog/patterns.md`·`checklist.md`를 Claude Code 세션 없이 터미널에서
검색할 방법이 없다.
재현 절차/배경: 지금은 3단계 "패턴 검색"이 SKILL.md 명령 2를 통해 Claude가 직접
grep하는 방식뿐이다. 스크립트, CI, 또는 Claude Code가 아닌 다른 도구에서는 카탈로그를
재사용할 수 없다. (원래 2단계에서 정의한 FR2 "패턴 검색 — 로컬 파일 기준 즉시 결과
표시"가 지금까지 실제 코드로 구현된 적이 없었다.)
기대 동작/제안 해결책: `python3 tools/catalog_search.py <키워드>`로 실행하면
patterns.md·checklist.md에서 키워드가 포함된 항목(카드/체크리스트 줄)을 찾아
사람이 읽기 좋은 형태로 출력한다. 일치하는 게 없으면 표준 카탈로그(3단계 문서)를
안내한다.
환경 정보: 로컬 Python 3, 외부 의존성 없음(표준 라이브러리만).
대안 검토: 그냥 `grep -A 5`를 직접 치는 방법 — 가능은 하지만 카드 구조(제목/트랙/계층)를
모르는 사람이 결과를 해석하기 어렵고, "일치 없으면 표준 카탈로그 안내" 같은 동작을
못 넣는다.

## PRD (경량형 — Google 원페이지 스타일)

- Feature Overview: 카탈로그 검색을 독립 실행 가능한 CLI 스크립트로 제공한다.
- Business Justification: 원문제("배운 게 재사용 안 됨")의 핵심 루프가 지금은 Claude
  Code 세션에 갇혀 있다 — 세션 밖에서도(스크립트, 다른 도구) 재사용 가능해야
  진짜 자산이 된다.
- Technical Architecture: 단일 파일 CLI, 표준 라이브러리만 사용, 계층형(입력 파싱 →
  검색 → 출력 포맷). 3단계 ADR-0002에서 상세 결정.
- Security & Compliance: 로컬 텍스트 파일만 읽음, 외부 네트워크/자격증명 없음 —
  해당 사항 없음.
- Testing Strategy: 2단계 EARS 요구사항 기반 단위 테스트(TDD Red-Green-Refactor),
  카탈로그 파일이 없거나 비어있는 경우 등 엣지 케이스 포함.

## 게이트 로그

등급: Full ([scope-tiers.md](../../../00-overview/scope-tiers.md) — 알고리즘 문제가
아니고, 단순 버그 수정 수준도 아닌 실제 기능이라 Full)

| 게이트 | 결정 | 근거 |
|---|---|---|
| 1 → 2 | Go | 요약/배경/기대 동작/대안 검토 전부 채움(IEEE 830: 문장당 동작 하나), PRD 경량형 5개 섹션 전부 채움(Full 등급 + 프로젝트 트랙이므로 [gates.md 1단계 DoD](../../../00-overview/gates.md)에 따라 결정 필요했음) |

## 2단계: 문제 분석 (Full 등급, [02-problem-analysis](../../../02-problem-analysis/README.md) 5단계 파이프라인 전체 적용)

### 1. 수집
- 사용한 기법: Document Analysis
- 수집된 원자료: `.claude/skills/dev-workflow/SKILL.md` 명령 2 절차, `docs/catalog/patterns.md`·`checklist.md` 카드 포맷, [06-service의 Twelve-Factor Config 원칙](../../../06-service/01-twelve-factor-app.md)

### 2. 기능 요구사항 (EARS)

```
FR1 (Event-driven):
  When 사용자가 키워드와 함께 CLI를 실행하면,
  the CLI는 shall patterns.md와 checklist.md에서 대소문자 구분 없이
  일치하는 블록을 찾아 출력한다.
  근거: 원문제 FR2("패턴 검색")의 첫 실제 구현
  충족기준: 키워드 "해시맵"으로 실행 시 Two Sum 패턴 카드가 출력됨

FR2 (Unwanted behavior):
  If 일치하는 항목이 없으면,
  then the CLI는 shall "일치 항목 없음" 메시지와 3단계 표준 카탈로그 문서
  경로를 출력한다.
  근거: SKILL.md 명령 2 step 3(폴백 규칙)을 코드로 옮김
  충족기준: 존재하지 않는 키워드로 실행 시 안내 메시지 출력, 종료 코드는
  에러가 아닌 0

FR3 (Ubiquitous):
  The CLI는 shall 항상 대소문자 구분 없이 검색한다.
  근거: 사용자가 "Two Sum"/"two sum" 등 다양한 대소문자로 입력할 수 있음
  충족기준: 대문자/소문자 혼합 키워드도 동일한 결과를 냄

FR4 (Optional feature):
  Where CATALOG_ROOT 환경변수가 설정되어 있으면,
  the CLI는 shall 그 경로 아래 catalog/를 사용한다(기본값: 스크립트 기준
  상대경로).
  근거: 6단계에서 적용할 Twelve-Factor Config 원칙을 요구사항 단계에서
  미리 반영
  충족기준: CATALOG_ROOT를 다른 경로로 설정하면 그 경로의 catalog/를 검색함
```

### 3. 비기능 요구사항 (Planguage)

```
범주(FURPS): Usability
  Scale: 검색 결과 출력까지 걸리는 시간(초)
  Meter: time 명령으로 측정
  Goal: 0.5초 이내
  Stretch: 0.1초 이내

범주(FURPS): Supportability
  Scale: 실행에 필요한 외부 패키지 수
  Meter: import 문에 표준 라이브러리 외 패키지가 있는지 확인
  Goal: 0개(표준 라이브러리만)
```

### 4. 우선순위

| ID | MoSCoW | Kano |
|---|---|---|
| FR1 | Must | Basic |
| FR2 | Should | Performance |
| FR3 | Must | Basic |
| FR4 | Could | Excitement |

### 5. 추적 (RTM)

요구사항이 4개(5개 미만)라 [2단계 규칙](../../../02-problem-analysis/05-traceability.md)에
따라 RTM은 생략한다.

**게이트**: `2 → 3` = Go — [`catalog/checklist.md`](../../../catalog/checklist.md)의
"2단계 파이프라인 체크리스트" 4개 항목 모두 충족(EARS 문형, Planguage 3필드,
MoSCoW×Kano, RTM은 5개 미만이라 생략 규칙에 따라 해당 없음).

## 3단계: 패턴 분석

[Mark Richards 5대 아키텍처 스타일](../../../03-pattern-analysis/02-architecture-styles.md)
중 Event-Driven/Microkernel/Microservices/Space-Based은 로컬 단일 사용자 CLI에
불필요해 후보에서 제외 — Layered 단일 파일 스크립트가 유일한 실질적 후보. 후보가
사실상 1개이고 FR1·FR3가 Kano "Basic"이라 ATAM 비교는 생략.

결정: [ADR-0002](../../../03-pattern-analysis/adr/0002-catalog-search-cli-architecture.md)
(MADR 최소 템플릿 — 대안이 2개뿐이라 Nygard 풀버전 대신 사용)로 Layered 단일 파일
스크립트 채택.

**게이트**: `3 → 4` = Go — ADR-0002 Accepted.

## 4단계: 패턴 구현 (Walking Skeleton)

[`implementations/project-track/catalog-search-cli/catalog_search.py`](../../../../implementations/project-track/catalog-search-cli/catalog_search.py)에
핵심 경로(입력 → 검색 → 출력)만 최소로 연결. FR2(폴백 메시지)·FR3(대소문자
무시)·FR4(CATALOG_ROOT)는 아직 안 채움 — [Walking Skeleton](../../../04-pattern-implementation/02-project-track-skeleton.md)
원칙대로 "버릴 코드가 아니라 5단계에서 자라날 골격"만 증명.

스모크 테스트:
```
$ python3 catalog_search.py "해시맵"
[patterns.md] '해시맵' 포함됨
$ python3 catalog_search.py "존재하지않는키워드"
(스켈레톤: 아직 폴백 메시지 없음)
```

**게이트**: `4 → 5` = Go — 핵심 경로 스모크 테스트 통과(주요 컴포넌트 실제로 연결됨).

## 5단계: 구현 (Full 등급 — 2단계 EARS 요구사항 전부 커버)

[`test_catalog_search.py`](../../../../implementations/project-track/catalog-search-cli/test_catalog_search.py)에
FR1~FR4를 그대로 테스트 케이스로 옮겨서 Red-Green-Refactor 진행:

- Red: 테스트를 스켈레톤(4단계)에 대고 실행 → `resolve_catalog_dir` 등이 없어
  `ImportError`로 실패
- Green: FR1~FR4를 전부 구현(대소문자 무시 검색, 폴백 메시지, `CATALOG_ROOT`
  환경변수) → 처음엔 FR3 테스트가 실패했는데, **구현이 아니라 테스트가
  잘못됨**을 발견함(아래 참고)
- Refactor: ADR-0002의 Layered 구조 그대로 `resolve_catalog_dir` / `search` /
  `main` 3계층으로 정리, `implementations/run_all_tests.py`가 `test_solution.py`만
  찾도록 하드코딩돼 있던 걸 `test_*.py`로 일반화(이 프로젝트의 테스트 파일명이
  달라서 발견됨)

**발견한 것 (7단계 회고로 넘길 재료)**: FR3 테스트가 "세 가지 대소문자 입력의
출력 문자열이 완전히 같아야 한다"고 검사했는데, 실제로는 출력 메시지가 사용자
입력 원문을 그대로 보여주는 게 의도된 동작이라 문자열이 다른 게 정상이었다.
"검색이 성공했는가"만 확인하도록 테스트를 고쳤다.

`python3 implementations/run_all_tests.py`로 이 프로젝트 + 기존 두 알고리즘
구현까지 3개 전체(17개 테스트)가 함께 통과하는 것 확인.

**게이트**: `5 → 6` = Go — 단위 테스트 통과(6개), FR1~FR4(EARS Unwanted-behavior
포함) 전부 커버.

## 6단계: 서비스 (프로젝트 트랙 — Planguage Goal 실측)

[Twelve-Factor App](../../../06-service/01-twelve-factor-app.md) 중 이 CLI에
해당하는 항목:

| 요소 | 적용 |
|---|---|
| Config | `CATALOG_ROOT` 환경변수로 카탈로그 위치 설정(FR4) — 하드코딩 안 함 |
| Backing Services | `docs/catalog/`를 "붙였다 뗄 수 있는 자원"으로 취급(경로만 설정으로 바꿈) |
| Processes | 상태 없음(stateless) — 실행마다 파일을 새로 읽고 끝남 |
| Logs | 표준출력(`print`)으로만 흘려보냄, 파일 로그 직접 관리 안 함 |

Planguage Goal 실측(위 2단계에서 정한 값):

| Goal | 목표 | 실측 |
|---|---|---|
| Usability: 검색 소요시간 | 0.5초 이내(Stretch 0.1초) | **34.0 ms** — Stretch까지 달성 |
| Supportability: 외부 패키지 수 | 0개 | **0개** (`os`, `sys`, `pathlib` — 전부 표준 라이브러리) |

두 Goal 모두 달성. 알고리즘 트랙(Two Sum/Contains Duplicate)에서는 Planguage
Goal 자체가 없어 "제출/채점+성능"으로 대체했었는데, 이 프로젝트가 **Planguage
Goal 실측 규칙을 실제로 적용한 첫 사례**다.

**게이트**: `6 → 7` = Go — Twelve-Factor 원칙 적용 확인, Planguage Goal 둘 다 달성(기록됨).
