"""
Contains Duplicate II (LeetCode #219) —
sessions/algorithm-track/2026-09-19-contains-duplicate-ii.md

4단계(패턴 구현) 원칙: "Make it work, make it right, make it fast" —
브루트포스로 먼저 정답만 확인. 5단계에서 해시맵 O(n)으로 최적화한다.
"""


def contains_nearby_duplicate_bruteforce(nums, k):
    """Green 단계: 정답 오라클. 모든 (i, j) 쌍을 확인하므로 O(n^2)."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j] and j - i <= k:
                return True
    return False


def contains_nearby_duplicate(nums, k):
    """Refactor(알고리즘 트랙: 최적화) 단계.

    docs/catalog/patterns.md의 "해시맵 원패스 탐색" 패턴 변형 — "봤는지 여부"가
    아니라 "마지막으로 본 인덱스"를 저장한다. 값을 다시 만나면 그 인덱스와의
    거리를 O(1)로 바로 비교한다. O(n) 시간, O(min(n, 값의 종류 수)) 공간.
    """
    last_seen = {}
    for i, num in enumerate(nums):
        if num in last_seen and i - last_seen[num] <= k:
            return True
        last_seen[num] = i
    return False
