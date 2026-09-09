# GitHub Code Review Options

Automated review supplements human review; it does not prove a change is safe or
correct. Choose a tool only after checking repository risk, data access,
governance requirements, and the tool's current documentation.

## Start with the repository's native gates

Before adding an AI reviewer:

1. Require relevant tests, lint, and security checks.
2. Protect the default branch with the appropriate ruleset.
3. Require human review for sensitive or high-impact changes.
4. Document ownership and review expectations in `CODEOWNERS`, `AGENTS.md`, or
   repository instructions as appropriate.

## Current review categories

### GitHub Copilot code review

GitHub Copilot can review pull requests and can be requested manually or through
repository rulesets where the account and plan permit it. Configuration,
availability, review effort, billing, approval behavior, and organization policy
change over time; verify them in GitHub's current documentation and repository
settings before enabling automatic reviews.

### CodeQL

CodeQL provides deterministic code scanning and code-quality findings through
GitHub checks. It is a security and static-analysis gate, not a substitute for a
general code review. Select only the languages present in the repository and
confirm the workflow passes on a representative pull request.

### Third-party GitHub Apps

CodeRabbit, Greptile, and Qodo offer pull-request review integrations. Treat each
installation as an authorization decision:

- inspect requested repository and organization permissions;
- scope installation to the smallest repository set;
- review retention, training, indexing, and private-code policies;
- verify current pricing and feature availability from the vendor;
- test on a low-risk pull request before relying on results;
- document how to disable and uninstall the integration.

Do not install an app, accept new permissions, or enable automatic writes without
explicit user authorization.

## Decision guide

| Need | Start with | Verify |
|---|---|---|
| Security vulnerabilities | CodeQL and language-specific scanners | Query coverage, workflow permissions, required checks |
| Native GitHub AI feedback | Copilot code review | Account policy, billing, ruleset behavior, re-review policy |
| Cross-file or vendor-specific review | A scoped third-party app trial | Permissions, data policy, noise rate, uninstall path |
| Merge confidence | Human review plus CI | Test evidence, unresolved threads, branch protection |

## Safe hands-on exercise

1. Use a public or synthetic test repository with no secrets or customer data.
2. Show the app permissions and obtain explicit approval before installation.
3. Open a small pull request containing a known, non-sensitive defect.
4. Compare findings with tests and a human review; do not grade solely on comment
   count.
5. Remove the app if the evaluation is complete or its access is not justified.

## Authoritative references

- [About GitHub Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review)
- [Configure GitHub Copilot code review](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-code-review)
- [CodeQL code-quality analysis](https://docs.github.com/en/code-security/reference/code-quality/codeql-detection)
- [CodeRabbit documentation](https://docs.coderabbit.ai/)
- [Greptile documentation](https://docs.greptile.com/)
- [Qodo code review documentation](https://docs.qodo.ai/code-review)
