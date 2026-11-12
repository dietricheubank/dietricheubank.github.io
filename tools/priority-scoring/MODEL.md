# Weighted Project Prioritization Model

A **public, configurable demonstration** of a five-criterion weighted scorecard. The defaults use weights of **30%, 25%, 20%, 15%, 10%**. **The criterion names and thresholds are illustrative defaults, not an assertion about any organization's formal model.**

## How it works

Score each project from 1 to 5 for every criterion. Compute:

`weighted_score = sum(rating_i * weight_i) / 100`

For default weights of 30/25/20/15/10, a project with scores 5/4/3/4/2 receives:

`(5*30 + 4*25 + 3*20 + 4*15 + 2*10)/100 = 3.90`

Scores range from 1 to 5 with valid inputs. Results are sorted descending.

## Default priority bands (editable)

- Critical: 4.5–5.0
- High: 3.7–4.49
- Medium: 2.7–3.69
- Low: 1.0–2.69

Priority scores inform discussion; they **do not automatically approve funding or delivery**. Review feasibility, dependencies, compliance, and capacity separately. Positive scoring of resource efficiency means *more* efficient is better.

## Use

Open `index.html` in a modern browser, or visit the hosted version from the portfolio homepage. Adjust criteria, weights and thresholds; add projects; then export CSV. Data is processed in the browser and is not sent to a server. Refreshing the page resets values. This prototype intentionally does not store data.

## Security and scope

All included names and example initiatives are fictional. No employer-confidential data, personal records, or patient data is included. No backend, login, or remote telemetry is used.

## Next improvements

- Import CSV with validation and explicit field mapping
- Save/load a portable JSON model definition
- Add optional benefit vs. effort comparison and capacity constraints
- Add decision log and assessment date fields
