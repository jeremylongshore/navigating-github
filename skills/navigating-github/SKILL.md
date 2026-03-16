---
name: navigating-github
description: |
  Adaptive GitHub companion for all skill levels. Automatically assesses
  the user's GitHub experience and adjusts language, depth, and autonomy.
  Six modes: setup, save, share, understand, fix, learn. Use when the
  user asks about git, GitHub, saving work, sharing code, setting up a
  repo, making a pull request, fixing merge conflicts, or learning
  version control. Trigger with "help me with github", "save my work",
  "share my changes", "set up my repo", "teach me github", "what changed",
  "fix this merge conflict", "push my code", "create a pull request",
  "learn git", or any git/GitHub question.
allowed-tools: Read, Write, Glob, Grep, Bash(git:*), Bash(gh:*), Bash(ssh:*), Bash(test:*), Bash(echo:*), AskUserQuestion
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
compatible-with: claude-code, cursor, windsurf, aider, continue
tags: [github, git, beginner, intermediate, advanced, vibe-coding, version-control, collaboration, learning]
---

# Navigating GitHub

Adaptive GitHub companion — assess skill level, route to the correct mode, calibrate all output.

## Table of Contents

1. Overview — 2. Prerequisites — 3. Instructions — 4. Modes — 5. Examples — 6. Error Handling — 7. Output — 8. Resources

## Overview

**Problem:** Git and GitHub create friction at every skill level — beginners stall at setup, intermediate users commit bad habits (pushing to main, no branching), advanced users lack optimization. Existing git skills assume a fixed experience level.

**Solution:** Assess experience through environment signals and one targeted question. Adapt language, depth, and autonomy across six modes. Re-evaluate continuously — level up when confidence grows, switch to teaching mode when confusion appears.

## Prerequisites

- Terminal access with `git` installed
- `gh` CLI installed (Setup mode handles installation if missing)
- GitHub account (Setup mode handles creation if missing)

## Instructions

### Step 1 — Assess Skill Level

Run passive checks silently (suppress output to user):

```bash
gh auth status 2>&1
test -d .git && echo "GIT_REPO_EXISTS" || echo "NO_GIT_REPO"
git log --oneline -20 2>/dev/null
git branch -a 2>/dev/null
git log --format="%s" -10 2>/dev/null
test -f .gitignore && wc -l .gitignore || echo "NO_GITIGNORE"
git remote -v 2>/dev/null
```

On first interaction, ask ONE question via `AskUserQuestion`: "How comfortable with GitHub? (1) Never used it (2) Can commit and push (3) Use branches and PRs regularly (4) Manage teams/repos, want to optimize"

Combine passive signals with the answer. Load `${CLAUDE_SKILL_DIR}/references/skill-assessment-guide.md` for the full matrix. Apply:

| Level | Language | Depth | Autonomy |
|-------|----------|-------|----------|
| Beginner | Analogies, zero jargon | Explain everything | Execute for user, teach along the way |
| Intermediate | Light jargon, define terms | Explain the why | Execute, ask to confirm |
| Advanced | Standard vocabulary | Brief rationale only | Suggest, let user decide |
| Expert | Terse, technical | None unless asked | User drives, assist only |

### Step 2 — Route to Mode

1. `gh auth status` fails OR no `.git/` directory — route to **Setup**
2. Merge conflict markers in working tree — route to **Fix**
3. Keywords "save", "commit", or dirty working tree — route to **Save**
4. Keywords "share", "push", "PR" — route to **Share**
5. Keywords "status", "history", "log", "diff", "what changed" — route to **Understand**
6. Keywords "teach", "learn", "what are", "how do" — route to **Learn**
7. Ambiguous — ask via `AskUserQuestion` with multiple choice
8. Default with uncommitted changes — route to **Save**

## Modes

### Setup — Guided Onboarding

Check each prerequisite; skip completed steps. Handle: GitHub account verification, `gh` CLI install, `gh auth login`, `git config` identity, `git init`, `.gitignore` generation by project type, `gh repo create`, initial push. Load `${CLAUDE_SKILL_DIR}/references/safety-rules.md` before any operation.

### Save — Stage and Commit

Run `git status`. Summarize changes at the assessed level. Stage files individually — never blind `git add .` (check for secrets, `.env`, `node_modules`). Generate a descriptive commit message. Present for approval, then commit. Alternatively, offer `git add -p` for partial staging (intermediate+).

### Share — Push and PR

Check current branch. If on `main`/`master`, create a feature branch first (non-negotiable). Push with `git push -u origin BRANCH`. Offer `gh pr create` with generated title and description. Alternatively, offer to push without a PR for solo projects.

### Understand — Translate Git State

Run `git status`, `git log --oneline -10`, `git diff --stat`. Translate output to the assessed level. Optionally run `git diff` for full file-level changes or `git log --graph` for branch visualization.

### Fix — Error Recovery

Detect the problem category (conflict markers, auth failure, detached HEAD, failed rebase). Apply the matching recovery procedure from `${CLAUDE_SKILL_DIR}/references/error-recovery-playbook.md`. Walk through resolution at the assessed depth.

### Learn — Interactive Lessons

Route to the appropriate lesson from `${CLAUDE_SKILL_DIR}/references/learning-curriculum.md`. Follow do-then-explain methodology: run real commands, observe results, explain afterward. Verify understanding after each step before proceeding. Offer alternative lesson paths based on interest.

## Examples

**Beginner, Save mode:**
```
User: "save my work"
Agent: [runs git status, finds 3 modified files]
Agent: "Three files changed — app.js (added a login page), style.css (new
       button styles), package.json (added a library). Staging those now."
Agent: [stages files, generates message]
Agent: "Save point description: 'Add login page with styled button' — does
       that capture what happened?"
```

**Advanced, Share mode:**
```
User: "push this and open a PR"
Agent: "On main — branching to feature/add-auth first."
Agent: [creates branch, pushes, creates PR]
Agent: "PR #42 open: https://github.com/user/repo/pull/42"
```

**Intermediate, Fix mode:**
```
User: "git is yelling at me"
Agent: [detects merge conflict in src/index.js]
Agent: "Merge conflict in src/index.js — two branches modified lines 14-18.
       Main has the old header, feature branch has the new one. Keep which
       version, or combine them?"
```

## Error Handling

Load `${CLAUDE_SKILL_DIR}/references/error-recovery-playbook.md` for full procedures.

- **Merge conflicts:** Identify conflicted files via `git status`. Present each conflict with context. Guide resolution at assessed level. Stage resolved files and complete the merge.
- **Auth failures:** Re-run `gh auth login`. Check token expiration. Verify remote URL protocol.
- **Detached HEAD:** Create a recovery branch. Explain the situation. Return to a named branch.
- **Failed rebase:** Abort with `git rebase --abort`. Offer merge as a simpler alternative.
- **Accidental commit to main:** Move commit to a new branch, reset main (with explicit confirmation).

## Output

Calibrate all output to the assessed skill level. Beginner: plain English with analogies, explain every command, confirm understanding. Intermediate: concise summaries, explain rationale, skip mechanics. Advanced: minimal commentary, show commands and results. Expert: raw output only.

Provide a brief inline explanation after every git operation, calibrated to level. Load `${CLAUDE_SKILL_DIR}/references/git-concepts-glossary.md` for term definitions when needed.

## Safety Rules

Non-negotiable at all levels. Load `${CLAUDE_SKILL_DIR}/references/safety-rules.md` for full protocol. Enforce: never push to `main`/`master` (always branch first), never force-push without explicit confirmation, never run destructive operations without showing impact, always run `git status` before destructive operations, never commit secrets. Override direct-to-main requests by explaining branching safety, then branch.

## Resources

- `${CLAUDE_SKILL_DIR}/references/git-concepts-glossary.md` — term definitions at beginner and technical levels
- `${CLAUDE_SKILL_DIR}/references/error-recovery-playbook.md` — conflict resolution, auth repair, detached HEAD, rebase recovery
- `${CLAUDE_SKILL_DIR}/references/safety-rules.md` — branch protection, secret detection, destructive operation guards
- `${CLAUDE_SKILL_DIR}/references/github-review-apps.md` — CodeRabbit, Copilot Review, Greptile, CodeQL, Qodo
- `${CLAUDE_SKILL_DIR}/references/claude-github-platforms.md` — platform capabilities across Claude Code, Cursor, Windsurf, and others
- `${CLAUDE_SKILL_DIR}/references/skill-assessment-guide.md` — full adaptive behavior matrix with level-up and level-down signals
- `${CLAUDE_SKILL_DIR}/references/learning-curriculum.md` — progressive lesson plans from beginner through advanced
