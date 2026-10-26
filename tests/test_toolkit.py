from eapm.evm import EVM
from eapm import adr, raid, roadmap
from eapm.cli import main

def test_evm_amber_and_values():
    m = EVM(bac=100000, pv=50000, ev=45000, ac=50000)
    assert round(m.cpi, 2) == 0.9 and round(m.spi, 2) == 0.9
    assert m.cv == -5000 and m.sv == -5000
    assert round(m.eac) == 111111 and m.health() == "AMBER"

def test_evm_green_red():
    assert EVM(100, 50, 55, 50).health() == "GREEN"
    assert EVM(100, 50, 30, 50).health() == "RED"

def test_adr_numbering(tmp_path):
    p1 = adr.create_adr(tmp_path, "Use Kafka for events", "c", "d", "q")
    p2 = adr.create_adr(tmp_path, "Adopt Zero Trust", "c", "d", "q")
    assert p1.name.startswith("0001-use-kafka") and p2.name.startswith("0002-adopt-zero-trust")

def test_raid_sorting():
    rows = raid.load("examples/raid.csv")
    md = raid.to_markdown(rows)
    assert md.index("R1") < md.index("R2") and "HIGH" in md

def test_roadmap():
    out = roadmap.from_file("examples/roadmap.json")
    assert out.startswith("gantt") and "section Migrate" in out

def test_cli_evm(capsys):
    main(["evm", "--bac", "100", "--pv", "50", "--ev", "50", "--ac", "50"])
    assert '"health": "GREEN"' in capsys.readouterr().out
