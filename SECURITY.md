# Security Policy

## Supported versions

SecretTrace is pre-release software. Security fixes are applied to the latest code on the default branch until a stable release policy is published.

## Reporting a vulnerability

Do not open a public issue containing credential material, exploit details, or sensitive repository data. Use GitHub's private security-advisory reporting for this repository.

Include only the minimum information needed to reproduce the issue, and redact any credential-shaped value. Never submit an active secret as a proof of concept.

## Handling exposed credentials

If SecretTrace identifies an actual secret, rotate or revoke it through the relevant provider. Removing it from the latest file is not sufficient if it remains in Git history, forks, caches, logs, or build artifacts.
