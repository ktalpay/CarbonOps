# Measurement Boundaries

## Why Measurement Boundaries Matter

Carbon-aware engineering can be useful only when its assumptions are clear. A repository that mentions CO2e, carbon intensity, or scheduling windows should explain what is measured, what is estimated, and what is outside scope.

## Current State

CarbonOps does not yet include a real carbon-intensity adapter. The current CLI has a placeholder schedule command for pre-alpha behavior.

CarbonOps should not be used to claim verified emissions reduction in its current state.

## What Future CO2e Reporting Would Require

Future reporting examples would need:

- Documented data sources.
- Region and time-window assumptions.
- Calculation method.
- Treatment of missing or stale data.
- Scope of the reported workflow.
- Clear distinction between estimate, recommendation, and measured outcome.

## What Not To Claim

Do not claim:

- Public adoption.
- Production usage.
- Commercial impact.
- Verified emissions reduction.
- External recognition.
- Real carbon reduction.
- Employer or customer impact.

## Data Source Assumptions To Document Later

Future adapter work should document:

- Data provider.
- Region coverage.
- Update frequency.
- Units.
- Licensing constraints.
- Known reliability limits.

## Methodology Assumptions To Document Later

Future methodology notes should document:

- Whether values are estimates or measured outputs.
- How build duration is handled.
- How CI/CD job boundaries are defined.
- How recommendations are generated.
- What a human reviewer should verify before acting on any recommendation.
