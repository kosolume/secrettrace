# Contributing to SecretTrace

SecretTrace is currently developed through small, reviewable changes tied to GitHub issues.

## Workflow

1. Open or select an issue with explicit acceptance criteria.
2. Create a focused branch from `develop`.
3. Add or update tests with the implementation.
4. Run `ruff check .`, `ruff format --check .`, `mypy src`, and `pytest`.
5. Open a pull request explaining behavior, security implications, and test evidence.

## Security rules

- Never commit real credentials or copied production secrets.
- Use clearly synthetic invalid values in tests and documentation.
- Never include complete candidate values in logs, snapshots, screenshots, or failure messages.
- Treat changes to redaction, filesystem traversal, rules, and reporting as security-sensitive.

## Commit style

Use concise imperative messages, for example:

- `feat: add root-bounded file discovery`
- `test: cover malformed UTF-8 input`
- `docs: explain redaction boundary`

For private vulnerability reports, follow [SECURITY.md](SECURITY.md).
