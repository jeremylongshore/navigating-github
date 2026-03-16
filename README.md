# Navigating GitHub

**The adaptive GitHub companion that meets you where you are.**

Whether you've never heard of GitHub or you're rebasing feature branches in your sleep, this skill adapts its language, depth, and autonomy to your experience level. It's the AI-native GitHub companion for everyone building with AI.

## Who Is This For?

- **Complete beginners** who need GitHub setup from scratch
- **Intermediate users** who commit and push but want better workflows
- **Advanced developers** who want to optimize their team collaboration
- **Anyone using AI coding tools** (Claude Code, Cowork, Cursor, Windsurf, Cline, Aider, Continue)

## How It Works

### AI-Driven Skill Assessment

The skill doesn't assume your level — it **figures it out** by reading signals from your environment and asking one targeted question. Then it adapts everything: language, explanations, how much it does for you vs. how much it lets you drive.

| Level | What You Experience |
|-------|-------------------|
| **Beginner** | Analogies, zero jargon, full step-by-step guidance. The AI does it for you and teaches as it goes. |
| **Intermediate** | Light jargon with definitions, explains the "why." The AI handles it and asks you to confirm. |
| **Advanced** | Standard git vocabulary, brief rationale only. The AI suggests, you decide. |
| **Expert** | Terse and technical. You drive, the AI assists. |

The skill continuously re-evaluates. If you start using branch commands confidently, it levels up. If you freeze on a rebase conflict, it drops into teaching mode for that topic.

## Six Modes

### Setup
*Triggers: no git repo, no GitHub auth, "set up my repo"*

Guided onboarding from zero to a working GitHub setup. Checks what's already done and only walks through what's missing: GitHub account, `gh` CLI, authentication, git identity, repo initialization, remote creation.

### Save
*Triggers: "save my work", "commit", uncommitted changes*

Stage changes, generate a meaningful commit message, and commit. Checks for secrets before staging. Beginners learn what commits are; advanced users get a one-liner.

### Share
*Triggers: "share my changes", "push", "create a PR"*

Branch if on main (always — safety first), push, and create a pull request with `gh`. Beginners learn what branches and PRs are; advanced users just get the URL.

### Understand
*Triggers: "what changed", "status", "show me the history"*

Translates `git status`, `git log`, and `git diff` into your language. Beginners get "you have 3 unsaved files." Advanced users get the raw diff with a summary.

### Fix
*Triggers: merge conflicts, auth errors, "I'm stuck"*

Conflict resolution, authentication repair, detached HEAD rescue, rebase recovery. Beginners get line-by-line walkthroughs. Advanced users get the diff and resolve it themselves.

### Learn
*Triggers: "teach me github", "what are branches", "how do PRs work"*

Interactive hands-on lessons using real commands on real repos. **Do-then-explain** methodology — run the command, see the result, then understand what happened.

**Beginner lessons:** GitHub 101, Branching Basics, Your First PR
**Intermediate lessons:** Branch Workflows, PR Review Flow, Team Git
**Advanced lessons:** Rebase vs Merge, GitHub Actions Basics, Code Review Ecosystem

## Install

### Claude Code
```bash
/plugin marketplace add jeremylongshore/navigating-github
```

### Manual
Clone this repo and add it to your Claude Code plugins directory:
```bash
git clone https://github.com/jeremylongshore/navigating-github.git
```

## Safety Rules (Non-Negotiable)

These apply at every skill level, every time:

- **Never** pushes to `main`/`master` — always branches first
- **Never** force pushes without explicit confirmation
- **Never** runs destructive operations (`reset --hard`, `clean -fd`) without showing you what will be affected and getting your OK
- **Never** commits secrets (`.env`, API keys, credentials)
- **Always** runs `git status` before any destructive operation

If you say "just push to main," it'll explain why branching is safer and branch anyway. Your code's safety comes first.

## Reference Files

The skill includes detailed reference material that the AI pulls from as needed:

| File | Contents |
|------|----------|
| `git-concepts-glossary.md` | Plain-English definitions of every git/GitHub term, with beginner analogies and technical details |
| `error-recovery-playbook.md` | Step-by-step recovery for merge conflicts, auth errors, detached HEAD, rebase problems |
| `safety-rules.md` | Full safety protocol — branch protection, secret detection, destructive operation guards |
| `github-review-apps.md` | Code review ecosystem — CodeRabbit, Copilot Review, Greptile, CodeQL, Qodo |
| `claude-github-platforms.md` | How GitHub works across Claude Code, Cowork, Cursor, and other AI platforms |
| `skill-assessment-guide.md` | How the AI determines your level and the full adaptive behavior matrix |
| `learning-curriculum.md` | Complete lesson plans for beginner through advanced |

## Platform Compatibility

Works with: **Claude Code**, **Cowork**, **Cursor**, **Windsurf**, **Cline**, **Aider**, **Continue**

The skill adapts to the platform's capabilities. Full hands-on experience on terminal-capable platforms; conceptual guidance where terminal access isn't available.

## Contributing

PRs welcome! This skill is designed to help everyone — if you see a gap in the curriculum, a confusing explanation, or a missing error recovery scenario, open an issue or submit a PR.

## License

MIT — see [LICENSE](LICENSE).

---

Built by [Jeremy Longshore](https://github.com/jeremylongshore) / [Intent Solutions](https://intentsolutions.io) for the [Tons of Skills](https://tonsofskills.com) marketplace.
