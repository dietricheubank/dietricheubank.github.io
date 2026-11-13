# Llm Observability Stack

A minimal Prometheus-compatible metrics endpoint and simple latency/error-rate aggregator.

## Run

Requires Python 3.11+ and no third-party dependencies.

```bash
cd projects/llm-observability-stack
python app.py
python -m unittest discover -s tests -v
```

## Design / scope

This is an **independent starter project** staged under the public portfolio repository until a matching standalone GitHub repository can be created. The implementation is synthetic by default; no integrations with private systems, employer APIs, secrets, or confidential data.

The metrics are synthetic, bind only to loopback, and expose no GPU or runtime-specific instrumentation yet. For production, use appropriate authentication/network controls and OpenTelemetry semantic conventions.

## Next steps

- Extend coverage for invalid input and edge cases.
- Document real-world threat models, operational constraints, and test fixtures.
- Publish a dedicated repository without exposing private configurations.
- Add versioned sample data, user-facing CLI, and packaging when project grows.

License: MIT (parent repository).
