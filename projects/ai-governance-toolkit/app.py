"""AI use-case intake triage. Screening only; not a regulatory classification."""
from dataclasses import dataclass

@dataclass(frozen=True)
class UseCase:
    name: str
    sensitive_data: bool = False
    affects_people: bool = False
    external_actions: bool = False
    human_review: bool = True
    vendor_model: bool = False

def assess(case: UseCase) -> dict:
    if not case.name.strip():
        raise ValueError("name required")
    flags = []
    if case.sensitive_data:
        flags.append("Privacy and data protection review")
    if case.affects_people:
        flags.append("Impact and fairness review")
    if case.external_actions:
        flags.append("Action authorization and rollback review")
    if not case.human_review and (case.affects_people or case.external_actions):
        flags.append("Human oversight design review")
    if case.vendor_model:
        flags.append("Vendor and contractual review")
    return {"name": case.name,
            "review_required": bool(flags),
            "review_areas": flags,
            "next_step": "Obtain accountable review" if flags else "Proceed to standard intake review"}

if __name__ == "__main__":
    demo = UseCase("Fictional helpdesk summarizer", sensitive_data=True, vendor_model=True)
    print(assess(demo))
