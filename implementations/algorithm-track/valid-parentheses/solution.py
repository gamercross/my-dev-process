"""
Valid Parentheses (LeetCode #20) —
sessions/algorithm-track/2026-09-19-valid-parentheses.md

4단계(패턴 구현) 원칙: "Make it work, make it right, make it fast" —
브루트포스로 먼저 정답만 확인. 5단계에서 스택 기반 O(n)으로 최적화한다.
"""


def valid_parentheses_bruteforce(s: str) -> bool:
    """Green 단계: 짝이 맞는 쌍을 찾을 때마다 지우고, 더 지울 게 없을 때
    빈 문자열이면 유효하다. 매 반복마다 문자열을 훑으므로 O(n^2)에 가깝다."""
    pairs = ("()", "[]", "{}")
    changed = True
    while changed:
        changed = False
        for pair in pairs:
            if pair in s:
                s = s.replace(pair, "", 1)
                changed = True
    return s == ""


valid_parentheses = valid_parentheses_bruteforce
