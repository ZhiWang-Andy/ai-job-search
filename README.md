# ChatGPT Desktop Job Search Starter Kit — Zhi Wang

这是一个**无需 OpenAI API Key、无需 Python、无需安装依赖**的轻量求职资料包。

下载 ZIP、解压后，你可以直接在 **ChatGPT Desktop 的 Codex 模式**中打开整个文件夹；也可以在普通 Chat / Work 对话中上传核心文件，让 ChatGPT 按这里保存的个人资料和搜索规则帮你找工作、评估岗位、准备申请材料和面试。

> 本分支是 `ZhiWang-Andy/ai-job-search` 的 Desktop-only starter kit。完整开发版仍在主项目分支中维护。

## 最快使用方法（推荐：Codex Desktop）

1. 下载本分支的 ZIP，并解压到任意本地目录，例如：
   `D:\job-search-desktop-kit`
2. 打开 ChatGPT Desktop。
3. 左上角切换到 **Codex**。
4. 选择 / 打开刚才解压后的文件夹。
5. 打开 `START_PROMPT_CN.txt`，复制其中内容作为第一条消息。
6. 之后直接用自然语言，例如：
   - `找今天新开的、适合我的 Summer 2027 PhD 实习，给我前 20 个。`
   - `评估这个岗位：https://...`
   - `为这个岗位准备 tailored resume 和 cover letter，但不要提交申请。`
   - `帮我准备这个公司的面试。`

**不需要运行任何 Python 程序，也不需要设置 `OPENAI_API_KEY`。**

## 普通 Chat / Work 模式

如果你不想使用 Codex，也可以直接新建 Chat / Work 对话，然后上传以下 4 个文件：

1. `CHATGPT_CONTEXT.md`
2. `CANDIDATE_PROFILE.md`
3. `MASTER_CV.md`
4. `SEARCH_PREFERENCES.json`

上传后发送：

```text
请把我上传的四个文件作为本次求职工作的事实来源和搜索规则。
先不要改写我的经历。现在搜索当前仍可申请、适合我的 Summer 2027 / PhD-level 工作和实习，优先官方公司招聘页或 ATS，并按 fit 排名。
```

## 文件说明

| 文件 | 用途 |
|---|---|
| `AGENTS.md` | Codex Desktop 自动读取的项目级工作规则 |
| `CHATGPT_CONTEXT.md` | ChatGPT/Codex 的求职、评估、申请、安全和隐私规则 |
| `CANDIDATE_PROFILE.md` | 公开安全版个人背景；候选人事实来源 |
| `MASTER_CV.md` | Tailor resume 时的事实来源和方向 |
| `SEARCH_PREFERENCES.json` | 目标岗位、搜索范围、source priority、去重规则 |
| `PROMPTS.md` | 中英文常用 prompt 模板 |
| `START_PROMPT_CN.txt` | Codex Desktop 中文第一条 prompt |
| `START_PROMPT_EN.txt` | Codex Desktop 英文第一条 prompt |
| `PRIVATE_PROFILE_TEMPLATE.json` | 可选的本地私人信息模板；不要上传公开仓库 |
| `job_search_tracker.csv` | 可选的本地职位追踪表模板 |

## 默认搜索策略

这个 kit 会要求 ChatGPT / Codex：

- 重点搜索 **Summer 2027 / PhD internships / graduate internships**，并考虑 May 2028 graduation timeline；
- 美国范围内搜索，不只限 Columbus；
- 不只搜 `quant` / `economist`，还覆盖 quantitative research/trading、systematic investing、finance/risk/credit、applied/research scientist、causal inference/data science、economic consulting/antitrust、pricing/marketplace science、policy/program evaluation、central banks/international institutions 等；
- 优先使用**雇主官方 careers 页面和官方 ATS requisition**；
- 只有存在当前有效的 application path / active requisition 才标为 `open`；
- 记录 job/requisition ID、location、posted date/deadline（若可验证）、status、fit score 和官方链接；
- 对同一 requisition 去重；此前只是 upcoming、现在正式开放的项目应当作为新的 active opportunity 报告；
- 不捏造技能、工作经历、publication、trading P&L、work authorization 或其他资格。

## 浏览网页

在 Desktop 的 Work / Codex 中，如果需要手动查看公司招聘页，可以使用 ChatGPT Desktop 的内置浏览器。Windows 默认快捷键为：

```text
Ctrl + Shift + B
```

你可以打开某个职位页面后直接说：

```text
评估当前浏览器中的职位。使用本文件夹中的候选人资料作为事实来源，不要编造资格。
```

## 申请控制

这个 starter kit 可以用于：

- 搜索职位；
- fit evaluation；
- resume tailoring；
- cover letter；
- company research；
- interview preparation；
- 本地 tracker。

但默认**不会替你最终提交申请**，不会替你接受法律条款，不会自动回答 EEO/demographic，也不会在你没有明确提供的情况下声明 work authorization / sponsorship 情况。

## 私人信息

GitHub 上的 kit 只包含公开安全信息。Email、电话、地址、签证/工作许可等私人字段不要提交到公开 GitHub。

如果你希望 Codex 在本地使用这些字段，可以复制：

```text
PRIVATE_PROFILE_TEMPLATE.json
```

另存为：

```text
PRIVATE_PROFILE.json
```

只保存在本地。`.gitignore` 已排除它。

## 生成文件建议

Codex 需要保存本地结果时，让它写入：

```text
output/
company_research/
```

这两个目录默认被 git-ignore。

---

# English Quick Start

This is a **no-API, no-Python, no-install** context package for ChatGPT Desktop.

Recommended workflow:

1. Download and extract the branch ZIP.
2. In ChatGPT Desktop, switch to **Codex**.
3. Open the extracted folder.
4. Paste `START_PROMPT_EN.txt` as the first message.
5. Ask naturally, e.g. `Find current Summer 2027 PhD-compatible jobs that fit my profile.`

For ordinary Chat / Work mode, upload `CHATGPT_CONTEXT.md`, `CANDIDATE_PROFILE.md`, `MASTER_CV.md`, and `SEARCH_PREFERENCES.json` into the conversation and ask ChatGPT to use them as the factual job-search context.

No OpenAI API key is required for this direct Desktop workflow. The full repository's optional Python/API automation is intentionally not included in this starter branch.
