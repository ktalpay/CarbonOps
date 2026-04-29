# Examples

CarbonOps examples are synthetic and public-safe. They demonstrate the current CLI shape and documentation boundaries only.

The current examples do not use real carbon-intensity data. They do not prove verified emissions reduction, production usage, commercial impact, external recognition, or operational maturity.

## Current Example: Placeholder Schedule Output

The current CLI includes a placeholder `schedule` command. It shows the intended command shape for a future scheduling experiment, but it does not make a real carbon-aware scheduling decision.

## How To Run

```bash
carbonops schedule --region gb_london --duration 30m --mode delay
```

## Expected Output

The timestamp will vary. The output should include the selected region, duration, mode, and placeholder wording.

Example:

```text
[2026-04-29T18:30] region=gb_london duration=30m mode=delay
Decision: delay 15m (placeholder, add real adapters in v0.0.2)
```

## What This Example Demonstrates

- CLI command shape.
- Placeholder schedule response.
- Public-safe example parameters.
- Current pre-alpha boundaries.

## What This Example Does Not Demonstrate

- Real carbon-intensity data lookup.
- Real scheduling logic.
- Verified emissions reduction.
- Production usage.
- Commercial impact.
- External recognition.
- Employer or customer impact.

## Future Demo Ideas

Future demos may use synthetic pipeline metadata, documented data-source assumptions, and a small example report. Any future demo should clearly separate estimates, recommendations, and validated results.
