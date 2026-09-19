"""
5단계(구현) 테스트. 2단계 EARS 요구사항(FR1~FR4)을 그대로 테스트 케이스로 옮긴다.
출처: docs/01-problem-save/sessions/project-track/2026-09-19-catalog-search-cli.md
"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path

from catalog_search import DEFAULT_CATALOG_DIR, resolve_catalog_dir, search

HERE = Path(__file__).resolve().parent


def test_fr1_finds_existing_pattern():
    # When 사용자가 키워드로 실행하면 the CLI는 shall 일치하는 블록을 찾아 출력한다
    result = search("해시맵")
    assert "patterns.md" in result


def test_fr2_fallback_message_when_no_match():
    # If 일치하는 항목이 없으면 then the CLI는 shall 안내 메시지를 출력한다
    result = search("이런키워드는존재하지않는다zzz")
    assert "일치 항목 없음" in result
    assert "표준 카탈로그" in result


def test_fr2_cli_exit_code_zero_on_no_match():
    # "일치 없음"은 에러가 아니므로 종료 코드는 0이어야 한다
    script = HERE / "catalog_search.py"
    proc = subprocess.run(
        [sys.executable, str(script), "이런키워드는존재하지않는다zzz"],
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0


def test_fr3_case_insensitive_search():
    # The CLI는 shall 항상 대소문자 구분 없이 검색한다.
    # 출력 메시지는 사용자가 입력한 키워드 원문을 그대로 보여주므로 문자열이
    # 다를 수 있다 — 검사할 건 "셋 다 찾았는가"이지 "출력이 똑같은가"가 아니다.
    for keyword in ("two sum", "TWO SUM", "Two Sum"):
        result = search(keyword)
        assert "patterns.md" in result, f"'{keyword}'로 찾지 못함: {result}"


def test_fr4_catalog_root_env_var_overrides_default():
    # Where CATALOG_ROOT가 설정되어 있으면 the CLI는 shall 그 경로의 catalog/를 쓴다
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        catalog = tmp_path / "catalog"
        catalog.mkdir()
        (catalog / "patterns.md").write_text(
            "## 테스트전용패턴\n키워드: 유니크마커123\n", encoding="utf-8"
        )
        (catalog / "checklist.md").write_text("", encoding="utf-8")

        os.environ["CATALOG_ROOT"] = str(tmp_path)
        try:
            assert resolve_catalog_dir() == catalog
            result = search("유니크마커123")
        finally:
            del os.environ["CATALOG_ROOT"]

        assert "patterns.md" in result


def test_default_catalog_dir_is_repo_catalog():
    assert DEFAULT_CATALOG_DIR.name == "catalog"
    assert (DEFAULT_CATALOG_DIR / "patterns.md").exists()


def run_all():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
        print(f"PASS {t.__name__}")
    print(f"\n{len(tests)}개 테스트 통과")


if __name__ == "__main__":
    run_all()
