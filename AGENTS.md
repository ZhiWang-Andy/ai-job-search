---
framework_version: 1.1.0-chatgpt
---

# Agent Guidelines: Zhi Wang Job Search

This workspace is a personalized job-search system. **ChatGPT / OpenAI Responses API is the primary AI runtime.**

## Single source of truth

Candidate facts:
- `profile/zhi_wang.md`
- `cv/zhi_wang_master.md`

Search targets:
- `config/search_preferences.json`

Primary OpenAI workflow:
- `CHATGPT.md`
- `chatgpt_job_agent.py`

Private contact details:
- optional local `config/private_profile.json` (git-ignored)

## Compatibility with upstream

The original `.claude/commands/` and `.claude/skills/` directories are retained from `MadsLorentzen/ai-job-search` so upstream updates remain mergeable and the workspace can still be used from Claude Code, Codex, Cursor, Gemini CLI, or other agent tools.

When an upstream instruction conflicts with this fork's candidate facts, the canonical files above win. Do not replace Zhi Wang's profile with upstream example data.

## Portal search tools

Portable search CLIs remain under `.agents/skills/`. They can be used directly, but the default entry point for this fork is:

```bash
python chatgpt_job_agent.py search
```

For fit evaluation and application preparation, follow the factual-grounding and privacy rules in `CHATGPT.md`.
