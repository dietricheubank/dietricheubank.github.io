"""Executive service KPI scorecard. All metrics synthetic."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Metric:
    name: str
    actual: float
    target: float
    direction: str = "up"  # up or down
    unit: str = ""

    def __post_init__(self):
        if self.direction not in ("up", "down"):
            raise ValueError("direction must be up or down")

    @property
    def on_target(self) -> bool:
        return self.actual >= self.target if self.direction == "up" else self.actual <= self.target

def summarize(metrics: list[Metric]) -> dict:
    if not metrics:
        raise ValueError("at least one metric required")
    return {"total": len(metrics),
            "on_target": sum(m.on_target for m in metrics),
            "at_risk": [m.name for m in metrics if not m.on_target]}

def render(metrics: list[Metric]) -> str:
    info = summarize(metrics)
    lines = [f"CIO SCORECARD — {info['on_target']}/{info['total']} on target"]
    for m in metrics:
        status = "ON TARGET" if m.on_target else "AT RISK"
        lines.append(f"{m.name}: {m.actual}{m.unit} / {m.target}{m.unit} [{status}]")
    return "\n".join(lines)

SAMPLE = [
    Metric("Service availability", 99.91, 99.9, unit="%"),
    Metric("Median restoration", 3.2, 2.0, direction="down", unit="h"),
    Metric("Milestones delivered", 87, 90, unit="%"),
]

if __name__ == "__main__":
    print(render(SAMPLE))
