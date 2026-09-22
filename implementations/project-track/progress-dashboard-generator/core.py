import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]

sys.path.insert(0, str(HERE))
from collectors.tracker import collect_tracker  # noqa: E402
from collectors.tests import collect_tests  # noqa: E402
from collectors.links import collect_links  # noqa: E402

# 마이크로커널 스타일: 이 리스트가 "플러그인 레지스트리"다. 새 수집기를 추가하려면
# collectors/에 파일 하나 추가하고 여기 한 줄만 더하면 된다 — render_report나
# main()은 손댈 필요 없다 (ADR-0003 참고).
COLLECTORS = [collect_tracker, collect_tests, collect_links]


def render_report(repo_root: Path, collectors=None) -> str:
    collectors = COLLECTORS if collectors is None else collectors
    lines = ["# 진행상황 대시보드", ""]
    for collector in collectors:
        section = collector(repo_root)
        lines.append(f"## {section['title']}")
        lines.extend(section["lines"])
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def resolve_output_path() -> Path | None:
    override = os.environ.get("REPORT_OUTPUT")
    return Path(override) if override else None


def main(argv) -> int:
    report = render_report(REPO_ROOT)
    output_path = resolve_output_path()
    if output_path:
        output_path.write_text(report, encoding="utf-8")
        print(f"저장됨: {output_path}")
    else:
        print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
