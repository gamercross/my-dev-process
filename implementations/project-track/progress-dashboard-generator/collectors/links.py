import re
from pathlib import Path

LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def find_broken_links(root: Path) -> dict:
    broken = []
    checked = 0
    for md in root.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for m in LINK_PATTERN.finditer(text):
            link = m.group(1)
            if link.startswith("http") or link.startswith("#"):
                continue
            target = link.split("#")[0]
            if not target:
                continue
            checked += 1
            target_path = (md.parent / target).resolve()
            if not target_path.exists():
                broken.append(f"{md.relative_to(root)}: {link}")
    return {"checked": checked, "broken": broken}


def collect_links(repo_root: Path) -> dict:
    result = find_broken_links(repo_root)
    lines = [
        f"- 검사한 상대 링크: {result['checked']}개",
        f"- 깨진 링크: {len(result['broken'])}개",
    ]
    lines.extend(f"  - {b}" for b in result["broken"])
    return {"title": "링크 무결성", "lines": lines}
