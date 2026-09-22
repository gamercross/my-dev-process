import random
import time

from solution import max_profit, max_profit_bruteforce


def make_worst_case(n):
    # 브루트포스가 가지치기할 방법이 없도록 무작위 가격(중복 없이 넓은 범위)
    random.seed(1)
    return random.sample(range(0, 1_000_000), n)


def timeit(fn, *args):
    start = time.perf_counter()
    fn(*args)
    return (time.perf_counter() - start) * 1000


if __name__ == "__main__":
    print("=== 추세 확인 (브루트포스 O(n^2)) ===")
    for n in (500, 1000, 2000, 4000):
        prices = make_worst_case(n)
        ms = timeit(max_profit_bruteforce, prices)
        print(f"n={n}: {ms:.1f} ms")

    print()
    print("=== 상한에서 최적화 버전 측정 ===")
    n = 100_000
    prices = make_worst_case(n)
    ms = timeit(max_profit, prices)
    print(f"n={n}: {ms:.3f} ms (최적화 O(n))")
