# Dietrich Eubank — Portfolio & Project Priority Studio

A responsive, static personal technology portfolio featuring an interactive project prioritization tool and public engineering documentation.

## Contents

- [Home page](index.html) — professional technology leadership and applied AI portfolio
- [Project Priority Studio](tools/priority-scoring/) — five-criterion weighted project ranking with adjustable weights, thresholds, and CSV export
- [Project methodology](tools/priority-scoring/MODEL.md) — scoring rules, limitations, and example
- [AI architecture illustration](assets/ai-architecture.svg) — illustrative public reference diagram
- [Scoring dashboard preview](assets/scoring-dashboard-preview.svg) — labeled fictional preview
- [Public project roadmap](PROJECT_ROADMAP.md) — planned work

## Local preview

Open `index.html` in a browser. No build system or dependencies required. The scoring model also works offline: open `tools/priority-scoring/index.html`.

## Tests

```bash
cd tools/priority-scoring
python -m unittest -v test_scoring.py
```

Automated tests run in GitHub Actions via `.github/workflows/scoring-tests.yml`.

## GitHub Pages

This repository is currently named `deubank-mws.github.io` under the account `dietricheubank`. To host the site as the clean account homepage at `https://dietricheubank.github.io/`, rename this repository to `dietricheubank.github.io` and verify **Settings → Pages** is publishing from the desired source. Until then, use the repository's Pages deployment link rather than assuming the root URL.

## Privacy and accuracy

The visuals show illustrative reference architecture and fictional project scoring data—not production screenshots or live organizational data. Public tools and examples are personal work and do not represent an employer.
