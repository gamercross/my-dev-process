import contextlib
import importlib.util
import io
from pathlib import Path


def _load_run_all_tests_module(repo_root: Path):
    path = repo_root / "implementations" / "run_all_tests.py"
    spec = importlib.util.spec_from_file_location("run_all_tests_module", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_test_suite(repo_root: Path, load_module=_load_run_all_tests_module) -> dict:
    # load_module은 의도적으로 주입 가능하게 뒀다: 기본값(_load_run_all_tests_module)은
    # 실제 implementations/run_all_tests.py를 통째로 다시 실행하는데, 그게 이
    # 대시보드 자신의 테스트 파일(이 파일)도 다시 발견해서 collect_tests를 또
    # 호출하면 무한 재귀가 된다. 그래서 단위 테스트는 항상 가짜 load_module을
    # 주입해서 이 재귀 경로를 아예 타지 않는다 (test_dashboard.py 참고).
    module = load_module(repo_root)
    test_files = module.find_test_files()
    results = {}
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        for f in test_files:
            rel = f.relative_to(repo_root / "implementations")
            results[str(rel)] = module.run_one(f)
    return results


def collect_tests(repo_root: Path, load_module=_load_run_all_tests_module) -> dict:
    results = run_test_suite(repo_root, load_module=load_module)
    passed = sum(results.values())
    total = len(results)
    lines = [f"- 테스트 파일: {passed}/{total}개 전체 통과"]
    failed = [name for name, ok in results.items() if not ok]
    if failed:
        lines.append("- 실패: " + ", ".join(failed))
    return {"title": "테스트 결과", "lines": lines}
