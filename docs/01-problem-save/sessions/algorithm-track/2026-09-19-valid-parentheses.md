제목: Valid Parentheses
출처(플랫폼, 문제번호): LeetCode #20
시나리오(원문 요약): 괄호 문자로만 이루어진 문자열이 주어질 때, 여는 괄호와 닫는 괄호가 올바른 순서와 짝으로 맞춰져 있는지 판별한다.
입력 형식 + 제약조건(수학적 표기, 예: 1 ≤ n ≤ 10^5): s(문자열, 1 ≤ len(s) ≤ 10^4, '(', ')', '{', '}', '[', ']'로만 구성)
출력 형식: boolean (true/false)
예제 입출력(최소 1쌍): s="()[]{}" → true, s="(]" → false
태그(3단계 패턴 분류와 연결): 스택, 괄호매칭
상태(미착수 / 분석중 / 풀이완료 / 복습필요): 분석중

## 게이트 로그

등급: Xpress ([scope-tiers.md](../../../00-overview/scope-tiers.md) — 알고리즘 트랙 단순 문제)

| 게이트 | 결정 | 근거 |
|---|---|---|
| 1 → 2 | Skip | 알고리즘 트랙 단순 문제 — [2단계 적용 범위](../../../02-problem-analysis/README.md) 규칙에 따라 무거운 파이프라인 생략 |
| 2 → 3 | Go | (2단계 Skip 상태로 바로 진입) |

## 3단계: 패턴 분석

`catalog/patterns.md`를 "스택"·"괄호" 키워드로 검색 → **일치 항목 없음**(지금까지
등록된 패턴은 "해시맵 원패스 탐색" 하나뿐). SKILL.md 명령 2 step 3대로 표준
카탈로그([01-algorithm-paradigms.md](../../../03-pattern-analysis/01-algorithm-paradigms.md))로
폴백 — 이 저장소에서 "검색 실패 → 폴백" 경로가 실제로 처음 타본 사례.

CLRS 4대 설계 패러다임(분할정복/DP/그리디/백트래킹) 중 어디에도 깔끔히 안 맞음 —
Two Sum의 해시맵처럼 이것도 **구현 기법 패턴**(스택 기반 매칭)에 해당한다.
선택 근거: 여는 괄호를 스택에 쌓아두고 닫는 괄호가 나올 때마다 스택 맨 위와
짝이 맞는지 확인하면 한 번의 순회로 판별 가능 — 그 외 대안(정규식으로 반복
치환 등)보다 직관적이고 O(n)이 자연스럽게 나옴.

**게이트**: `3 → 4` = Go — 선택 근거 기록 완료.

## 4단계: 패턴 구현 (스켈레톤)

"Make it work" 원칙대로 브루트포스부터: 짝이 맞는 괄호 쌍("()", "[]", "{}")을
문자열에서 찾을 때마다 제거하는 걸 더 이상 지울 게 없을 때까지 반복하고, 마지막에
빈 문자열이면 true. [`implementations/algorithm-track/valid-parentheses/solution.py`](../../../../implementations/algorithm-track/valid-parentheses/solution.py)에
`valid_parentheses_bruteforce`로 구현, 예제 케이스로 스모크 테스트:

```
$ python3 -c "from solution import valid_parentheses_bruteforce as f; \
  print(f('()[]{}'), f('(]'), f('([)]'), f('{[]}'))"
True False False True
```

**게이트**: `4 → 5` = (대기) — 5단계(TDD로 스택 최적화 + 경계값 테스트)는 다음
진행.
