# ADR-0002: 카탈로그 검색 CLI를 단일 파일 계층형 스크립트로 구현

- Status: Accepted
- Deciders: 본인
- Date: 2026-09-19

## Context and Problem Statement

[2단계](../../01-problem-save/sessions/project-track/2026-09-19-catalog-search-cli.md)에서
확정한 FR1~FR4를 만족하려면, `docs/catalog/`의 두 파일을 읽어 키워드로 검색하고
사람이 읽기 좋게 출력하는 도구가 필요하다. [02-architecture-styles.md](../02-architecture-styles.md)의
5대 스타일 중 뭘 쓸지 정한다.

## Considered Options

1. **Layered(계층형) 단일 파일 스크립트** — 입력 파싱 → 검색 → 출력 포맷 3계층을
   함수로만 나눈 순수 Python 스크립트
2. **현행 유지 (LLM 전용 명령)** — 코드를 안 만들고 SKILL.md 명령 2가 Claude에게
   grep을 시키는 지금 방식을 그대로 둔다

Event-Driven/Microkernel/Microservices/Space-Based 스타일은 검토 대상에서
제외했다 — 단일 사용자가 로컬에서 파일 두 개를 읽는 도구에 비동기 이벤트나
플러그인, 분산 서비스가 필요할 이유가 없다. 후보가 사실상 2개로 좁혀지므로
[03-tradeoff-evaluation-atam.md](../03-tradeoff-evaluation-atam.md)의 ATAM
비교는 생략한다 — FR1·FR3가 Kano "Basic"이라 과도한 평가가 낭비이기도 하다.

## Decision Outcome

**옵션 1(Layered 단일 파일 스크립트)을 채택**한다. FR1~FR4를 실제 코드로 만족시킬
수 있는 건 옵션 1뿐이고(옵션 2는 Claude Code 세션 밖에서 재사용 불가 — PRD의
Business Justification과 정면으로 배치됨), 계층 3개짜리 단순 구조라 아키텍처
자체에 대한 트레이드오프 논쟁의 여지가 거의 없다.

### Consequences

**장점**
- 외부 의존성 없이(Supportability NFR) 어디서든 실행 가능
- 계층이 단순해서 5단계 TDD 사이클을 바로 적용 가능

**단점 / 리스크**
- 카탈로그가 아주 커지면(수천 항목) 단순 문자열 검색은 느려질 수 있음 — 지금은
  Usability Goal(0.5초)로 충분히 커버되는 규모라 재검토는 나중으로 미룸
