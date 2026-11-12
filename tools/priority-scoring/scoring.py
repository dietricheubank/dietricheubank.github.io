"""Standard-library reference for the public weighted scoring model."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

DEFAULT_WEIGHTS = (30, 25, 20, 15, 10)
DEFAULT_THRESHOLDS = (4.5, 3.7, 2.7)


@dataclass(frozen=True)
class Result:
    score: float
    priority: str


def evaluate(
    ratings: Sequence[int],
    weights: Sequence[float] = DEFAULT_WEIGHTS,
    thresholds: Sequence[float] = DEFAULT_THRESHOLDS,
) -> Result:
    """Return weighted score and priority. No business-specific fields required."""
    if not ratings or len(ratings) != len(weights):
        raise ValueError("Provide one rating per criterion")
    if any(type(r) is not int or r < 1 or r > 5 for r in ratings):
        raise ValueError("Ratings must be integers between 1 and 5")
    if any(w < 0 or w > 100 for w in weights) or abs(sum(weights) - 100) > 1e-8:
        raise ValueError("Weights must be between 0 and 100 and sum to 100")
    if len(thresholds) != 3 or not (5 >= thresholds[0] > thresholds[1] > thresholds[2] >= 1):
        raise ValueError("Thresholds must descend from Critical to Medium within 1–5")
    score = sum(r * w for r, w in zip(ratings, weights)) / 100
    priority = ("Critical" if score >= thresholds[0] else
                "High" if score >= thresholds[1] else
                "Medium" if score >= thresholds[2] else "Low")
    return Result(round(score, 4), priority)


if __name__ == "__main__":
    sample = evaluate((5, 4, 3, 4, 2))
    print(f"Weighted score: {sample.score:.2f} | Priority: {sample.priority}")
