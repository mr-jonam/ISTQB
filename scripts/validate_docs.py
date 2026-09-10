"""Validate local Markdown links and unfinished editorial markers."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MARKER = re.compile(r"\b(?:TODO|TBD|FIXME)\b", re.IGNORECASE)
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")

    for number, line in enumerate(text.splitlines(), start=1):
        if MARKER.search(line):
            errors.append(f"{path.relative_to(ROOT)}:{number}: marker incompleto")

    for match in LINK.finditer(text):
        raw_target = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
        if not raw_target or raw_target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target_without_anchor = unquote(raw_target.split("#", 1)[0])
        if not target_without_anchor:
            continue
        resolved = (path.parent / target_without_anchor).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: link non trovato: {raw_target}")

    return errors


def main() -> int:
    errors: list[str] = []
    markdown_files = [ROOT / "README.md", ROOT / "CONTRIBUTING.md"]
    markdown_files.extend(sorted(DOCS.rglob("*.md")))

    for markdown_file in markdown_files:
        errors.extend(validate_file(markdown_file))

    if errors:
        print("Documentazione non valida:")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print(f"OK: {len(markdown_files)} file Markdown validati")
    return 0


if __name__ == "__main__":
    sys.exit(main())

