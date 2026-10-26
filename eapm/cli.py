import argparse, json
from . import adr, evm, raid, roadmap

def main(argv=None):
    p = argparse.ArgumentParser(prog="eapm", description="Enterprise Architecture + PMO toolkit")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("adr", help="create an Architecture Decision Record")
    a.add_argument("title"); a.add_argument("--dir", default="docs/adr")
    a.add_argument("--context", required=True); a.add_argument("--decision", required=True)
    a.add_argument("--consequences", required=True); a.add_argument("--status", default="Proposed")

    e = sub.add_parser("evm", help="Earned Value metrics")
    for k in ("bac", "pv", "ev", "ac"):
        e.add_argument(f"--{k}", type=float, required=True)

    r = sub.add_parser("raid", help="RAID CSV -> markdown"); r.add_argument("csv")
    g = sub.add_parser("roadmap", help="roadmap JSON -> Mermaid gantt"); g.add_argument("json")

    args = p.parse_args(argv)
    if args.cmd == "adr":
        print(adr.create_adr(args.dir, args.title, args.context, args.decision, args.consequences, args.status))
    elif args.cmd == "evm":
        print(json.dumps(evm.EVM(args.bac, args.pv, args.ev, args.ac).report(), indent=2))
    elif args.cmd == "raid":
        print(raid.to_markdown(raid.load(args.csv)))
    elif args.cmd == "roadmap":
        print(roadmap.from_file(args.json))

if __name__ == "__main__":
    main()
