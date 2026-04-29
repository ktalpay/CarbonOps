# ADR-0001: Carbon-Aware Delivery Scope

## Status

Proposed

## Context

CarbonOps is a pre-alpha reference toolkit for exploring carbon-aware delivery concepts. The current repository contains documentation, a Python package skeleton, a Typer-based CLI, a `version` command, a placeholder `schedule` command, and basic CLI tests.

The project does not currently include real carbon-intensity adapters, real scheduling logic, or a validated methodology for carbon or CO2e reporting.

## Decision

CarbonOps will keep its current scope conservative. The near-term scope is:

- Public-safe documentation.
- CLI skeleton.
- Placeholder scheduling behavior.
- Measurement-boundary documentation.
- Future ADRs and examples that separate implemented behavior from planned behavior.

CarbonOps should not be described as proving verified emissions reduction, production usage, commercial impact, public adoption, or external recognition.

## Consequences

- The repository can be reviewed as an early technical artifact without implying maturity it does not have.
- Carbon-aware language must stay tied to documented assumptions and current implementation limits.
- Future features should remain clearly marked as planned until implemented and tested.

## Alternatives Considered

- Present CarbonOps as a production-ready carbon-aware CI/CD platform. Rejected because the current implementation is pre-alpha and placeholder-based.
- Avoid carbon-aware language entirely. Rejected because the repository purpose is to explore that domain, as long as the limitations are explicit.
