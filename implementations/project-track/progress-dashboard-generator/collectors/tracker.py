from pathlib import Path

TABLE_HEADER_MARKER = "| 문제/프로젝트 |"


def parse_tracker_table(text: str) -> list[dict]:
    """sessions/README.md의 트래커 마크다운 표를 행 딕셔너리 목록으로 파싱한다."""
    rows = []
    in_table = False
    for line in text.splitlines():
        if line.startswith(TABLE_HEADER_MARKER):
            in_table = True
            continue
        if not in_table:
            continue
        if line.startswith("|---"):
            continue
        if not line.startswith("|"):
            break
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6:
            continue
        rows.append(
            {
                "name": cells[0],
                "track": cells[1],
                "tier": cells[2],
                "pattern": cells[3],
                "gate": cells[4],
                "tests": cells[5],
            }
        )
    return rows


def summarize_rows(rows: list[dict]) -> dict:
    by_track: dict[str, int] = {}
    by_tier: dict[str, int] = {}
    completed = 0
    total_tests = 0
    for row in rows:
        by_track[row["track"]] = by_track.get(row["track"], 0) + 1
        by_tier[row["tier"]] = by_tier.get(row["tier"], 0) + 1
        if "완주" in row["gate"]:
            completed += 1
        digits = "".join(ch for ch in row["tests"].split("개")[0] if ch.isdigit())
        if digits:
            total_tests += int(digits)
    return {
        "total": len(rows),
        "completed": completed,
        "by_track": by_track,
        "by_tier": by_tier,
        "total_tests": total_tests,
    }


def collect_tracker(repo_root: Path) -> dict:
    path = repo_root / "docs" / "01-problem-save" / "sessions" / "README.md"
    text = path.read_text(encoding="utf-8")
    rows = parse_tracker_table(text)
    summary = summarize_rows(rows)

    lines = [
        f"- 전체 항목: {summary['total']}개 (1→7 완주: {summary['completed']}개)",
        "- 트랙별: "
        + ", ".join(f"{k} {v}개" for k, v in sorted(summary["by_track"].items())),
        "- 등급별: "
        + ", ".join(f"{k} {v}개" for k, v in sorted(summary["by_tier"].items())),
        f"- 트래커에 기록된 테스트 개수 합계: {summary['total_tests']}개",
    ]
    return {"title": "트래커 요약", "lines": lines}
