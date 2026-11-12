# Dietrich Eubank — Public Technology Portfolio

**[Portfolio website](https://dietricheubank.github.io/)** · [GitHub profile](https://github.com/dietricheubank)

A static, accessible-minded portfolio bringing together technology leadership, distributed AI engineering, public decision tools, case studies and educational demos.

## Website sections

| Area | Link | What is available |
|---|---|---|
| Home | [Portfolio](https://dietricheubank.github.io/) | Featured work and clear professional positioning |
| Engineering | [Forge case study](https://dietricheubank.github.io/case-studies/forge.html) | Public, generalized architecture and reliability lessons |
| Portfolio decisions | [Project Priority Studio 2.0](https://dietricheubank.github.io/tools/priority-scoring/v2.html) | Weighted scores, benefit-effort chart, dependency-aware capacity shortlist, CSV and printable report |
| AI operations | [Human approval demo](https://dietricheubank.github.io/demos/ai-ops/) | Synthetic incident workflow with approval gate and simulated audit |
| Leadership | [IT Leadership Playbook](https://dietricheubank.github.io/leadership/) | Five editable public Markdown templates |
| Writing | [Insights](https://dietricheubank.github.io/insights/) | Three short engineering and leadership articles |
| Biography | [About](https://dietricheubank.github.io/about/) | Professional background and principles |

## Repository map

- `index.html` — homepage
- `assets/` — architecture, demo and scorecard visuals, shared CSS
- `case-studies/` — public engineering writeups
- `demos/ai-ops/` — interactive fictional workflow
- `tools/priority-scoring/` — classic scorer, v2, Python reference and tests
- `leadership/templates/` — reusable governance worksheets
- `insights/` — public technical and leadership writing
- `tests/` — local link/asset validation
- `.github/workflows/` — GitHub Actions checks
- `robots.txt` and `sitemap.xml` — basic discoverability

## Run locally

Open `index.html` in a browser to preview the homepage. For correct root-relative navigation between subpages, serve the repository root locally:

```bash
python -m http.server 8000
```

Open `http://localhost:8000/`.

## Run checks

```bash
python -m unittest discover -s tests -v
cd tools/priority-scoring
python -m unittest -v test_scoring.py
```

GitHub Actions runs these validation checks for relevant changes.

## Accuracy and confidentiality

Scoring scenarios and incident events are **fictional**. Diagrams are **illustrative**, not live configuration exports. No real AI systems, employer environments, customer data, patient records, secret keys, or private network details are connected to these public demos.

The portfolio does not present unverified project outcome metrics. Site analytics and a public contact form have intentionally not been added to avoid unnecessary third-party data collection; GitHub provides a public contact path. A headshot, LinkedIn URL and PDF résumé require verified assets before publication.

## License

MIT License applies to original code and documentation in this repository, unless otherwise noted. Third-party trademarks remain the property of their respective owners.
