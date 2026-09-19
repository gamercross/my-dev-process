"""
Contains Duplicate (LeetCode #217) —
sessions/algorithm-track/2026-09-17-contains-duplicate.md

4단계(패턴 구현) 원칙(docs/04-pattern-implementation/01-algorithm-track-skeleton.md):
"Make it work, make it right, make it fast" — 브루트포스로 먼저 정답만 확인.
"""


def contains_duplicate_bruteforce(nums):
    """Green 단계: 정답 오라클. O(n^2), 모든 쌍을 확인한다."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


def contains_duplicate(nums):
    """Refactor(알고리즘 트랙: 최적화) 단계.

    docs/catalog/patterns.md의 "해시맵 원패스 탐색" 패턴의 해시셋 변형. O(n) 시간,
    O(n) 공간 — 배열을 한 번만 순회하며 "지금까지 본 값"을 해시셋에 저장해두고
    이미 나온 값인지 O(1)에 확인한다.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
