# Sample Output

These examples show current pre-alpha CLI behavior. They use placeholder behavior and should not be read as real carbon-aware scheduling.

## Version Command

Command:

```bash
carbonops version
```

Sample output:

```text
0.0.1
```

## Placeholder Schedule Command

Command:

```bash
carbonops schedule --region gb_london --duration 30m --mode delay
```

Sample output:

```text
[2026-04-29T18:30] region=gb_london duration=30m mode=delay
Decision: delay 15m (placeholder, add real adapters in v0.0.2)
```

The timestamp will vary.

The schedule decision is placeholder output. No real carbon-intensity adapter, scheduling algorithm, or verified methodology is used in the current implementation.
