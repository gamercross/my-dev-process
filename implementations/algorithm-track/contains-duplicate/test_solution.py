"""
5단계(구현) 테스트. TDD Red-Green-Refactor + 동등분할/경계값 분석 적용.
출처: docs/05-implementation/01-tdd-red-green-refactor.md,
      docs/05-implementation/02-boundary-value-equivalence.md
"""
import random

from solution import contains_duplicate, contains_duplicate_bruteforce


def test_example_case():
    # 1단계 세션 파일(sessions/algorithm-track/2026-09-17-contains-duplicate.md)의 예제
    assert contains_duplicate([1, 2, 3, 1]) is True


def test_all_unique_returns_false():
    assert contains_duplicate([1, 2, 3, 4]) is False


def test_minimum_length_boundary():
    # 경계값: len(nums)의 하한(1 ≤ len(nums)) — 원소 1개짜리 배열은 중복이 불가능
    assert contains_duplicate([7]) is False


def test_duplicate_at_first_and_last_index():
    # 경계값: 중복이 배열의 양 끝에 걸쳐 있을 때
    nums = [5, 1, 2, 3, 4, 5]
    assert contains_duplicate(nums) is True


def test_negative_numbers():
    # 동등분할: 음수 구간도 하나의 클래스로 봐야 함
    assert contains_duplicate([-1, -2, -3, -1]) is True


def test_optimized_matches_bruteforce_on_random_input():
    # 차등 테스트(differential testing): 브루트포스를 정답 오라클로 두고,
    # 최적화 버전이 항상 같은 참/거짓을 내는지 확인.
    random.seed(0)
    for _ in range(200):
        n = random.randint(1, 30)
        # 중복이 섞이도록 값의 범위를 배열 길이보다 좁게 잡는다
        nums = [random.randint(-10, 10) for _ in range(n)]

        brute = contains_duplicate_bruteforce(nums)
        fast = contains_duplicate(nums)

        assert brute == fast


def run_all():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
        print(f"PASS {t.__name__}")
    print(f"\n{len(tests)}개 테스트 통과")


if __name__ == "__main__":
    run_all()
