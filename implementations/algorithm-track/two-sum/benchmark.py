"""
6단계(서비스) 성능 확인. 제약조건(2 <= len(nums) <= 10^4) 상한에서
브루트포스 O(n^2) vs 최적화 O(n)을 실측한다.

정답 쌍을 배열 맨 끝(인덱스 n-2, n-1)에 두고, 나머지는 우연히 같은 합이 나올
확률이 무시할 수 있는 넓은 정수 범위에서 뽑는다 — 브루트포스가 사실상 전체를
다 훑어야 하는 최악 케이스에 가깝게 만든 것.
"""
import random
import time

from solution import two_sum, two_sum_bruteforce


def time_it(fn, nums, target):
    start = time.perf_counter()
    result = fn(nums, target)
    elapsed = time.perf_counter() - start
    return result, elapsed


if __name__ == "__main__":
    n = 10_000  # 제약조건 상한
    rng = random.Random(0)
    rest = rng.sample(range(-10**9, 10**9), n - 2)
    a, b = 10**9, 10**9 - 1  # rest 범위 밖의 값이라 겹칠 일이 없다
    nums = rest + [a, b]
    target = a + b

    brute_result, brute_time = time_it(two_sum_bruteforce, nums, target)
    fast_result, fast_time = time_it(two_sum, nums, target)

    assert nums[brute_result[0]] + nums[brute_result[1]] == target
    assert nums[fast_result[0]] + nums[fast_result[1]] == target

    print(f"n = {n} (제약조건 상한, 정답이 배열 맨 끝인 최악 케이스)")
    print(f"브루트포스 O(n^2): {brute_time*1000:.1f} ms")
    print(f"해시맵 O(n):       {fast_time*1000:.3f} ms")
    print(f"배속:              {brute_time/fast_time:.0f}배")
