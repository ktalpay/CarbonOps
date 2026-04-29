# Contributing To CarbonOps

Thank you for your interest in CarbonOps.

CarbonOps is a pre-alpha carbon-aware DevOps / CI/CD reference toolkit. Contributions should keep the repository conservative, public-safe, and clear about what is implemented versus planned.

## Development Setup

```bash
git clone https://github.com/ktalpay/CarbonOps.git
cd CarbonOps
pip install -e .
pip install pytest
python -m pytest -q
```

## Repository Structure

```text
src/carbonops/     Python package and CLI entry points
tests/             Basic CLI tests
docs/              Documentation baseline
adr/               Architecture decision records
examples/          Synthetic example notes
```

## Contribution Guidelines

- Keep CarbonOps clearly pre-alpha.
- Separate implemented behavior from planned behavior.
- Do not claim adoption, commercial impact, operational use, verified emissions reduction, or external recognition.
- Use synthetic data for examples.
- Do not commit credentials, private data, customer data, internal endpoints, or private source code.
- Add tests for behavior changes.

## Pull Requests

For non-trivial changes, open an issue or describe the reason in the pull request.

A useful pull request should include:

- What changed.
- Why it changed.
- Test result.
- Any public-safety considerations.

## Running Tests

```bash
python -m pytest -q
```

## Code Style

- Keep code small and readable.
- Avoid unnecessary dependencies.
- Use clear names.
- Add comments only where they explain non-obvious decisions.

## Conduct

Please follow `CODE_OF_CONDUCT.md`.
