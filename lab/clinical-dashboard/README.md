# Clinical Modernization Executive Dashboard

This example uses entirely fictional data and simplified readiness rules. It is **not a real healthcare IT project status report**.

## Capabilities
- Edit migration volume, completed devices, weekly capacity and remaining duration
- Track workflow validation, blocking issues and fictional device-health evidence
- See a simplified hold/review recommendation and printable executive narrative
- Link to the detailed migration wave planning simulator

## Model
- Percent migrated = completed / total
- Remaining work = total − completed
- Remaining weeks = ceiling(remaining / modeled weekly capacity)
- A review-ready scenario requires zero blockers, at least 95% workflow validation and 98% health

These heuristic thresholds are invented and must not be used to approve clinical change or device deployments.
