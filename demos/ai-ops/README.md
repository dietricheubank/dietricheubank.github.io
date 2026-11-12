# Synthetic AI Operations Demo

A **deterministic, self-contained, browser-only** incident workflow that shows observations, a tentative diagnosis, explicit approval, a simulated remediation and a visible audit trail.

- All incident details are fictional
- No real LLM, credentials, APIs, or operations access
- No telemetry or user input is sent anywhere
- Approval is required before the *simulated* action
- Reset and rejection paths are included

Run by opening `index.html` locally or through the public site. This educational demo does not represent a hardened production incident-response system.

## Production considerations

A real implementation would need strong authentication and authorization, durable tamper-evident audit logs, safe scoped actions, idempotency, rate limits, approvals tied to identity, rollback checks, and observability. Incident hypotheses must remain distinguishable from evidence.
