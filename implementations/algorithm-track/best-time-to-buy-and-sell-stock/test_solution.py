import random

from solution import max_profit, max_profit_bruteforce


def test_example_case():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5


def test_monotonically_decreasing_has_zero_profit():
    assert max_profit([7, 6, 4, 3, 1]) == 0


def test_single_day_has_zero_profit():
    assert max_profit([5]) == 0


def test_monotonically_increasing_profit_is_last_minus_first():
    assert max_profit([1, 2, 3, 4, 5]) == 4


def test_all_equal_prices_has_zero_profit():
    assert max_profit([3, 3, 3, 3]) == 0


def test_max_before_min_is_not_used_as_answer():
    # 최댓값이 최솟값보다 먼저 나오면 그 쌍은 못 쓴다 — 브루트포스도 같이 검증
    prices = [9, 1, 2]
    assert max_profit_bruteforce(prices) == 1
    assert max_profit(prices) == 1


def test_optimized_matches_bruteforce_on_random_input():
    random.seed(42)
    for _ in range(200):
        n = random.randint(1, 30)
        prices = [random.randint(0, 100) for _ in range(n)]
        assert max_profit(prices) == max_profit_bruteforce(prices)


def run_all():
    tests = [
        test_example_case,
        test_monotonically_decreasing_has_zero_profit,
        test_single_day_has_zero_profit,
        test_monotonically_increasing_profit_is_last_minus_first,
        test_all_equal_prices_has_zero_profit,
        test_max_before_min_is_not_used_as_answer,
        test_optimized_matches_bruteforce_on_random_input,
    ]
    for t in tests:
        t()
        print(f"PASS {t.__name__}")
    print(f"{len(tests)}개 테스트 통과")


if __name__ == "__main__":
    run_all()
