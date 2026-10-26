# ea-pm-toolkit
Small CLI that turns common Enterprise Architecture and PMO artifacts into version-controlled, reviewable files.

| Command | Output |
|---|---|
| `eapm adr` | Numbered Architecture Decision Record (markdown) |
| `eapm evm` | PMBOK Earned Value metrics: CPI, SPI, CV, SV, EAC, ETC, VAC, TCPI + RAG health |
| `eapm raid` | Risk-ranked RAID log table from CSV (probability × impact) |
| `eapm roadmap` | Mermaid Gantt for a phased transition roadmap (renders natively on GitHub) |

```bash
python -m eapm adr "Adopt event-driven integration" --context "Point-to-point APIs create coupling" \
  --decision "Use Kafka as the integration backbone" --consequences "Needs schema governance"
python -m eapm evm --bac 100000 --pv 50000 --ev 45000 --ac 50000
python -m eapm raid examples/raid.csv
python -m eapm roadmap examples/roadmap.json
pytest -q
```
