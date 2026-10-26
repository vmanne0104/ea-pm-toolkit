"""Architecture Decision Records (ADR) generator, numbered markdown files."""
from datetime import date
from pathlib import Path
import re

TEMPLATE = """# {num}. {title}

Date: {date}
Status: {status}

## Context
{context}

## Decision
{decision}

## Consequences
{consequences}
"""

def slug(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")

def next_number(folder: Path) -> int:
    nums = [int(p.name[:4]) for p in folder.glob("[0-9][0-9][0-9][0-9]-*.md")]
    return max(nums, default=0) + 1

def create_adr(folder, title, context, decision, consequences, status="Proposed") -> Path:
    folder = Path(folder); folder.mkdir(parents=True, exist_ok=True)
    n = next_number(folder)
    path = folder / f"{n:04d}-{slug(title)}.md"
    path.write_text(TEMPLATE.format(num=n, title=title, date=date.today().isoformat(),
                    status=status, context=context, decision=decision, consequences=consequences))
    return path
