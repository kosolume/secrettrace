# SecretTrace

[![CI](https://github.com/jpaintsil-neu/secrettrace/actions/workflows/ci.yml/badge.svg)](https://github.com/jpaintsil-neu/secrettrace/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

SecretTrace is an offline-first command-line security scanner for finding potentially exposed credentials in source-code repositories. Its planned detection pipeline combines pattern matching, entropy analysis, contextual scoring, configurable suppression, and safe-by-default redaction.

> **Project status:** Foundation phase. Repository structure, quality gates, documentation, and delivery workflow are being established before the detection engine is implemented.

## Why I am building it

Secret scanning is not only a pattern-matching problem. A useful scanner must balance detection coverage against false positives while ensuring it doesn't leak the values it finds. This project explores that engineering problem through an explainable, privacy-conscious pipeline suitable for local development and CI.

## Planned v1.0 capabilities

- Recursive, root-bounded text-file discovery
- Binary and oversized-file avoidance
- Known-format and configurable regular-expression rules
- Shannon-entropy analysis
- Context-aware confidence scoring
- Severity classification and stable fingerprints
- Path exclusions, allowlists, and suppression rules
- Redacted console and JSON reports
- Predictable exit codes for CI pipelines
- Unit, integration, security, and regression tests

Git-history scanning, pre-commit integration, SARIF output, parallel execution, remote scanning, and secret-validity checks are intentionally deferred until after v1.0.

## Secure design principles

1. **Offline first:** normal scans make no network requests.
2. **Redact by default:** findings, logs, exceptions, and artifacts must never expose a complete candidate value.
3. **Explainable results:** findings identify the signals that contributed to confidence.
4. **Conservative filesystem access:** scans stay within the requested root and handle symbolic links cautiously.
5. **Synthetic test data only:** examples and tests never contain active credentials.

See [Threat Model](docs/threat-model.md) and [Architecture](docs/architecture.md) for the current design baseline.

## Architecture

```text
CLI -> Scan Coordinator -> File Discovery -> Detector Registry
                                      |-> Regex Detector
                                      |-> Entropy Detector
                                      |-> Context Detector
Detector Results -> Confidence Scorer -> Suppression Engine -> Reporters
```

Detection, scoring, suppression, and reporting are separate concerns so each can evolve and be tested independently.

## Development setup

Requirements:

- Python 3.11 or newer
- Git

```bash
git clone https://github.com/jpaintsil-neu/secrettrace.git
cd secrettrace
python -m venv .venv
source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Verify the foundation:

```bash
secrettrace --version
pytest
ruff check .
mypy src
```

The `scan` command is reserved in the CLI but intentionally reports that the detection engine is not implemented during this foundation phase.

## Repository map

```text
secrettrace/
├── src/secrettrace/        
├── tests/                  
├── docs/                   
├── examples/               
├── .github/workflows/      
├── pyproject.toml          
└── .secrettrace.yml        
```

## Quality gates

Every change is expected to pass:

- tests on supported Python versions;
- Ruff linting and formatting checks;
- mypy static type checking; and
- coverage reporting.

The long-term coverage target is at least 85% meaningful coverage, with emphasis on detector, redaction, filesystem, and configuration logic.

## Roadmap

- **v0.1 — Foundation:** package, CLI, domain models, and secure file discovery
- **v0.2 — Detection:** regex rules, private-key detection, and redaction
- **v0.3 — Analysis:** entropy, context, and confidence scoring
- **v0.4 — Control:** configuration, exclusions, allowlists, and suppression
- **v0.5 — Reporting:** console/JSON output and CI exit codes
- **v1.0 — Release:** integration tests, benchmarks, security review, and documentation
- **Post-v1.0:** Git history, pre-commit, SARIF, and extensibility

## Responsible use

Use SecretTrace only on repositories and files you own or are authorized to assess. A finding indicates a potential secret, not proof that a credential is valid. If a real secret is exposed, revoke or rotate it; deleting it from the latest file alone does not remove it from Git history.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Security-sensitive reports should follow [SECURITY.md](SECURITY.md).

## License

Licensed under the [MIT License](LICENSE).
