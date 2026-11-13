# Six Standalone-Ready Project Starters

These projects are isolated in subfolders temporarily because repository creation is unavailable through the connected GitHub integration.

| Project | Purpose |
|---|---|
| [enterprise-agent-framework](./enterprise-agent-framework/) | Allowlisted mock tools, approval gates, structured audit log |
| [cio-scorecard](./cio-scorecard/) | Executive reliability and delivery KPI report generator |
| [it-investment-optimizer](./it-investment-optimizer/) | Exact budget optimizer with dependency-aware subsets (≤20 projects) |
| [llm-observability-stack](./llm-observability-stack/) | Synthetic Prometheus-format LLM request telemetry endpoint |
| [modern-workplace-toolkit](./modern-workplace-toolkit/) | Endpoint onboarding, security, operations and retirement evidence validator |
| [ai-governance-toolkit](./ai-governance-toolkit/) | AI risk and review-area intake screening for fictional use cases |

Run all tests locally:

```bash
for project in projects/*/; do
  [ -e "$project/app.py" ] || continue
  (cd "$project" && python -m unittest discover -s tests -v)
done
```

The GitHub Actions workflow `.github/workflows/project-starters.yml` runs each package independently on Python 3.12.

To promote each to its own repository, create a new public repo and copy the respective folder contents (or use Git subtree split to preserve directory history). Do not accidentally include sensitive files.
