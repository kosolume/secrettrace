# Threat Model

## Security objective

SecretTrace should identify potential credential exposure without becoming a new channel through which source code or credential material is disclosed.

## Protected assets

- Candidate secret values
- Source-code contents
- Repository paths and metadata
- Scan reports and CI artifacts
- User configuration and suppressions

## Trust boundaries

- User-supplied scan root
- Files and symbolic links inside that root
- Configuration and custom rules
- Terminal, logs, report files, and CI systems
- Third-party Python dependencies

## Initial threats and controls

| Threat | Initial control |
|---|---|
| Full candidate leaks into output | Central redaction before reporter boundary |
| Candidate leaks through exception text | Sanitized error types and tests |
| Scanner reads outside requested root | Resolved-path containment checks; conservative symlink policy |
| Binary or huge files exhaust resources | File-type checks and configurable size limits |
| Malicious regular expression causes excessive runtime | Reviewed built-in rules and bounded candidate inputs |
| Report exposes reusable secret material | Redacted values and non-secret-derived stable fingerprints |
| External service receives source code | No network calls in normal scan operation |
| Examples contain working credentials | Synthetic invalid fixtures and repository-wide regression scan |
| Compromised dependency affects scanner | Small dependency set, pinned ranges, and CI review |

## Non-goals for v1.0

- Proving whether a credential is active
- Automatically revoking or rotating credentials
- Rewriting Git history
- Scanning systems without authorization

This document is a living design artifact. Controls will be linked to tests as they are implemented.
