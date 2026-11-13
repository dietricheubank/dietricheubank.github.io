# Modern Workplace Toolkit

Vendor-neutral endpoint lifecycle policy validation and evidence checklist generator.

## Run

Requires Python 3.11+ and no third-party dependencies.

```bash
cd projects/modern-workplace-toolkit
python app.py
python -m unittest discover -s tests -v
```

## Design / scope

This is an **independent starter project** staged under the public portfolio repository until a matching standalone GitHub repository can be created. The implementation is synthetic by default; no integrations with private systems, employer APIs, secrets, or confidential data.

Evidence checks are educational and must be adapted to approved policies, device classes, security requirements, and jurisdictional obligations.

## Next steps

- Extend coverage for invalid input and edge cases.
- Document real-world threat models, operational constraints, and test fixtures.
- Publish a dedicated repository without exposing private configurations.
- Add versioned sample data, user-facing CLI, and packaging when project grows.

License: MIT (parent repository).
