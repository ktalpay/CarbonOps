# Architecture Note

CarbonOps is pre-alpha. The current implementation is a small Python package and Typer CLI with a version command and placeholder schedule command.

For the reviewed architecture baseline, see:

- `docs/architecture-overview.md`
- `docs/measurement-boundaries.md`
- `adr/0001-carbon-aware-delivery-scope.md`
- `adr/0002-ci-cd-measurement-boundaries.md`
- `adr/0003-toolkit-vs-production-platform.md`

This repository does not currently implement real carbon-intensity adapters, real scheduling logic, REST API behavior, Docker packaging, Hugging Face datasets, or methodology-backed CO2e reporting.
