# Unified Communications Migration Simulator

Original public educational simulation of enterprise telephony migration planning. It does not represent a real organization, user inventory, calling architecture, Microsoft Teams configuration or port order.

## Capabilities
- Plan user counts, cutover waves and number/license readiness
- Model five conceptual prerequisites (routing, emergency calling, pilot, communications, rollback)
- Evaluate synthetic calling tests and service desk preparedness
- Produce a printable go/hold decision summary

## Limitations
- No Microsoft Graph or carrier integrations
- No actual number portability, call routing, or emergency service validation
- Number/license readiness is reported as a possible range: minimum overlap = max(0, number-ready + licensed − total), maximum overlap = min(number-ready, licensed). Percentages are treated as exact for this illustrative estimate; actual user-level overlap requires a joined inventory.
- The recommended go/hold labels are fictional guidance, not deployment authorization
