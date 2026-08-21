# Zhi Wang — ChatGPT Job Search Agent

<p align="center">
  <img src="assets/mascot/pip_flight_loop.gif" alt="AI job search mascot" width="180">
</p>

A personalized job-search and application workspace for **Zhi Wang**, Economics Ph.D. candidate at The Ohio State University.

This repository is based on [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) and keeps the upstream portal/search infrastructure, but this fork uses **ChatGPT / the OpenAI Responses API as the primary runtime** and uses Zhi Wang's own research, skills, resume, and job-search preferences as the source of truth.

## What this fork does

- searches current public job openings with OpenAI web search;
- searches broadly for Economics-PhD-compatible roles rather than only exact `economist` or `quant` titles;
- evaluates job fit against Zhi Wang's actual background;
- creates a tailored resume, cover letter, fit memo, and interview notes;
- tracks prepared applications locally;
- preserves the upstream `.agents/skills/` job-portal tools and `.claude/` workflows for compatibility;
- keeps private contact details and generated application materials out of the public repository.

## Candidate source of truth

- `profile/zhi_wang.md` — canonical candidate profile
- `cv/zhi_wang_master.md` — master resume facts and tailoring inventory
- `config/search_preferences.json` — target roles, cycle, and search strategy
- `CHATGPT.md` — grounding and workflow rules for ChatGPT
- optional local `config/private_profile.json` — private contact/logistics fields; git-ignored

The tracked profile is intentionally public-safe. Phone number, street address, and other private application fields are not committed.

## Target search directions

Primary targets include:

- Quantitative Research / Quantitative Trading / Systematic Investing
- Financial-market, asset-pricing, risk, treasury, credit, and portfolio research
- Applied Scientist / Research Scientist / Data Scientist roles using economics, causal inference, experimentation, pricing, demand, or marketplace methods

The search also actively includes economist/economic research, antitrust and competition consulting, pricing/revenue/consumer science, banking/credit analytics, strategy/business economics, policy/program evaluation, regulatory economics, and international/development-finance roles.

For the current configuration, prioritize **Summer 2027 / PhD internships and adjacent roles compatible with a May 2028 graduation**.

## Setup

### 1. Fork and clone

This repository is already Zhi Wang's personalized fork. If another user starts from the upstream template, the standard GitHub CLI path is:

```bash
gh repo fork MadsLorentzen/ai-job-search --clone
```

**Privacy warning:** a fork of a public repository is public. The upstream `/setup` workflow can write personal data into tracked files, so do not run it with private contact information in a public fork. See **SETUP.md section 8** for the upstream private-remote recipe before personalizing a new copy.

For this personalized fork, clone or update `ZhiWang-Andy/ai-job-search` and keep private fields only in the git-ignored `config/private_profile.json`.

### 2. Python environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-chatgpt.txt
$env:OPENAI_API_KEY="YOUR_KEY"
```

Optional: copy `config/private_profile.example.json` to `config/private_profile.json` and fill it locally. Do not commit that file.

Check configuration:

```powershell
python chatgpt_job_agent.py doctor
```

## Search jobs

Broad default search:

```powershell
python chatgpt_job_agent.py search
```

Focused search:

```powershell
python chatgpt_job_agent.py search --query "Summer 2027 PhD quantitative research internships in the US"
```

The search prefers official employer career/ATS pages, verifies that a role is currently applyable, deduplicates results, and scores fit using the personalized profile.

## Evaluate one job

```powershell
python chatgpt_job_agent.py evaluate "https://company.example/jobs/123"
```

You can also pass a local text file or paste a job description as the argument.

## Prepare an application

```powershell
python chatgpt_job_agent.py apply "https://company.example/jobs/123"
```

This creates a private local package under `chatgpt_output/` containing:

- `fit.md`
- `tailored_resume.md`
- `cover_letter.md`
- `interview_notes.md`
- `package.json`

It also appends a local `job_search_tracker.csv`. These files are ignored by git.

`apply` means **prepare the application package**. The project does not click final submit, answer attestations, or make work-authorization/EEO representations on the user's behalf.

## OpenAI runtime

The Python entry point uses the OpenAI Responses API, structured JSON outputs, and OpenAI's built-in web-search tool. The default model is `gpt-5.6`; override it with `OPENAI_MODEL` or `--model`.

## Upstream compatibility

The original project remains the upstream source for portal CLIs and workflow improvements. This fork was synchronized to upstream **v1.6.0** before the ChatGPT personalization layer was added. The personalization is kept in clearly separated files so future upstream updates remain manageable.

## Tests

```powershell
python -m pytest -q tests/test_chatgpt_job_agent.py
```

The personalized tests do not require an OpenAI API key.

## License and attribution

The upstream project is MIT-licensed. See `LICENSE` and the original repository for attribution and upstream documentation.