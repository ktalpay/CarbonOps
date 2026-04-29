# Roadmap

CarbonOps is pre-alpha. Roadmap items describe planned hardening work and should not be read as adoption, production usage, commercial impact, verified emissions reduction, or external recognition.

## Stage 1: Repository Hygiene And README Reframing

Status: completed for the current hardening pass.

Completed:

- Added repository hygiene `.gitignore`.
- Replaced placeholder-only tests with basic CLI tests.
- Reframed README for pre-alpha scope.

## Stage 2: Documentation Baseline

Status: completed for the current baseline.

Completed:

- Architecture overview.
- Measurement boundaries.
- Security and confidentiality note.
- Roadmap.
- Repository status.

## Stage 3: ADR Baseline

Status: completed for the current baseline.

Completed:

- Carbon-aware delivery scope ADR.
- CI/CD measurement boundaries ADR.
- Toolkit versus production platform ADR.

## Stage 4: Demo Or Example Workflow

Status: planned.

Planned:

- Safe demo scenario.
- Placeholder or synthetic input.
- Example output with documented limitations.

## Stage 5: CI Decision

Status: completed for the current baseline.

Completed:

- Added a minimal test-only GitHub Actions workflow.
- The workflow installs the package and runs `python -m pytest -q`.
- CI should not be presented as production-readiness evidence.

## Stage 6: Screenshot / Evidence Readiness

Status: planned.

Planned:

- Capture screenshots only after README, docs, ADRs, and CI decisions are reviewed.
- Reassess pin readiness after hardening.
- Keep evidence claims conservative.
