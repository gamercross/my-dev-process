# 5단계: 구현

> 상태: 🟡 진행 중 — 첫 사례([Two Sum](../../implementations/algorithm-track/two-sum/)) 완료

패턴 스켈레톤을 실제 문제/요구사항에 맞게 완성하는 단계.

```mermaid
flowchart LR
    Red[Red<br/>실패하는 테스트] --> Green[Green<br/>최소한으로 통과]
    Green --> Refactor[Refactor<br/>구조 개선]
    Refactor --> Red
    Refactor -.완료.-> Next[6단계: 서비스]
```

## 방향을 정하는 표준 개념

| 개념 | 문서 | 핵심 |
|---|---|---|
| 개발 리듬 | [01-tdd-red-green-refactor.md](01-tdd-red-green-refactor.md) | Kent Beck의 TDD Red-Green-Refactor 순환. 알고리즘 트랙은 "Refactor 자리에 최적화"로 변형 |
| 테스트 설계 | [02-boundary-value-equivalence.md](02-boundary-value-equivalence.md) | ISO/IEC/IEEE 29119의 동등분할 + 경계값 분석으로 "뭘 엣지 케이스로 볼지" 체계적으로 뽑기 |

## 코드는 어디에 두는가

`docs/`는 방법론·기록용이라 실제 코드는 저장소 최상위 `implementations/`에 둡니다 —
1단계 `sessions/`와 같은 이름 규칙입니다.

```
implementations/<트랙파일명>/<세션 슬러그>/
  solution.py         # 구현 (알고리즘 트랙: 브루트포스 + 최적화 버전 둘 다 남김)
  test_solution.py     # 단위 테스트 + 경계값/차등 테스트
```

## 이 단계에서 하는 일

- 완성 코드 + 단위 테스트 (Red-Green-Refactor 순환으로)
- **Full 등급**: 엣지 케이스는 2단계 EARS Unwanted-behavior 요구사항 기준
- **Xpress/Lite 등급** (2단계를 생략한 경우): 2단계 명세가 없으므로, 대신
  동등분할/경계값 분석만으로 엣지 케이스를 뽑고 브루트포스 대비 차등 테스트로 보강
- 완료 후 [6단계](../06-service/README.md)로 전달

## 실제 사례 — Two Sum

[`implementations/algorithm-track/two-sum/`](../../implementations/algorithm-track/two-sum/)에서
실제로 진행함:

| 단계 | 한 일 |
|---|---|
| Red | `test_solution.py`를 먼저 작성 → `solution.py`가 없어 `ModuleNotFoundError`로 실패 확인 |
| Green | 브루트포스(O(n²))만 작성 → 5개 테스트 전부 통과 |
| Refactor(최적화) | [해시맵 원패스 탐색](../catalog/patterns.md) 패턴으로 O(n) 구현으로 교체 → 5개 테스트 재통과 |

테스트 구성(2단계를 생략한 Xpress 등급이라 경계값 분석으로 대체):
- 예제 케이스, 배열 길이 하한(2개) 경계, 정답이 배열 양끝일 때, 음수 포함
- 브루트포스를 정답 오라클로 둔 차등 테스트(무작위 200회) — 최적화 버전이 항상
  유효한 정답을 내는지 확인
