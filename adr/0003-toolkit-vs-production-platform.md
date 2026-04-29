# ADR-0003: Toolkit vs Production Platform

## Status

Proposed

## Context

CarbonOps is currently a pre-alpha artifact with a small CLI skeleton and documentation baseline. It is intended to explore architecture and engineering practices for carbon-aware delivery.

Public documentation needs to distinguish a reference toolkit from a production platform so reviewers do not infer adoption, production usage, commercial impact, verified emissions reduction, or external recognition.

## Decision

CarbonOps will be described as a reference toolkit and pre-alpha public artifact, not as a production platform.

Future production-readiness would require:

- Real carbon-intensity adapters.
- Meaningful automated tests.
- Reviewed CI.
- Security review.
- Methodology documentation.
- Reproducible examples.
- Clear release and maintenance policy.

## Consequences

- README and docs should keep implementation status visible.
- Planned features should not be described as current capabilities.
- Pin or evidence decisions should wait for further hardening and review.

## Alternatives Considered

- Describe CarbonOps as production-oriented now. Rejected because the implementation and evidence are not mature enough.
- Avoid public positioning until the project is complete. Rejected because conservative public documentation can still make the project easier to inspect while preserving accurate scope.
