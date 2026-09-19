"""
5단계(구현) 테스트. TDD Red-Green-Refactor + 동등분할/경계값 분석 적용.
출처: docs/05-implementation/01-tdd-red-green-refactor.md,
      docs/05-implementation/02-boundary-value-equivalence.md
"""
import random

from solution import two_sum, two_sum_bruteforce


def test_example_case():
    # 1단계 세션 파일(sessions/algorithm-track/2026-09-17-two-sum.md)의 예제 입출력
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_minimum_length_boundary():
    # 경계값: len(nums)의 하한(2 ≤ len(nums)) 바로 위 — 원소 2개짜리 배열
    assert two_sum([3, 3], 6) == [0, 1]


def test_answer_spans_array_boundaries():
    # 경계값: 정답이 배열의 첫 원소와 마지막 원소일 때
    nums = [5, 1, 1, 1, 1, 4]
    assert two_sum(nums, 9) == [0, 5]


def test_negative_numbers():
    # 동등분할: 음수 구간도 하나의 클래스로 봐야 함
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]


def test_optimized_matches_bruteforce_on_random_input():
    # 차등 테스트(differential testing): 브루트포스를 정답 오라클로 두고,
    # 최적화 버전이 항상 유효한 정답(합이 target과 일치)을 내는지 확인.
    # 정답이 여러 쌍일 수 있으므로 인덱스 자체가 아니라 "그 인덱스 쌍의 합"으로 비교한다.
    random.seed(0)
    for _ in range(200):
        n = random.randint(2, 20)
        nums = random.sample(range(-50, 50), n)
        i, j = sorted(random.sample(range(n), 2))
        target = nums[i] + nums[j]

        brute = two_sum_bruteforce(nums, target)
        fast = two_sum(nums, target)

        assert brute is not None and fast is not None
        assert nums[brute[0]] + nums[brute[1]] == target
        assert nums[fast[0]] + nums[fast[1]] == target


def run_all():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
        print(f"PASS {t.__name__}")
    print(f"\n{len(tests)}개 테스트 통과")


if __name__ == "__main__":
    run_all()
