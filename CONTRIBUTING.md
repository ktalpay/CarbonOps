# Contributing to CarbonOps  
Thank you for your interest in contributing to CarbonOps — an open-source sustainability toolkit by **FutureOps Technology Ltd**.

We welcome contributions of all kinds: features, bug fixes, documentation, tests, and discussions.

---

# 🛠 Development Setup

```bash
git clone https://github.com/ktalpay/CarbonOps.git
cd CarbonOps
pip install -e ".[dev]"
```

### Recommended tools
- Python 3.9+
- pytest
- ruff (linting)
- black (formatting)
- typer (CLI development)

---

# 📁 Repository Structure

```
carbonops/
    cli/            # CLI entrypoints
    core/           # Calculation, models, utilities
    adapters/       # Data sources and integrations
tests/              # pytest test files
docs/               # Additional documentation
```

---

# ✔ Contribution Process

## 1) Open an Issue First  
For all non-trivial changes, create an issue describing:

- What you want to change  
- Why it is needed  
- Alternatives considered  

## 2) Create a Feature Branch

```bash
git checkout -b feature/my-change
```

## 3) Add Tests  
All new functionality must include tests.

Run tests with:

```bash
pytest
```

## 4) Apply Formatting

```bash
ruff check .
black .
```

## 5) Open a Pull Request  
Your PR must include:

- A clear description  
- Reference to the issue number  
- Test results  
- Screenshots (if applicable)

Maintainers will review your PR and may request changes.

---

# 🧪 Running Tests

```bash
pytest -q
```

---

# 📝 Commit Message Guidelines

We follow a simplified semantic commit style:

- feat: new feature  
- fix: bug fix  
- docs: documentation  
- refactor: non-functional restructuring  
- test: test improvements  
- chore: repo maintenance  

Example:

```
feat: add DEFRA 2024 dataset adapter
```

---

# 🌐 Code Style

- Follow PEP8  
- Use informative variable names  
- Keep functions small and testable  
- Avoid unnecessary dependencies  
- Document complex logic with docstrings  

---

# 🤝 Community Conduct

All contributors must adhere to our **Code of Conduct** (CODE_OF_CONDUCT.md).

---

# 🙌 Thank You

Your contributions help CarbonOps grow into the open sustainability standard we envision.  
FutureOps appreciates your support!
