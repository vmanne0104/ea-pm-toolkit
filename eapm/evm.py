"""Earned Value Management: PMBOK metrics."""
from dataclasses import dataclass

INF = float("inf")

@dataclass
class EVM:
    bac: float  # Budget at completion
    pv: float   # Planned value
    ev: float   # Earned value
    ac: float   # Actual cost

    @property
    def cpi(self): return self.ev / self.ac if self.ac else INF
    @property
    def spi(self): return self.ev / self.pv if self.pv else INF
    @property
    def cv(self): return self.ev - self.ac
    @property
    def sv(self): return self.ev - self.pv
    @property
    def eac(self): return self.bac / self.cpi if self.cpi not in (0, INF) else INF
    @property
    def etc(self): return self.eac - self.ac
    @property
    def vac(self): return self.bac - self.eac
    @property
    def tcpi(self):
        rem = self.bac - self.ac
        return (self.bac - self.ev) / rem if rem else INF

    def health(self) -> str:
        if self.cpi >= 1 and self.spi >= 1: return "GREEN"
        if self.cpi >= 0.9 and self.spi >= 0.9: return "AMBER"
        return "RED"

    def report(self) -> dict:
        r = lambda x: round(x, 3) if x != INF else x
        out = {k: r(getattr(self, k)) for k in ("cpi", "spi", "cv", "sv", "eac", "etc", "vac", "tcpi")}
        out["health"] = self.health()
        return out
