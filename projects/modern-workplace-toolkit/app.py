"""Generalized endpoint lifecycle acceptance and policy validation."""
from dataclasses import dataclass

STAGES = ("request", "provision", "secure", "operate", "retire")
REQUIRED = {
    "request": {"business_owner", "approved"},
    "provision": {"asset_tag", "enrollment_verified"},
    "secure": {"encryption", "patch_policy"},
    "operate": {"support_owner", "monitoring"},
    "retire": {"data_wipe_evidence", "inventory_updated"},
}

@dataclass(frozen=True)
class Review:
    stage: str
    passed: bool
    missing: tuple[str, ...]

def validate(stage: str, evidence: dict[str, bool]) -> Review:
    if stage not in STAGES:
        raise ValueError("unsupported lifecycle stage")
    missing = tuple(sorted(k for k in REQUIRED[stage] if evidence.get(k) is not True))
    return Review(stage, not missing, missing)

def report(records: dict[str, dict[str, bool]]) -> str:
    result = []
    for stage in STAGES:
        r = validate(stage, records.get(stage, {}))
        result.append(f"{stage}: {'PASS' if r.passed else 'GAPS ' + ', '.join(r.missing)}")
    return "\n".join(result)

if __name__ == "__main__":
    print(report({"request": {"business_owner": True, "approved": True}}))
