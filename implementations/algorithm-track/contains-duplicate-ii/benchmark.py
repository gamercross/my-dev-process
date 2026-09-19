"""
6단계(서비스) 성능 확인. 제약조건 상한(1 <= len(nums) <= 10^5)에서
브루트포스 O(n^2) vs 해시맵 O(n)을 실측한다.

브루트포스는 j-i>k인 쌍도 그대로 확인하므로(가지치기 없음) k 값과 무관하게
항상 O(n^2)다 — 전부 서로 다른 값(중복 없음)이면 모든 쌍을 다 훑는 진짜
최악 케이스가 된다. Contains Duplicate 회고의 교훈대로, 상한에서 바로
재지 않고 작은 n에서 추세부터 확인한다.
"""
import random
import time

from solution import contains_nearby_duplicate, contains_nearby_duplicate_bruteforce


def time_it(fn, nums, k):
    start = time.perf_counter()
    result = fn(nums, k)
    elapsed = time.perf_counter() - start
    return result, elapsed


if __name__ == "__main__":
    rng = random.Random(0)

    print("브루트포스 O(n^2) — 중복 없는 배열(최악 케이스), 크기별 추세 확인:")
    prev_time = None
    for n in (500, 1000, 2000, 4000):
        nums = rng.sample(range(-10**9, 10**9), n)
        result, elapsed = time_it(contains_nearby_duplicate_bruteforce, nums, n)
        assert result is False
        ratio = f" ({elapsed / prev_time:.1f}배)" if prev_time else ""
        print(f"  n={n:>6}: {elapsed*1000:8.1f} ms{ratio}")
        prev_time = elapsed

    print()
    n_full = 100_000  # 제약조건 상한
    nums_full = rng.sample(range(-10**9, 10**9), n_full)
    _, fast_time = time_it(contains_nearby_duplicate, nums_full, n_full)
    print(f"해시맵 O(n), n={n_full}(제약조건 상한, 중복 없음 — 최악 케이스): "
          f"{fast_time*1000:.2f} ms")
    print("브루트포스는 O(n^2)라 이 크기에서 직접 측정하면 비현실적 "
          "(위 추세로 추정 시 수십 초~수분)")
