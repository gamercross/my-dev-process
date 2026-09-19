#!/usr/bin/env python3
"""
카탈로그 검색 CLI. ADR-0002(Layered)에 따라 3계층으로 나눈다:
입력 파싱(main) -> 검색(search) -> 출력(print). 요구사항은 2단계 EARS 명세
(FR1~FR4) 그대로.

사용법:
    python3 catalog_search.py <키워드>
    CATALOG_ROOT=/다른/저장소/경로 python3 catalog_search.py <키워드>   # FR4
"""
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]  # implementations/project-track/catalog-search-cli -> repo root
DEFAULT_CATALOG_DIR = REPO_ROOT / "docs" / "catalog"
STANDARD_CATALOG_HINT = (
    "docs/03-pattern-analysis/ (알고리즘: 01-algorithm-paradigms.md, "
    "프로젝트: 02-architecture-styles.md)"
)


def resolve_catalog_dir() -> Path:
    """FR4: CATALOG_ROOT 환경변수가 있으면 그 경로 아래 catalog/를 쓴다."""
    override = os.environ.get("CATALOG_ROOT")
    if override:
        return Path(override) / "catalog"
    return DEFAULT_CATALOG_DIR


def search(keyword: str, catalog_dir: Path | None = None) -> str:
    """FR1/FR2/FR3: 대소문자 구분 없이 patterns.md·checklist.md에서 keyword를 찾고,
    없으면 표준 카탈로그를 안내한다."""
    catalog_dir = catalog_dir or resolve_catalog_dir()
    needle = keyword.lower()

    hits = []
    for name in ("patterns.md", "checklist.md"):
        text = (catalog_dir / name).read_text(encoding="utf-8")
        if needle in text.lower():
            hits.append(f"[{name}] '{keyword}' 포함됨")

    if hits:
        return "\n".join(hits)
    return f"일치 항목 없음. 표준 카탈로그를 참고하세요: {STANDARD_CATALOG_HINT}"


def main(argv: list[str]) -> int:
    keyword = argv[1] if len(argv) > 1 else ""
    print(search(keyword))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
