# Architecture Overview

## Purpose

CarbonOps is a pre-alpha reference toolkit for exploring carbon-aware DevOps and CI/CD concepts. The repository is intended to document how delivery workflows could be measured, governed, and improved with sustainability-aware engineering practices.

It is not a production platform.

## Current Implemented Shape

The current implementation is intentionally small:

- Python package skeleton.
- Typer-based CLI.
- `version` command.
- Placeholder `schedule` command.
- Basic CLI tests for current pre-alpha behavior.

The placeholder scheduler does not use real carbon-intensity data and does not make verified scheduling decisions.

## Planned Conceptual Architecture

Future work may explore this conceptual shape:

```text
CLI or workflow input
  -> carbon-intensity adapter
  -> measurement and policy boundary
  -> scheduling recommendation or report
  -> human review
```

This is a planned architecture direction, not the current implementation.

## Current Request / CLI Flow

Current flow:

```text
carbonops version
  -> prints package version

carbonops schedule --region <region> --duration <duration> --mode <mode>
  -> prints placeholder schedule output
```

The `schedule` command currently demonstrates CLI shape only.

## What Is Not Implemented Yet

CarbonOps does not yet include:

- Real carbon-intensity data adapters.
- Real scheduling logic.
- CO2e reporting methodology.
- CI/CD integration that is committed as active project evidence.
- Architecture decision records.
- Demo workflow or example output with documented assumptions.

## Public-Safety Boundaries

Public CarbonOps content should avoid:

- Private systems.
- Customer data.
- Credentials or secrets.
- Internal endpoints.
- Employer-specific implementation details.
- Claims of adoption, production usage, commercial impact, verified emissions reduction, or external recognition.
