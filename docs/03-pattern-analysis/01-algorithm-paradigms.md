# 알고리즘 트랙 — 후보 패턴 도출

문제를 어떤 알고리즘으로 풀지 막막할 때, 임의로 아무 자료구조나 떠올리기보다 **표준
알고리즘 설계 패러다임 4가지**를 체크리스트처럼 훑으면 후보를 빠르게 좁힐 수 있습니다.
CLRS(Cormen/Leiserson/Rivest/Stein)를 비롯한 알고리즘 교재들이 공통으로 쓰는 분류입니다.

## 4대 알고리즘 설계 패러다임

| 패러다임 | 핵심 아이디어 | 적합한 문제 특징 |
|---|---|---|
| Divide and Conquer (분할정복) | 문제를 독립적인 부분문제로 쪼개 각각 풀고 결합 | 부분문제가 서로 독립적일 때. 대용량 데이터에 특히 효율적 |
| Dynamic Programming (동적계획법) | 부분문제를 재귀적으로 풀되 결과를 저장해 중복 계산 제거 | 부분문제가 겹치고(overlapping subproblems), 최적 부분구조(optimal substructure)를 가질 때 |
| Greedy (탐욕법) | 매 단계에서 지역적으로 최선인 선택을 함 | 지역 최적해가 전역 최적해로 이어짐이 증명 가능할 때. 빠르고 단순하지만 항상 전역 최적은 아님 |
| Backtracking (백트래킹) | 제약조건을 만족하는 해를 탐색하며, 막히면 되돌아감 | 제약 충족 문제(constraint satisfaction), 조합 탐색 |

## 사용 절차

1. **[문제 분석](../02-problem-analysis/README.md) 산출물(태그, 제약조건)을 놓고 4개 중
   후보를 1~2개로 좁힌다.** 예: "부분문제가 겹치는가?"에 예라고 답했으면 DP 후보.
2. `docs/catalog/patterns.md`에서 같은 태그의 과거 항목을 검색한다 (구체적 구현 아이디어).
3. 후보가 여전히 2개 이상이면 [03-tradeoff-evaluation-atam.md](03-tradeoff-evaluation-atam.md)의
   시나리오 비교 방식을 간소화해서 적용한다 (시간복잡도 vs 구현 난이도 vs 코드 길이).
4. 선택 근거를 한 줄 기록 — 7단계 회고에서 "왜 이걸 골랐는지" 복기 가능하게.

## 출처
- Cormen, Leiserson, Rivest, Stein, *Introduction to Algorithms* (CLRS) — 표준 알고리즘
  패러다임 분류의 근거 교재
- [What Are the 4 Types of Algorithms? - DesignGurus](https://www.designgurus.io/answers/detail/what-are-the-4-types-of-algorithm)
