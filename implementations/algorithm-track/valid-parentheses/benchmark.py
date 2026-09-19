"""
6단계(서비스) 성능 확인. 제약조건 상한(1 <= len(s) <= 10^4)에서
브루트포스 O(n^2) vs 스택 O(n)을 실측한다.

지난 Two Sum 벤치마크에서 "최악 케이스"라고 주장한 입력이 실제로는 최악이
아니었던 걸 회고에서 발견했다(catalog/checklist.md "6단계 성능 실측
체크리스트" 참고) — 이번엔 여러 크기에서 실제로 돌려서 O(n^2) 추세를 눈으로
확인한다. 완전히 중첩된 문자열("((...))")은 매 순회마다 가운데 있는 "()"
하나만 지워지므로(한 번에 한 쌍씩, 매번 전체를 다시 훑음) 진짜 최악 케이스다.
"""
import time

from solution import valid_parentheses, valid_parentheses_bruteforce


def fully_nested(n_pairs: int) -> str:
    return "(" * n_pairs + ")" * n_pairs


def time_it(fn, s):
    start = time.perf_counter()
    result = fn(s)
    elapsed = time.perf_counter() - start
    return result, elapsed


if __name__ == "__main__":
    print("브루트포스 O(n^2) — 완전 중첩 문자열, 크기별 추세 확인:")
    prev_time = None
    for n_pairs in (500, 1000, 2000, 4000):
        s = fully_nested(n_pairs)
        result, elapsed = time_it(valid_parentheses_bruteforce, s)
        assert result is True
        ratio = f" ({elapsed / prev_time:.1f}배)" if prev_time else ""
        print(f"  len={len(s):>6}: {elapsed*1000:8.1f} ms{ratio}")
        prev_time = elapsed

    print()
    n_pairs = 5_000  # len(s) == 10_000, 제약조건 상한
    s = fully_nested(n_pairs)
    brute_result, brute_time = time_it(valid_parentheses_bruteforce, s)
    fast_result, fast_time = time_it(valid_parentheses, s)
    assert brute_result == fast_result is True

    print(f"n = {len(s)} (제약조건 상한, 완전 중첩)")
    print(f"브루트포스 O(n^2): {brute_time*1000:.1f} ms")
    print(f"스택 O(n):         {fast_time*1000:.3f} ms")
    print(f"배속:              {brute_time/fast_time:.0f}배")
