"""Exact small-portfolio optimizer (subset enumeration; fictional data)."""
from dataclasses import dataclass
from itertools import combinations

@dataclass(frozen=True)
class Project:
    code: str
    cost: int
    value: int
    dependencies: tuple[str, ...] = ()

def optimize(projects: list[Project], budget: int) -> tuple[list[str], int, int]:
    """Maximize total value, then prefer lower spend. Supports <= 20 projects."""
    if budget < 0 or len(projects) > 20:
        raise ValueError("budget must be nonnegative; max 20 projects")
    codes = [p.code for p in projects]
    if len(set(codes)) != len(codes) or any(not c for c in codes):
        raise ValueError("unique nonempty project codes required")
    if any(p.cost < 0 or p.value < 0 for p in projects):
        raise ValueError("costs and values must be nonnegative")
    if any(d not in codes or d == p.code for p in projects for d in p.dependencies):
        raise ValueError("invalid dependency")
    best = ([], 0, 0)
    for count in range(len(projects) + 1):
        for subset in combinations(projects, count):
            selected = {p.code for p in subset}
            if any(not set(p.dependencies).issubset(selected) for p in subset):
                continue
            cost = sum(p.cost for p in subset)
            if cost > budget:
                continue
            value = sum(p.value for p in subset)
            if (value, -cost) > (best[1], -best[2]):
                best = (sorted(selected), value, cost)
    return best

SAMPLE = [Project("A", 6, 10), Project("B", 5, 8),
          Project("C", 4, 9, ("A",)), Project("D", 3, 4)]

if __name__ == "__main__":
    codes, value, cost = optimize(SAMPLE, 10)
    print(f"Selected: {codes} | value={value} | cost={cost}")
