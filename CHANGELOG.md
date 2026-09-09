# Changelog

## [2.1.0] - 2026-09-09

### Added

- Add valid Claude Code plugin and marketplace manifests for the documented
  installation workflow.
- Add explicit error handling and approval boundaries for local and GitHub
  writes.
- Add a pinned CI gate for skill, command, manifest, and reference consistency.

### Changed

- Migrate deprecated `compatible-with` metadata to the current free-text
  `compatibility` field.
- Replace stale platform and review-app claims with capability gates and links to
  current authoritative documentation.
- Use the correct plugin-root variable from the `/github-learn` command.

### Security

- Require confirmation before repository creation, commit, push, merge, branch
  deletion, or GitHub App installation.

## [2.0.0]

- Initial two-mode setup and nine-lesson curriculum.
