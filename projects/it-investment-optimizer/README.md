# It Investment Optimizer

Exact budget-constrained project selection with dependencies using exhaustive search for small candidate sets.

## Run

Requires Python 3.11+ and no third-party dependencies.

```bash
cd projects/it-investment-optimizer
python app.py
python -m unittest discover -s tests -v
```

## Design / scope

This is an **independent starter project** staged under the public portfolio repository until a matching standalone GitHub repository can be created. The implementation is synthetic by default; no integrations with private systems, employer APIs, secrets, or confidential data.

An exact exponential search is intentional for <=20 projects; it is not appropriate for large portfolios. Values are arbitrary utility points, not guaranteed ROI.

## Next steps

- Extend coverage for invalid input and edge cases.
- Document real-world threat models, operational constraints, and test fixtures.
- Publish a dedicated repository without exposing private configurations.
- Add versioned sample data, user-facing CLI, and packaging when project grows.

License: MIT (parent repository).
