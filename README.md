[![CI](https://github.com/ktalpay/CarbonOps/actions/workflows/ci.yml/badge.svg)](https://github.com/ktalpay/CarbonOps/actions/workflows/ci.yml)


# CarbonOps

CarbonOps is an open‑source, carbon‑aware DevOps toolkit. It lets you:
- collect & normalise grid carbon‑intensity data,
- schedule CI/CD & batch workloads in lower‑carbon windows,
- report grams CO₂e per build/release at repo level.

> Status: **pre‑alpha (v0.0.1)** — API may change.

## Quickstart

```bash
git clone https://github.com/ktalpay/CarbonOps.git
cd CarbonOps
pip install -e .
carbonops version
```

## Features (v0.1 target)
- Python CLI (`typer`) and minimal SDK.
- Region adapters for `GB` (National Grid), `EU`, and generic custom CSV.
- Policy engine: `delay | relocate | run-now` with thresholds.
- GitHub Action to annotate PRs with CO₂e per build.
- Metrics export: JSON and OpenMetrics format.

## Roadmap
- [ ] v0.0.1 repo bootstrap (this commit)
- [ ] v0.0.2 carbon-intensity adapters + simple scheduler
- [ ] v0.0.3 GitHub Action + per-repo CO₂e report
- [ ] v0.1.0 first pilot + docs site

## Contributing
Issues and PRs are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License
MIT — see [`LICENSE`](LICENSE).
