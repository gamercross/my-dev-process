"""
5단계(구현) 테스트. TDD + 동등분할/경계값 분석 적용.
출처: docs/05-implementation/01-tdd-red-green-refactor.md,
      docs/05-implementation/02-boundary-value-equivalence.md

참고: 4단계에서 이미 브루트포스가 예제 4개를 정확히 맞혔기 때문에, 이번엔
Two Sum 때처럼 "처음엔 다 실패"하는 Red 구간이 없다 — 대신 경계값 분석으로
브루트포스가 못 버틸 수도 있는 케이스들을 체계적으로 찾아내는 게 5단계의
실질적인 작업이다.
"""
import random

from solution import valid_parentheses, valid_parentheses_bruteforce


def test_example_cases():
    assert valid_parentheses("()[]{}") is True
    assert valid_parentheses("(]") is False


def test_minimum_length_boundary():
    # 경계값: len(s)의 하한(1). 길이 1은 홀수라 항상 무효.
    assert valid_parentheses("(") is False
    assert valid_parentheses(")") is False


def test_odd_length_is_always_invalid():
    # 동등분할: 홀수 길이는 짝을 이룰 수 없어 무조건 False인 하나의 클래스
    assert valid_parentheses("(()") is False
    assert valid_parentheses("()(") is False


def test_even_length_but_structurally_invalid():
    # 길이는 짝수라 패리티 검사로는 못 거르고, 실제 짝 맞춤 로직이 필요한 케이스
    assert valid_parentheses("([)]") is False
    assert valid_parentheses("))((") is False


def test_nested_valid():
    assert valid_parentheses("({[]})") is True


def test_length_upper_bound():
    # 경계값: len(s)의 상한(10^4)에서도 정확해야 한다
    s = "()" * 5000  # len == 10000
    assert len(s) == 10_000
    assert valid_parentheses(s) is True


def test_optimized_matches_bruteforce_on_random_input():
    # 차등 테스트: 무작위로 만든(균형 잡힌 것 절반, 임의 문자열 절반) 입력에
    # 대해 최적화 버전과 브루트포스가 항상 같은 답을 내는지 확인
    random.seed(0)
    brackets = "()[]{}"
    for _ in range(200):
        n = random.randint(1, 20)
        s = "".join(random.choice(brackets) for _ in range(n))
        assert valid_parentheses(s) == valid_parentheses_bruteforce(s), s


def run_all():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
        print(f"PASS {t.__name__}")
    print(f"\n{len(tests)}개 테스트 통과")


if __name__ == "__main__":
    run_all()
