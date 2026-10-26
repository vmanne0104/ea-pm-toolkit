"""RAID log (Risks, Assumptions, Issues, Dependencies) with exposure scoring."""
import csv

def exposure(probability: int, impact: int) -> int:
    """1-5 scales -> exposure 1-25."""
    return probability * impact

def rating(score: int) -> str:
    return "HIGH" if score >= 15 else "MEDIUM" if score >= 8 else "LOW"

def load(path) -> list[dict]:
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        if r["type"].lower() == "risk":
            s = exposure(int(r["probability"]), int(r["impact"]))
            r["exposure"], r["rating"] = s, rating(s)
        else:
            r["exposure"], r["rating"] = "", ""
    return rows

def to_markdown(rows: list[dict]) -> str:
    risks = sorted((r for r in rows if r["type"].lower() == "risk"), key=lambda r: -r["exposure"])
    others = [r for r in rows if r["type"].lower() != "risk"]
    out = ["| ID | Type | Description | Owner | Exposure | Rating | Mitigation |", "|---|---|---|---|---|---|---|"]
    for r in risks + others:
        out.append(f"| {r['id']} | {r['type']} | {r['description']} | {r['owner']} | {r['exposure']} | {r['rating']} | {r['mitigation']} |")
    return "\n".join(out)
