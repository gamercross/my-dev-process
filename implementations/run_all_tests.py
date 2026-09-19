#!/usr/bin/env python3
"""
implementations/ 아래 모든 test_solution.py를 한 번에 찾아서 돌린다.
각 폴더가 독립된 모듈 네임스페이스(solution.py)를 쓰므로, 매번 sys.path를
그 폴더로 바꿔서 격리 실행한다.
"""
import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def find_test_dirs():
    return sorted(p.parent for p in ROOT.rglob("test_solution.py"))


def run_one(test_dir: Path) -> bool:
    sys.path.insert(0, str(test_dir))
    try:
        for mod_name in ("solution", "test_solution"):
            sys.modules.pop(mod_name, None)
        test_mod = importlib.import_module("test_solution")
        test_mod.run_all()
        return True
    except Exception as e:  # noqa: BLE001 - 요약 리포트용으로 전부 잡아서 계속 진행
        print(f"FAIL {test_dir.relative_to(ROOT)}: {e}")
        return False
    finally:
        sys.path.remove(str(test_dir))


if __name__ == "__main__":
    test_dirs = find_test_dirs()
    results = {}
    for d in test_dirs:
        rel = d.relative_to(ROOT)
        print(f"=== {rel} ===")
        results[str(rel)] = run_one(d)
        print()

    passed = sum(results.values())
    total = len(results)
    print(f"요약: {passed}/{total}개 구현 전체 테스트 통과")
    if passed != total:
        sys.exit(1)
