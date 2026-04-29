# CarbonOps

CarbonOps is a pre-alpha carbon-aware DevOps / CI/CD reference toolkit. It is intended to explore how delivery workflows can be documented, measured, and governed with sustainability-aware engineering practices.

CarbonOps is not a production platform. At this stage, it should be read as an early public technical artifact with a small Python CLI skeleton and placeholder scheduling behavior.

> Status: **pre-alpha (v0.0.1)**. APIs, commands, and repository structure may change.

## Current Implementation

CarbonOps currently provides:

- Python package skeleton.
- Typer-based CLI.
- `version` command.
- Placeholder `schedule` command for pre-alpha CLI behavior.
- Basic CLI tests for version output and placeholder schedule output.

The placeholder scheduler does not use real carbon-intensity adapters and does not make verified scheduling decisions.

## Planned Capabilities

CarbonOps aims to demonstrate the following areas over time:

- Carbon-intensity data adapters.
- CI/CD scheduling policy experiments.
- Reporting examples.
- Measurement-boundary documentation.
- ADRs and architecture docs.

These items are planned unless they are explicitly listed in the current implementation section.

## Measurement Boundaries

Any CO2e or carbon-intensity language in this repository is exploratory unless backed by real adapters, reproducible examples, and documented methodology.

This repository should not be used to claim verified emissions reduction. Measurement assumptions, limitations, and data-source boundaries will be documented later as the implementation matures.

## What This Repository Does Not Prove

This repository does not prove:

- Public adoption.
- Production usage.
- Commercial impact.
- Verified emissions reduction.
- External recognition.
- Employer or customer impact.

## Repository Status

Pre-alpha. Under active hardening.

The current goal is to make the repository easier to review, safer to read publicly, and clearer about what is implemented versus planned.

## Repository Map

- `src/carbonops/` — Python package and CLI entry points.
- `tests/` — basic CLI tests.
- `README.md` — repository overview and current scope.
- `LICENSE` — project license.
- `CONTRIBUTING.md` — contribution guidance.
- `CODE_OF_CONDUCT.md` — community conduct note.
- `SECURITY.md` — security policy.

Planned documentation and ADR folders will be added in later hardening work.

## Quickstart

```bash
git clone https://github.com/ktalpay/CarbonOps.git
cd CarbonOps
pip install -e .
carbonops version
```

## Roadmap

- [x] v0.0.1 repository bootstrap.
- [x] Basic CLI version and placeholder schedule tests.
- [ ] README reframing for pre-alpha scope.
- [ ] Carbon-intensity adapter exploration.
- [ ] Simple scheduling-policy experiment.
- [ ] Reporting example with documented measurement boundaries.
- [ ] First demo scenario.
- [ ] Architecture docs and ADRs.

## Contributing

Issues and PRs are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

MIT. See [`LICENSE`](LICENSE).
