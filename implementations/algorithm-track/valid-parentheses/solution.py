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


def valid_parentheses(s: str) -> bool:
    """Refactor(알고리즘 트랙: 최적화) 단계 — 스택 기반 매칭. O(n) 시간,
    O(n) 공간. 여는 괄호를 스택에 쌓고, 닫는 괄호가 나오면 스택 맨 위와
    짝이 맞는지 한 번만 확인한다.

    빠른 실패: 길이가 홀수면 무조건 무효이므로 스택을 만들 필요도 없다
    (동등분할 — 홀수 길이는 항상 False인 클래스)."""
    if len(s) % 2 != 0:
        return False

    closing_to_opening = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in closing_to_opening:
            if not stack or stack.pop() != closing_to_opening[ch]:
                return False
        else:
            stack.append(ch)
    return not stack
