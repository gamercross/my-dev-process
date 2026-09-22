"""
5단계(구현) 테스트. 2단계 EARS 요구사항(FR1~FR5)을 그대로 테스트 케이스로 옮긴다.
출처: docs/01-problem-save/sessions/project-track/2026-09-22-progress-dashboard-generator.md

주의: 이 테스트들은 절대로 실제 REPO_ROOT를 기본(주입 없는) collect_tests/
render_report/main()에 통과시키지 않는다 — 그렇게 하면 실제
implementations/run_all_tests.py가 다시 실행되면서 이 테스트 파일 자신을 다시
발견해 재귀 호출된다(collectors/tests.py의 주석 참고). collect_tests는 항상
가짜 load_module을, render_report는 항상 가짜 collectors 목록을 주입해서 쓴다.
collect_tracker/collect_links는 run_all_tests.py를 건드리지 않아 재귀 위험이
없으므로 실제 저장소를 대상으로 통합 테스트해도 안전하다.
"""
import os
import tempfile
from pathlib import Path

import core
from collectors.links import collect_links, find_broken_links
from collectors.tests import collect_tests
from collectors.tracker import parse_tracker_table, summarize_rows

FIXTURE_TABLE = """\
## 트래커

| 문제/프로젝트 | 트랙 | 등급 | 사용한 패턴 | 게이트 | 테스트 | 세션 파일 |
|---|---|---|---|---|---|---|
| A | 알고리즘 | Xpress | 패턴X | 1→7 완주 | 5개 | [보기](a.md) |
| B | 프로젝트 | Full | 패턴Y | 1→7 완주 | 6개 | [보기](b.md) |
| C | 알고리즘 | Xpress | - | 1→2 | - | [보기](c.md) |

다음 섹션
"""


def test_fr1_parse_tracker_table_reads_rows():
    # When 대시보드를 실행하면 the 도구는 shall 트래커 표를 파싱해 집계한다
    rows = parse_tracker_table(FIXTURE_TABLE)
    assert len(rows) == 3
    assert rows[0]["name"] == "A"
    assert rows[1]["tier"] == "Full"


def test_fr1_summarize_rows_counts_completed_only_when_gate_says_so():
    # 경계값: "1→2"처럼 완주가 아닌 게이트는 완주 카운트에서 제외
    rows = parse_tracker_table(FIXTURE_TABLE)
    summary = summarize_rows(rows)
    assert summary["total"] == 3
    assert summary["completed"] == 2
    assert summary["by_track"] == {"알고리즘": 2, "프로젝트": 1}
    assert summary["by_tier"] == {"Xpress": 2, "Full": 1}


def test_fr1_summarize_rows_ignores_dash_test_count():
    # 경계값: 테스트 열이 "-"(미착수)이면 합계에 더하지 않는다
    rows = parse_tracker_table(FIXTURE_TABLE)
    summary = summarize_rows(rows)
    assert summary["total_tests"] == 11  # 5 + 6, C의 "-"는 제외


def test_fr1_collect_tracker_reads_real_tracker_file():
    # run_all_tests.py를 안 건드리므로 실제 저장소로 통합 테스트해도 재귀 위험 없음
    section = core.collect_tracker(core.REPO_ROOT)
    assert section["title"] == "트래커 요약"
    assert any("전체 항목" in line for line in section["lines"])


def test_fr3_find_broken_links_detects_missing_target():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "a.md").write_text(
            "[존재함](b.md) [없음](missing.md) [외부](https://example.com) "
            "[앵커만](#foo)\n",
            encoding="utf-8",
        )
        (root / "b.md").write_text("내용\n", encoding="utf-8")

        result = find_broken_links(root)
        assert result["broken"] == ["a.md: missing.md"]
        # 외부 링크(http)와 앵커 전용(#)은 검사 대상에서 제외되므로 checked에는
        # "존재함"·"없음" 두 개만 들어간다
        assert result["checked"] == 2


def test_fr3_collect_links_section_reports_zero_when_clean():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "a.md").write_text("[존재함](a.md)\n", encoding="utf-8")
        section = collect_links(root)
        assert "깨진 링크: 0개" in section["lines"][1]


def test_fr2_collect_tests_uses_injected_loader_not_the_real_repo():
    # 진짜 run_all_tests.py를 로드하면 이 테스트 파일 자신이 재발견되어 재귀호출
    # 되므로, 항상 가짜 loader를 주입해서 실제 파일 시스템을 건드리지 않는다.
    fake_root = Path("/dummy-repo")

    class FakeModule:
        @staticmethod
        def find_test_files():
            return [
                fake_root / "implementations" / "test_a.py",
                fake_root / "implementations" / "test_b.py",
            ]

        @staticmethod
        def run_one(f):
            return f.name != "test_b.py"

    section = collect_tests(fake_root, load_module=lambda repo_root: FakeModule())
    assert "1/2개 전체 통과" in section["lines"][0]
    assert any("test_b.py" in line for line in section["lines"] if "실패" in line)


def test_fr4_render_report_assembles_sections_in_given_order():
    fake_collectors = [
        lambda repo_root: {"title": "첫번째", "lines": ["- 하나"]},
        lambda repo_root: {"title": "두번째", "lines": ["- 둘"]},
    ]
    report = core.render_report(Path("/dummy"), collectors=fake_collectors)
    assert report.index("## 첫번째") < report.index("## 두번째")
    assert "- 하나" in report and "- 둘" in report


def test_fr5_resolve_output_path_reads_env_var():
    # Where REPORT_OUTPUT이 설정되어 있으면 the 도구는 shall 그 경로에 저장한다
    assert core.resolve_output_path() is None
    os.environ["REPORT_OUTPUT"] = "/tmp/whatever.md"
    try:
        assert core.resolve_output_path() == Path("/tmp/whatever.md")
    finally:
        del os.environ["REPORT_OUTPUT"]


def test_fr5_main_writes_report_to_output_path_when_set():
    original_render = core.render_report
    core.render_report = lambda repo_root, collectors=None: "FAKE-REPORT\n"
    try:
        with tempfile.TemporaryDirectory() as tmp:
            out_path = Path(tmp) / "out.md"
            os.environ["REPORT_OUTPUT"] = str(out_path)
            try:
                core.main([])
            finally:
                del os.environ["REPORT_OUTPUT"]
            assert out_path.read_text(encoding="utf-8") == "FAKE-REPORT\n"
    finally:
        core.render_report = original_render


def run_all():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for t in tests:
        t()
        print(f"PASS {t.__name__}")
    print(f"\n{len(tests)}개 테스트 통과")


if __name__ == "__main__":
    run_all()
