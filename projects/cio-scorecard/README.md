# Cio Scorecard

Data-backed executive IT scorecards with thresholds, trend direction and text reports.

## Run

Requires Python 3.11+ and no third-party dependencies.

```bash
cd projects/cio-scorecard
python app.py
python -m unittest discover -s tests -v
```

## Design / scope

This is an **independent starter project** staged under the public portfolio repository until a matching standalone GitHub repository can be created. The implementation is synthetic by default; no integrations with private systems, employer APIs, secrets, or confidential data.

The KPI definitions and thresholds are synthetic. A real scorecard needs documented data lineage, trend baselines, and governance for metric ownership.

## Next steps

- Extend coverage for invalid input and edge cases.
- Document real-world threat models, operational constraints, and test fixtures.
- Publish a dedicated repository without exposing private configurations.
- Add versioned sample data, user-facing CLI, and packaging when project grows.

License: MIT (parent repository).
