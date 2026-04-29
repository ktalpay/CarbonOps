# ADR-0002: CI/CD Measurement Boundaries

## Status

Proposed

## Context

CarbonOps may later explore carbon-aware CI/CD measurement and scheduling recommendations. CI/CD measurement boundaries matter because ambiguous data can lead to unsupported claims about carbon impact.

The current project has no real carbon-intensity adapter yet.

## Decision

Future measurement work must define, at minimum:

- Region.
- Time window.
- Data source.
- Job duration.
- Calculation method.
- Stale or missing data behavior.
- Whether the output is an estimate, demonstration, or validated result.

Current outputs should be treated as placeholder demonstrations unless a future implementation documents and validates the methodology.

## Consequences

- Future examples will need explicit assumptions before they can be used as evidence.
- CarbonOps should not claim verified emissions reduction in its current state.
- Reports or recommendations should be labeled carefully so they are not confused with measured production outcomes.

## Alternatives Considered

- Report CO2e values without documented assumptions. Rejected because it would create a greenwashing and evidence-safety risk.
- Delay all measurement documentation until adapters exist. Rejected because boundaries should guide implementation rather than be added after claims appear.
