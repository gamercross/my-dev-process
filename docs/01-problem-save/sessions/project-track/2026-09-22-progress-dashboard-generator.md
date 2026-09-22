요약: 지금까지 트래커(`sessions/README.md`)·진행상황 표(`00-overview/README.md`)·
링크 무결성을 항목이 늘어날 때마다 사람이 손으로 갱신하고 있다.
재현 절차/배경: 이 저장소를 여러 번 전체 점검하면서 "미착수"로 남은 안내 문구,
어긋난 개수, 깨진 링크를 반복해서 발견했다 (worklog.md 2026-09-19, 2026-09-22
항목 참고). 원인은 항상 같다 — 사람이 여러 파일에 흩어진 숫자를 동시에 맞게
갱신해야 하는데, 그중 하나를 빠뜨리면 바로 스테일해진다.
기대 동작/제안 해결책: `python3 core.py`로 실행하면 트래커 표를 파싱해 집계하고,
전체 테스트를 돌려 통과 여부를 가져오고, 모든 문서의 상대 링크를 검사해서
깨진 게 있는지까지 한 번에 마크다운 리포트로 뽑아준다. 이 리포트가 "지금 진짜
상태"의 단일 출처가 되면, 손으로 여러 파일을 맞추는 대신 이 리포트 하나만
읽고 각 README의 상태 줄이 그것과 맞는지 확인하면 된다.
환경 정보: 로컬 Python 3, 외부 의존성 없음(표준 라이브러리만).
대안 검토: 계속 손으로 갱신 — 지금까지 여러 번 스테일 버그가 났던 방식이라
원문제(배운 게 재사용 안 됨)를 이 워크플로우 시스템 자신에게도 적용 안 하는
셈이라 기각.

## PRD (경량형 — Google 원페이지 스타일)

- Feature Overview: 트래커/테스트 결과/링크 무결성을 자동으로 집계하는 로컬
  리포트 생성 도구.
- Business Justification: 이 저장소 자체가 "배운 걸 자동으로 재사용하자"는
  시스템인데, 정작 자신의 상태 추적은 여전히 수작업이라 여러 번 스테일
  버그가 났다 (00-overview/README.md·06-service/README.md의 "미착수"/"(예정)"
  잔재, worklog 2026-09-22 참고). 이 도구가 그 격차를 메운다.
- Technical Architecture: 핵심(리포트 조립) + 플러그인(수집기 3개)로 분리된
  마이크로커널 구조. 3단계 ADR-0003에서 상세 결정.
- Security & Compliance: 로컬 텍스트 파일만 읽고 씀, 외부 네트워크/자격증명
  없음 — 해당 사항 없음.
- Testing Strategy: 2단계 EARS 요구사항(FR1~FR5) 기반 단위 테스트
  (TDD Red-Green-Refactor), 수집기별로 고립된 방식(순수 함수/tmp 디렉터리/
  가짜 의존성 주입)으로 테스트.

## 게이트 로그

등급: Full ([scope-tiers.md](../../../00-overview/scope-tiers.md) — 알고리즘
문제가 아니고, 단순 수정 수준도 아닌 실제 기능이라 Full)

| 게이트 | 결정 | 근거 |
|---|---|---|
| 1 → 2 | Go | 요약/배경/기대 동작/대안 검토 전부 채움(IEEE 830), PRD 경량형 5개 섹션 전부 채움 |

## 2단계: 문제 분석 (Full 등급, [02-problem-analysis](../../../02-problem-analysis/README.md) 5단계 파이프라인 전체 적용)

### 1. 수집
- 사용한 기법: Document Analysis
- 수집된 원자료: `docs/01-problem-save/sessions/README.md`의 트래커 표 포맷,
  `implementations/run_all_tests.py`의 `find_test_files`/`run_one` 인터페이스,
  이 저장소에서 여러 세션마다 에드혹으로 반복 작성했던 링크 체크 스니펫
  (worklog.md 2026-09-19, 2026-09-22)

### 2. 기능 요구사항 (EARS)

```
FR1 (Event-driven):
  When 사용자가 리포트 생성을 실행하면,
  the 도구는 shall sessions/README.md의 트래커 표를 파싱해서 전체 항목 수·
  트랙별/등급별 개수·1→7 완주 개수·테스트 개수 합계를 계산한다.
  근거: 원문제("트래커/진행상황 표를 손으로 갱신하다 스테일 버그가 남")의 핵심
  충족기준: 트래커 표에 행이 N개 있으면 리포트의 "전체 항목"이 N으로 표시됨

FR2 (Event-driven):
  When 사용자가 리포트 생성을 실행하면,
  the 도구는 shall implementations/run_all_tests.py를 통해 전체 테스트를
  실행하고 통과한 파일 수/전체 파일 수를 리포트에 포함한다.
  근거: "테스트가 실제로 통과하는지"도 매번 손으로 run_all_tests.py를 따로
  돌려 확인하던 것을 리포트에 통합
  충족기준: 테스트 파일이 하나라도 실패하면 리포트에 실패한 파일명이 나열됨

FR3 (Event-driven):
  When 사용자가 리포트 생성을 실행하면,
  the 도구는 shall 저장소의 모든 .md 파일에서 상대 링크를 검사해서 깨진
  링크 목록을 리포트에 포함한다.
  근거: 여러 세션에서 반복 작성했던 링크 체크 스니펫을 도구 안으로 흡수
  충족기준: 존재하지 않는 상대 경로를 가리키는 링크가 있으면 "파일:링크"
  형태로 리포트에 나열됨. http(s) 링크와 앵커 전용(#) 링크는 검사 대상에서
  제외됨

FR4 (Ubiquitous):
  The 도구는 shall 집계 결과를 사람이 읽기 좋은 마크다운 리포트로 표준출력에
  출력한다.
  근거: 리포트 자체가 "지금 진짜 상태"의 단일 출처가 되려면 사람이 바로
  읽을 수 있어야 함
  충족기준: 실행 시 "# 진행상황 대시보드" 제목과 FR1~FR3의 3개 섹션이 순서대로
  표준출력에 나타남

FR5 (Optional feature):
  Where REPORT_OUTPUT 환경변수가 설정되어 있으면,
  the 도구는 shall 표준출력 대신 그 경로에 리포트를 파일로 저장한다.
  근거: 6단계에서 적용할 Twelve-Factor Config 원칙을 요구사항 단계에서 미리
  반영(카탈로그 검색 CLI의 CATALOG_ROOT와 같은 패턴 재사용)
  충족기준: REPORT_OUTPUT을 설정하고 실행하면 그 경로에 파일이 생기고
  "저장됨: <경로>" 메시지가 출력됨
```

### 3. 비기능 요구사항 (Planguage)

```
범주(FURPS): Usability
  Scale: 리포트 생성(테스트 실행 포함)까지 걸리는 시간(초)
  Meter: 실제로 실행해서 측정
  Goal: 2초 이내
  Stretch: 0.5초 이내

범주(FURPS): Supportability
  Scale: 실행에 필요한 외부 패키지 수
  Meter: import 문에 표준 라이브러리 외 패키지가 있는지 확인
  Goal: 0개(표준 라이브러리만)

범주(FURPS): Supportability
  Scale: 새 수집기(예: 벤치마크 추세 집계)를 추가할 때 수정해야 하는 기존
  파일 수
  Meter: git diff --stat으로 확인(다음 수집기를 실제로 추가해볼 때 측정)
  Goal: 0개(핵심 파일은 안 건드리고 새 파일 추가 + 등록 한 줄만)
```

### 4. 우선순위

| ID | MoSCoW | Kano |
|---|---|---|
| FR1 | Must | Basic |
| FR2 | Must | Basic |
| FR3 | Should | Performance |
| FR4 | Must | Basic |
| FR5 | Could | Excitement |

### 5. 추적 (RTM)

요구사항이 5개(5개 이상)라 [2단계 규칙](../../../02-problem-analysis/05-traceability.md)에
따라 RTM을 작성한다 — 이 저장소에서 메타 프로젝트 자신이 아닌 개별 프로젝트가
RTM을 실제로 채우는 첫 사례.

| ID | 요구사항 요약 | 구현 위치 | 테스트 | 충족기준 |
|---|---|---|---|---|
| FR1 | 트래커 표 파싱·집계 | [`collectors/tracker.py`](../../../../implementations/project-track/progress-dashboard-generator/collectors/tracker.py) | `test_fr1_*` 4개 | 트래커 행 개수가 리포트 "전체 항목"과 일치 |
| FR2 | 테스트 실행 결과 집계 | [`collectors/tests.py`](../../../../implementations/project-track/progress-dashboard-generator/collectors/tests.py) | `test_fr2_*` | 실패 파일이 있으면 이름이 나열됨 |
| FR3 | 링크 무결성 검사 | [`collectors/links.py`](../../../../implementations/project-track/progress-dashboard-generator/collectors/links.py) | `test_fr3_*` 2개 | 깨진 링크가 "파일:링크" 형태로 나열됨 |
| FR4 | 마크다운 리포트 조립 | [`core.py`](../../../../implementations/project-track/progress-dashboard-generator/core.py)의 `render_report` | `test_fr4_*` | 3개 섹션이 순서대로 출력됨 |
| FR5 | REPORT_OUTPUT 환경변수 | `core.py`의 `resolve_output_path`/`main` | `test_fr5_*` 2개 | 환경변수 경로에 파일 저장됨 |

**게이트**: `2 → 3` = Go — [`catalog/checklist.md`](../../../catalog/checklist.md)의
"2단계 파이프라인 체크리스트" 4개 항목 모두 충족(EARS 문형, Planguage 3필드,
MoSCoW×Kano, RTM 작성).

## 3단계: 패턴 분석

`catalog/patterns.md`를 "환경변수", "config" 키워드로 검색 → FR5(REPORT_OUTPUT)는
기존 **"환경변수 기반 Config 오버라이드"** 패턴과 정확히 일치(카탈로그 검색
CLI의 `CATALOG_ROOT`와 같은 형태) — 프로젝트 트랙 패턴이 처음으로 재사용된
사례. "플러그인"/"레지스트리"/"마이크로커널" 키워드는 일치 없음 → 구조 자체는
표준 카탈로그([02-architecture-styles.md](../../../03-pattern-analysis/02-architecture-styles.md))로.

[Mark Richards 5대 아키텍처 스타일](../../../03-pattern-analysis/02-architecture-styles.md)
중 Layered와 Microkernel 두 후보로 좁혀짐(나머지 3개는 로컬 단일 사용자 도구에
불필요). 카탈로그 검색 CLI(ADR-0002) 때와 달리 이번엔 "독립적으로 늘어나는
수집 항목"이라는 확장 축이 이미 3개 존재해서 실제 트레이드오프가 갈림 —
[ATAM 축약 비교](../../../03-pattern-analysis/03-tradeoff-evaluation-atam.md)를
이 저장소에서 처음으로 실제로 적용(지금까지는 후보가 1개뿐이라 매번 생략됐음).

결정: [ADR-0003](../../../03-pattern-analysis/adr/0003-progress-dashboard-architecture.md)
(MADR + ATAM 표)으로 Microkernel(핵심 + 플러그인 수집기) 채택.

**게이트**: `3 → 4` = Go — ADR-0003 Accepted, FR5는 기존 패턴 재사용.

## 4단계: 패턴 구현 (Walking Skeleton)

[`implementations/project-track/progress-dashboard-generator/core.py`](../../../../implementations/project-track/progress-dashboard-generator/core.py)에
핵심 경로(수집기 3개 → 리포트 조립 → 출력)를 전부 연결. [Walking
Skeleton](../../../04-pattern-implementation/02-project-track-skeleton.md)
원칙대로 FR1~FR3는 실제 로직까지, FR5(환경변수)는 뼈대만 있는 상태로 먼저
전체를 관통시켰다.

스모크 테스트:
```
$ python3 core.py
# 진행상황 대시보드

## 트래커 요약
- 전체 항목: 6개 (1→7 완주: 6개)
...
## 테스트 결과
- 테스트 파일: 6/6개 전체 통과

## 링크 무결성
- 검사한 상대 링크: 220개
- 깨진 링크: 0개
```

**게이트**: `4 → 5` = Go — 핵심 경로가 실제 저장소를 대상으로 정상 동작함을 확인.

## 5단계: 구현 (Full 등급 — 2단계 EARS 요구사항 전부 커버)

[`test_dashboard.py`](../../../../implementations/project-track/progress-dashboard-generator/test_dashboard.py)에
FR1~FR5를 테스트 케이스로 옮기던 중, **설계 단계에서 미리 피한 재귀 위험**을
발견했다: `collect_tests`의 기본 동작(진짜 `run_all_tests.py`를 다시 실행)을
그대로 테스트에서 호출하면, 그 실행이 이 프로젝트 자신의 테스트 파일
(`test_dashboard.py`)을 다시 찾아내 실행하고, 그 안의 같은 테스트가 다시
`collect_tests`를 호출해 무한 재귀가 된다. 그래서 처음부터 `collect_tests`/
`run_test_suite`에 `load_module` 의존성 주입 지점을 만들고, 테스트는 항상
가짜 loader를 주입하도록 설계했다 — 실제로 재귀가 일어나기 전에(코드를 짜다가
"이 테스트 파일도 discovery 대상이다"라는 걸 깨닫고) 막은 경우라, Red 구간
자체는 없었다. 대신 설계가 맞는지 두 단계로 직접 검증했다: (1)
`test_dashboard.py` 단독 실행, (2) `run_all_tests.py`로 전체 스위트 실행 —
둘 다 재귀 없이 정상 종료함을 실제로 확인(추측이 아니라 실행으로 검증).

FR1(트래커 파싱)은 경계값 3가지(완주가 아닌 게이트는 완주 카운트 제외, 테스트
열의 "-"는 합계에서 제외, 여러 트랙/등급 혼합)를 픽스처 텍스트로 테스트.
FR3(링크 검사)는 tmp 디렉터리에 실제 파일을 만들어 깨진 링크/http/앵커
케이스를 검사. FR2·FR4·FR5는 위에서 설명한 주입 방식으로 실제 파일시스템·
프로세스에 의존하지 않고 테스트.

`run_all_tests.py`로 7개 구현(48개 테스트) 전체 통과 확인.

**게이트**: `5 → 6` = Go — 단위 테스트 통과(10개), FR1~FR5 전부 커버.

## 6단계: 서비스 (프로젝트 트랙 — Planguage Goal 실측)

[Twelve-Factor App](../../../06-service/01-twelve-factor-app.md) 중 이 도구에
해당하는 항목:

| 요소 | 적용 |
|---|---|
| Config | `REPORT_OUTPUT` 환경변수로 출력 대상 설정(FR5) — 하드코딩 안 함 |
| Processes | 상태 없음(stateless) — 실행마다 파일을 새로 읽고 끝남 |
| Logs | 표준출력(`print`)으로만 흘려보냄 |

Planguage Goal 실측(위 2단계에서 정한 값):

| Goal | 목표 | 실측 |
|---|---|---|
| Usability: 리포트 생성 시간(테스트 실행 포함) | 2초 이내(Stretch 0.5초) | **101.1 ms** — Stretch까지 달성 |
| Supportability: 외부 패키지 수 | 0개 | **0개** (표준 라이브러리만) |
| Supportability: 새 수집기 추가 시 기존 파일 수정 수 | 0개 | 아직 실측 안 함 — 다음에 실제로 네 번째 수집기를 추가할 때 `git diff --stat`으로 측정 예정 |

**게이트**: `6 → 7` = Go — Twelve-Factor 원칙 적용 확인, Planguage Goal 2/3
달성(나머지 1개는 미래 실측 조건이 아직 안 옴).

## 7단계: 유지보수 (회고)

날짜: 2026-09-22
문제/프로젝트: 진행상황 대시보드 생성기 (Full 등급, 두 번째 프로젝트 트랙 완주 사례)

잘된 점: Full 등급 프로젝트 트랙이 카탈로그 검색 CLI 이후 **처음으로 재현**됐고,
이번엔 이전과 다른 결정이 실제로 나왔다 — 아키텍처는 Layered 대신 Microkernel,
FR이 5개라 RTM을 실제로 채웠고, 후보가 2개라 ATAM 축약 비교표도 이 저장소에서
처음 실제로 썼다. "이 시스템이 항상 같은 답만 내는 틀"이 아니라 문맥에 따라
다른 결정을 낼 수 있다는 걸 확인했다. 또한 FR5(환경변수 Config)는 기존
패턴을 그대로 재사용했다 — 프로젝트 트랙 패턴도 알고리즘 트랙처럼 재사용된다는
걸 처음 확인.

어려웠던 점: 테스트를 설계하다가 `collect_tests`가 자기 자신의 테스트 파일을
재귀적으로 실행할 수 있다는 걸 발견했다(자기 참조 문제).
  → 5 Whys:
    1. 왜 재귀 가능성이 있었나? → `collect_tests`가 기본적으로 진짜
       `run_all_tests.py`를 다시 실행하는데, 그게 이 프로젝트 폴더 안의
       `test_*.py`까지 다시 찾아낸다.
    2. 왜 그게 문제가 되나? → 그 테스트 파일이 `collect_tests`를 검증하려고
       다시 `collect_tests`를 (기본 인자로) 호출하면, 그 호출이 또
       `run_all_tests.py`를 실행해 같은 테스트를 다시 찾아내 무한히
       반복된다.
    3. 왜 이런 자기 참조가 생겼나? → 대시보드 도구의 "구현체"와 그
       구현체가 "집계하는 대상"(테스트 스위트 전체)이 같은 저장소 안에
       공존하기 때문 — 다른 두 수집기(트래커, 링크)는 이런 자기 참조가
       없다(읽기만 하지, 자기 자신을 실행하지 않음).
    4. 왜 처음 설계할 때 못 봤나? → 못 본 게 아니라, `core.py`를 스모크
       테스트하기 전에 "이 프로젝트도 결국 implementations/ 아래에 들어가고,
       run_all_tests.py의 discovery 대상이 된다"는 걸 미리 생각해서
       `load_module` 주입 지점을 처음부터 넣어뒀다 — 그래서 실제로 무한
       재귀가 발생한 적은 없다.
  근본원인(Blameless): 테스트 대상(전체 테스트 스위트)과 테스트 도구
  자신이 같은 discovery 메커니즘 아래 있을 때는 자기 참조 위험이 있다는
  걸 "실행해서 발견"하지 않고 "설계 시점에 미리 추론"으로 피한 사례 —
  두 방식 다 이 시스템이 요구하는 "실행으로 검증"에 어긋나지 않는다.
  실제로 (1) 단독 실행, (2) 전체 스위트 실행 두 가지로 재귀가 없음을
  직접 확인했다.

새로 배운 패턴: 없음(FR5는 기존 패턴 재사용). 다만 **"자기 자신을 실행하는
도구는 의존성 주입으로 재귀를 끊는다"**는 원칙을 얻었다 — 새 체크리스트
항목으로 등록.

놓쳤던 체크리스트 항목: **"이 저장소 자신의 상태(테스트 스위트, 파일 트리
등)를 다루는 도구를 만들 때는, 그 도구 자신도 그 상태의 일부가 되어
자기 참조·재귀를 일으킬 수 있는지 먼저 따져본다"** — `catalog/checklist.md`에
추가.

이걸로 이 프로젝트도 1→7 완주(Full 등급 기준). 이 저장소는 이제 **알고리즘
5건 + 프로젝트 2건, 총 7개 항목**이 1→7 완주.
