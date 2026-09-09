# GitHub Host Capability Guide

Use this guide to establish what the active agent host can actually do before a
lesson or setup workflow. Product names alone are not proof of capability.

## Capability gate

Check these capabilities in order:

| Capability | Read-only check | Required for |
|---|---|---|
| Local shell | `git --version` | Local repository lessons |
| Local repository | `git rev-parse --show-toplevel` | Branch, commit, and history lessons |
| GitHub CLI | `gh --version` | GitHub authentication and remote operations |
| GitHub authentication | `gh auth status` | Repository, pull-request, and review writes |
| File tools | Read, Glob, Grep, and a safe write mechanism | Guided edits and secret checks |
| User prompting | A host-native question or confirmation tool | Ambiguous choices and approval boundaries |

If a capability is absent, teach the concept or provide the exact command for
the user to run. Never claim an operation completed without a returned receipt.

## Claude Code

Claude Code can use local `git`, the GitHub CLI, file tools, and user prompts when
those tools are available and permitted in the session. The plugin command uses
`${CLAUDE_PLUGIN_ROOT}` to locate the bundled skill; the skill uses
`${CLAUDE_SKILL_DIR}` for its own references.

Use browser/device OAuth through `gh auth login`. Do not ask the user to paste a
GitHub token into chat. Before remote writes, show the account and repository
reported by `gh auth status` and `git remote -v`.

## Other terminal-capable agent hosts

Cursor, Windsurf, and other coding agents can use this curriculum only when they
provide equivalent file tools, a terminal, `git`, `gh`, and an interactive
confirmation path. Translate host-specific tool names; do not copy Claude Code
tool invocations literally.

If the host cannot ask questions during a run, stop before choices such as
public/private visibility, authentication, force-push, repository creation,
merge, or GitHub App installation.

## Browser-only chat hosts

Without a connected repository or terminal, provide explanations, command
previews, and exercises only. Do not claim to inspect a repository or execute a
GitHub operation. Ask the user to paste sanitized output when diagnosis depends
on local state.

## Authentication and permissions

- Let `gh` own GitHub authentication and credential storage.
- Prefer the least repository and organization access needed for the lesson.
- Treat installing a GitHub App as an external authorization change. Show its
  requested permissions and obtain explicit approval.
- Re-check the active GitHub account before creating a repository or pushing.
- Never put tokens in command arguments, lesson transcripts, commits, or files.

## Authoritative references

- [Claude Code common workflows](https://code.claude.com/docs/en/common-workflows)
- [GitHub CLI manual](https://cli.github.com/manual/)
- [GitHub authentication documentation](https://docs.github.com/en/authentication)
