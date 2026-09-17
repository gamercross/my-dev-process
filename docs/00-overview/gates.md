# 게이트 규정 — 단계를 잘 넘어가고 있는지 확인하는 방법

7단계를 그냥 순서대로 밟는 것과, **각 단계를 제대로 마쳤는지 확인하고 넘어가는 것**은
다릅니다. 이 문서는 두 표준 개념을 결합해 "다음 단계로 넘어가도 되는가"를 명확한
규정으로 만듭니다.

## 쓰는 두 가지 표준 개념

1. **DoR/DoD (스크럼)** — 각 단계마다 "시작하려면 뭐가 갖춰져 있어야 하는가"(Definition
   of Ready, 진입기준)와 "끝났다고 부르려면 뭐가 갖춰져 있어야 하는가"(Definition of
   Done, 완료기준)를 미리 정해둡니다. DoR은 다음 단계로 들어가는 조건, DoD는 지금
   단계에서 나가는 조건입니다.
2. **Stage-Gate (Robert G. Cooper)** — 제품 개발에서 단계 사이마다 "게이트"를 두고,
   미리 정한 기준으로 **Go / Kill / Hold / Recycle** 넷 중 하나를 결정하는 방법론입니다.
   - **Go**: DoD를 충족했다 → 다음 단계로
   - **Recycle**: DoD를 못 채웠다 → 지금 단계로 돌아가 보완
   - **Hold**: 외부 사정(우선순위 변경 등)으로 일시 중단
   - **Kill**: 원문제 정의 자체가 잘못됐다고 판명 → [0단계](README.md#원문제-정의)로

즉 "느낌상 다음으로 넘어가도 될 것 같다"가 아니라, **정해둔 체크리스트를 다 채웠는지로만
판단**합니다.

## 단계별 DoR / DoD

| 단계 | 진입기준 (DoR) | 완료기준 (DoD) |
|---|---|---|
| 0. 원문제 정의 | — (시작점) | 시나리오·원하는 결과·적용 대상 3요소가 문장으로 명시됨 |
| 1. 문제 저장 | 0단계 완료 | 트랙 선택됨, 템플릿 필수 필드 전부 채움(IEEE 830: 문장당 동작 하나, 정성적 표현 없음), 태그 부여됨 |
| 2. 문제 분석 | 1단계 항목 저장 완료 | [`catalog/checklist.md`](../catalog/checklist.md)의 "2단계 파이프라인 체크리스트" 4개 항목 모두 체크 |
| 3. 패턴 분석 | 2단계 요구사항 확정 | [`catalog/checklist.md`](../catalog/checklist.md)의 "3단계 파이프라인 체크리스트" 4개 항목 모두 체크 |
| 4. 패턴 구현 | 3단계 결정(패턴/ADR) 확정 | [Walking Skeleton](../04-pattern-implementation/02-project-track-skeleton.md) 기준으로 주요 컴포넌트가 실제로 연결됨(스모크 테스트 통과) — 또는 알고리즘 트랙은 브루트포스가 정답을 냄 |
| 5. 구현 | 4단계 스켈레톤 검증 완료 | 단위 테스트 통과, 2단계 EARS Unwanted-behavior(엣지 케이스) 요구사항 전부 커버 |
| 6. 서비스 | 5단계 구현·테스트 통과 | 2단계 Planguage Goal을 실측해서 달성 여부가 기록됨 (미달이어도 "기록됨"이면 조건 충족 — 미달 자체가 7단계 입력이 됨) |
| 7. 유지보수 | 6단계 실측 완료 | 회고 작성 + 5 Whys로 근본원인 도달 + `catalog/patterns.md` 또는 `checklist.md` 갱신 + git 커밋 |

DoD 열은 앞 단계가 이미 만들어둔 체크리스트를 그대로 가리킵니다 — **게이트 규정은
새로운 기준을 만드는 게 아니라, 이미 흩어져 있던 기준들을 "언제 확인하는가"의 순서로
모아놓은 것**입니다.

## 게이트 통과 기록 (이 프로젝트 자체)

| 게이트 | 결정 | 근거 |
|---|---|---|
| 0 → 1 | Go | 원문제 정의 문장 확정 |
| 1 → 2 | Go | 템플릿 3종 작성 완료 |
| 2 → 3 | Go | 5단계 파이프라인 체크리스트 충족, [applied-example.md](../02-problem-analysis/applied-example.md) 참고 |
| 3 → 4 | Go | [ADR-0001](../03-pattern-analysis/adr/0001-storage-and-interface.md) Accepted |
| 4 → 5 | Go | 트랙 자동 인식 스모크 테스트 통과 ([04단계 README](../04-pattern-implementation/README.md)) |
| 5 → 6 | (대기) | 5단계 미착수 |

## 출처
- [What Is the Difference Between DoD and DoR? - Scrum.org](https://www.scrum.org/resources/blog/what-difference-between-definition-done-dod-and-definition-ready-dor)
- Cooper, R. G., *The Stage-Gate® System* — [Toolshero 정리](https://www.toolshero.com/innovation/stage-gate-process/)
