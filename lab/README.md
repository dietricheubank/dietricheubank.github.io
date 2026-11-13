# Technology Leadership Lab — design notes

The lab is a static, browser-only, fictional technology-investment exercise.

## Learning goals
- Connect enterprise strategy, delivery, service operations and continuous improvement.
- Explain budget tradeoffs and unselected alternatives.
- Illustrate that a calculated score is not an approved investment decision.
- Link investment choices to reusable project and service practices.

## Model assumptions
- Initiative cost and value points are synthetic integers, not dollars or ROI.
- The residual risk index is an illustrative sum of risk-reduction points capped at zero.
- Users manually select initiatives, subject to a budget guardrail. The lab does **not** optimize a portfolio.
- No real service levels or organizational results are shown.
- No persistence, APIs, external data transfer or analytics.

## Architecture
- `index.html`: accessible HTML structure and responsive presentation
- `lab.js`: deterministic state, selection controls, scenario reporting
- `assets/operating-model.svg` and `assets/modern-workplace-reference.svg`: original explanatory reference architecture diagrams

## Verification
A Python standard-library static test checks that all source files and project references exist. End-to-end UI accessibility review remains a separate task.

## Next iterations
Add multiple fictional organizational scenarios; deliverable/capacity dependencies; scenarios comparing alternative plans; historical scorecard examples and documented manual QA.
