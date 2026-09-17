# Architecture

## Purpose

SecretTrace is structured as a pipeline whose filesystem, detection, scoring, suppression, and reporting concerns can be tested and changed independently.

## Planned component flow

1. The CLI parses user intent and configuration.
2. The scan coordinator creates a root-bounded scan plan.
3. File discovery selects readable text candidates and records skipped files.
4. Registered detectors produce candidate findings without reporting them directly.
5. The confidence scorer combines explainable signals.
6. The suppression engine applies explicit policy after detection.
7. Reporters receive sanitized finding models only.

## Design boundaries

- Detectors do not read arbitrary files or write output.
- Reporters never receive unredacted values.
- Configuration is validated before scanning begins.
- Filesystem traversal must not escape the resolved scan root.
- Network access is outside the normal scan pipeline.

## Planned extension points

- `Detector` protocol for candidate generation
- `Reporter` protocol for output formats
- Immutable `Finding` and `Rule` domain models
- Central detector registry
- Versioned configuration schema

Architecture decisions will be recorded as the implementation evolves rather than retroactively documenting unexplained code.
