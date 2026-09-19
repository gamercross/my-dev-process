"""
Two Sum (LeetCode #1) — sessions/algorithm-track/2026-09-17-two-sum.md

4단계(패턴 구현) 원칙(docs/04-pattern-implementation/01-algorithm-track-skeleton.md):
"Make it work, make it right, make it fast" — 브루트포스로 먼저 정답만 확인.
"""


def two_sum_bruteforce(nums, target):
    """Green 단계: 정답 오라클. O(n^2), 모든 쌍을 확인한다."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


def two_sum(nums, target):
    """Refactor(알고리즘 트랙: 최적화) 단계.

    docs/catalog/patterns.md의 "해시맵 원패스 탐색" 패턴 적용. O(n) 시간,
    O(n) 공간 — 배열을 한 번만 순회하며 "지금까지 본 값"을 해시맵에 저장해두고
    필요한 짝이 이미 나왔는지 O(1)에 확인한다.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None
