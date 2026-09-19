"""
5단계(구현) 테스트. 동등분할/경계값 분석 적용.
출처: docs/05-implementation/02-boundary-value-equivalence.md
"""
import random

from solution import contains_nearby_duplicate, contains_nearby_duplicate_bruteforce


def test_example_cases():
    assert contains_nearby_duplicate([1, 2, 3, 1], 3) is True
    assert contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 2) is False
    assert contains_nearby_duplicate([1, 0, 1, 1], 1) is True


def test_k_zero_is_always_false():
    # 동등분할: k=0이면 i==j만 허용되는데 i!=j가 필요하므로 항상 False인 클래스
    assert contains_nearby_duplicate([1, 1, 1], 0) is False


def test_minimum_length_boundary():
    # 경계값: len(nums)의 하한(1) — 쌍 자체가 불가능
    assert contains_nearby_duplicate([5], 0) is False


def test_distance_exactly_at_k_boundary():
    # 경계값: 거리가 k와 정확히 같으면 참(포함), k+1이면 거짓(제외)
    assert contains_nearby_duplicate([1, 2, 3, 4, 1], 4) is True
    assert contains_nearby_duplicate([1, 2, 3, 4, 5, 1], 4) is False


def test_k_larger_than_array_length_reduces_to_plain_contains_duplicate():
    # 동등분할: k가 배열 길이 이상이면 거리 제한이 사실상 없는 것과 같음
    assert contains_nearby_duplicate([1, 2, 3, 4, 5], 100) is False
    assert contains_nearby_duplicate([1, 2, 3, 4, 1], 100) is True


def test_negative_numbers():
    assert contains_nearby_duplicate([-1, -2, -1], 2) is True


def test_optimized_matches_bruteforce_on_random_input():
    random.seed(0)
    for _ in range(200):
        n = random.randint(1, 30)
        nums = [random.randint(-5, 5) for _ in range(n)]
        k = random.randint(0, n)
        assert contains_nearby_duplicate(nums, k) == contains_nearby_duplicate_bruteforce(
            nums, k
        ), (nums, k)


def run_all():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
        print(f"PASS {t.__name__}")
    print(f"\n{len(tests)}개 테스트 통과")


if __name__ == "__main__":
    run_all()
