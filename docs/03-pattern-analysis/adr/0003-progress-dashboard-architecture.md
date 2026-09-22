# ADR-0003: 진행상황 대시보드 생성기를 마이크로커널(플러그인 수집기) 구조로 구현

- Status: Accepted
- Deciders: 본인
- Date: 2026-09-22

## Context and Problem Statement

[2단계](../../01-problem-save/sessions/project-track/2026-09-22-progress-dashboard-generator.md)에서
확정한 FR1~FR5는 서로 독립적인 세 가지 "수집" 작업(트래커 파싱, 테스트 실행,
링크 검사)과 그걸 하나의 리포트로 합치는 작업으로 나뉜다. 이 세 수집 작업은
지금도 독립적이고, worklog.md 이력을 보면 앞으로도 늘어날 가능성이 높다
(벤치마크 추세, 체크리스트 항목 수 등을 나중에 더 집계하고 싶어질 수 있음).
[02-architecture-styles.md](../02-architecture-styles.md)의 5대 스타일 중 뭘
쓸지 정한다.

## Considered Options

1. **Layered(계층형)** — ADR-0002(카탈로그 검색 CLI)와 같은 방식. 파싱 →
   집계 → 출력 3계층을 함수로 나누되, 새 집계 항목이 생기면 집계 계층
   함수 안에 분기를 직접 추가한다.
2. **Microkernel(마이크로커널)** — 핵심(리포트 조립기 + 수집기 레지스트리)과
   확장 기능(수집기 각각)을 분리한다. 각 수집기는 `repo_root -> {title, lines}`
   형태의 함수 하나이고, `core.py`의 `COLLECTORS` 리스트에 등록만 하면
   된다. 새 수집기를 추가할 때 `core.py`(핵심)는 건드리지 않는다.

Event-Driven/Microservices/Space-Based은 검토 대상에서 제외했다 — 로컬 단일
사용자 도구에 비동기 이벤트나 분산 서비스가 필요할 이유가 없다.

## ATAM 축약 비교 (2단계 Planguage 시나리오 재사용)

| 시나리오 | Layered | Microkernel(채택) | 비고 |
|---|---|---|---|
| Usability: 리포트 생성 2초 이내(Stretch 0.5초) | O | O | 로컬 파일 I/O 수준이라 두 구조 다 성능 차이 없음 |
| Supportability: 외부 패키지 0개 | O | O | 동일 |
| Supportability: 새 수집기 추가 시 기존 파일 0개 수정 | X | O | Layered는 집계 함수 본문을 직접 수정해야 함. Microkernel은 `collectors/`에 파일 하나 추가 + `COLLECTORS` 리스트 한 줄만 추가 |
| 단순성(초기 개발 속도) | O | △ | Layered가 초기 구현은 더 빠름 — 패키지 구조·레지스트리 설계 비용이 없음 |

카탈로그 검색 CLI(ADR-0002)와 다른 점: 그때는 FR이 독립적으로 늘어날 여지가
없어서(검색 로직 하나뿐) Layered가 유일한 실질적 후보였다. 이번엔 "독립적으로
늘어나는 수집 항목"이라는 명확한 확장 축이 이미 3개 존재하고 더 늘어날
근거(worklog 이력)도 있어서, 트레이드오프가 실제로 갈린다.

## Decision Outcome

**옵션 2(Microkernel)를 채택**한다. 초기 구현 비용이 약간 더 들지만
(`collectors/` 패키지 분리, 공통 반환 형식 `{title, lines}` 약속), "새
수집기 추가 시 기존 파일 0개 수정"이라는 Supportability 시나리오를 Layered는
만족 못 하고 Microkernel은 만족한다 — 이게 이번 결정의 민감점(sensitivity
point)이다.

### Consequences

**장점**
- 수집기 하나(`collectors/tracker.py` 등)가 독립적으로 테스트 가능 — 실제로
  5단계에서 각 수집기를 서로 다른 방식(순수 함수, tmp 디렉터리, 가짜 의존성
  주입)으로 고립시켜 테스트할 수 있었다.
- 새 수집기 추가 = 파일 추가 + 등록 한 줄. `core.py`(핵심)의 회귀 리스크가
  없다.

**단점 / 리스크**
- 수집기가 3개뿐인 지금은 공통 인터페이스(`{title, lines}`)를 지키는 비용이
  구조의 이득보다 커 보일 수 있음 — 하지만 카탈로그 검색 CLI 때처럼 "나중에
  안 늘어날 것"이라고 미리 단정하지 않기로 했다(worklog 이력이 근거).
- 수집기 간에 공유 상태가 필요해지면(예: 한 수집기 결과를 다른 수집기가
  참조) 이 구조로는 부자연스러워짐 — 지금은 그런 요구사항이 없어 해당 없음.
