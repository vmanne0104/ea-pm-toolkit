"""Render a phased architecture transition roadmap as a Mermaid Gantt chart."""
import json

def to_mermaid(data: dict) -> str:
    lines = ["gantt", f"    title {data['title']}", "    dateFormat YYYY-MM-DD"]
    for phase in data["phases"]:
        lines.append(f"    section {phase['name']}")
        for t in phase["tasks"]:
            status = f"{t['status']}, " if t.get("status") else ""
            lines.append(f"    {t['name']} :{status}{t['id']}, {t['start']}, {t['duration']}")
    return "\n".join(lines)

def from_file(path) -> str:
    with open(path) as f:
        return to_mermaid(json.load(f))
