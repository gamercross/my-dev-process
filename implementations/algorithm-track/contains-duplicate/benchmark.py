"""
6단계(서비스) 성능 확인. 제약조건은 1 <= len(nums) <= 10^5.

브루트포스 O(n^2)는 n=10^5에서 약 5*10^9회 비교가 필요해(작은 n에서 측정한
추세로 추정하면 약 1~2분), 그때그때 결과를 보며 반복 실행하기엔 비현실적이므로
최적화 버전만 제약조건 상한(n=10^5)에서 측정하고, 브루트포스는 훨씬 작은 n에서
측정해 O(n^2) 증가 추세만 보여준다.
"""
import random
import time

from solution import contains_duplicate, contains_duplicate_bruteforce


def time_it(fn, nums):
    start = time.perf_counter()
    result = fn(nums)
    elapsed = time.perf_counter() - start
    return result, elapsed


if __name__ == "__main__":
    rng = random.Random(0)

    # 최적화 버전: 제약조건 상한에서 측정. 중복 없음(worst case, 끝까지 다 순회).
    n_full = 100_000
    nums_full = rng.sample(range(-10**9, 10**9), n_full)
    _, fast_time = time_it(contains_duplicate, nums_full)
    print(f"최적화(해시셋) O(n), n={n_full} (제약조건 상한, 중복 없음 — 최악 케이스): "
          f"{fast_time*1000:.2f} ms")

    # 브루트포스: O(n^2)라 상한에서는 못 돌리므로 훨씬 작은 n으로 추세만 확인
    print()
    print("브루트포스 O(n^2) — 제약조건 상한(10^5)은 비현실적이라 축소해서 증가 추세만 확인:")
    for n in (1_000, 2_000, 4_000):
        nums = rng.sample(range(-10**9, 10**9), n)
        _, brute_time = time_it(contains_duplicate_bruteforce, nums)
        print(f"  n={n:>6}: {brute_time*1000:8.1f} ms")
