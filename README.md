# ChatGPT Desktop Job Search Starter Kit — Zhi Wang

这是一个**无需 OpenAI API Key、无需 Python、无需安装依赖**的轻量求职资料包。

下载 ZIP、解压后，你可以直接在 **ChatGPT Desktop 的 Codex 或 Work 模式**中打开整个文件夹；如果只想用普通 Chat，也可以只上传一份合并好的 context 文件开始求职。

> 这是 `ZhiWang-Andy/ai-job-search` 的 Desktop-only starter kit。完整开发版仍在主项目中维护。

## 方法 A：Codex Desktop（最推荐）

1. 下载本分支 ZIP 并解压，例如到 `D:\job-search-desktop-kit`。
2. 打开 ChatGPT Desktop。
3. 左上角切换到 **Codex**。
4. 打开刚才解压后的文件夹。
5. 复制 `START_PROMPT_CN.txt` 作为第一条消息。
6. 之后直接说：
   - `找今天新开的、适合我的 Summer 2027 PhD 实习，给我前 20 个。`
   - `评估这个岗位：https://...`
   - `为这个岗位准备 tailored resume 和 cover letter，但不要提交申请。`
   - `帮我准备这个公司的面试。`

**不需要运行 Python，也不需要设置 `OPENAI_API_KEY`。**

## 方法 B：Work Desktop

在 ChatGPT Desktop 中切换到 **ChatGPT → Work**，打开解压后的本地文件夹，然后使用 `START_PROMPT_CN.txt`。Work 和 Codex 都可以在获得你的许可后使用本地文件夹。

## 方法 C：普通 Chat，只上传一个文件

如果你不想打开整个文件夹，最省事的方法是新建普通 Chat / Work 对话，只上传：

```text
CHATGPT_UPLOAD_SINGLE_FILE.md
```

然后直接说：

```text
使用我上传的文件作为本次求职的事实来源和搜索规则。
现在搜索当前仍可申请、适合我的 Summer 2027 / PhD-level 工作和实习，优先官方公司招聘页或 ATS，并按 fit 排名。
```

这一份文件已经合并了公开安全版背景、研究/经历、技术能力、target role families、搜索规则和 resume tailoring 原则。

## 方法 D：普通 Chat，上传模块化文件

如果你希望资料分开管理，上传以下 4 个文件：

1. `CHATGPT_CONTEXT.md`
2. `CANDIDATE_PROFILE.md`
3. `MASTER_CV.md`
4. `SEARCH_PREFERENCES.json`

然后让 ChatGPT 把它们作为候选人事实来源和搜索规则。

## 文件说明

| 文件 | 用途 |
|---|---|
| `AGENTS.md` | Codex Desktop 项目级规则 |
| `CHATGPT_CONTEXT.md` | 搜索、fit、申请、安全和隐私规则 |
| `CHATGPT_UPLOAD_SINGLE_FILE.md` | 普通 Chat/Work 一次只上传这一份即可 |
| `CANDIDATE_PROFILE.md` | 公开安全版候选人事实 |
| `MASTER_CV.md` | Resume tailoring 的事实来源 |
| `SEARCH_PREFERENCES.json` | 岗位范围、source priority、status/dedupe 规则 |
| `PROMPTS.md` | 中英文 ready-to-use prompt |
| `START_PROMPT_CN.txt` | 中文第一条 prompt |
| `START_PROMPT_EN.txt` | 英文第一条 prompt |
| `PRIVATE_PROFILE_TEMPLATE.json` | 可选本地私人字段模板；不要上传公开仓库 |
| `job_search_tracker.csv` | 本地职位追踪表模板 |

## 默认搜索策略

ChatGPT / Codex 会被要求：

- 重点搜索 **Summer 2027 / PhD internships / graduate internships**，并考虑 May 2028 graduation timeline；
- 美国范围内搜索，不只限 Columbus；
- 广泛覆盖 quantitative research/trading、systematic investing、finance/risk/credit、applied/research scientist、causal inference/data science、economic consulting/antitrust、pricing/marketplace science、policy/program evaluation、central banks/international institutions 等；
- 优先使用**雇主官方 careers 页面和官方 ATS requisition**；
- 只有存在当前有效 application path / active requisition 才标为 `open`；
- 尽可能记录 job/requisition ID、location、posted date/deadline、status、fit score 和官方链接；
- 对同一 requisition 去重；此前只是 upcoming、现在正式开放的项目应作为新的 active opportunity；
- 不捏造技能、经历、publication、trading P&L、work authorization 或其他资格。

## 内置浏览器

在 Desktop 的 Work / Codex 中，Windows 可按：

```text
Ctrl + Shift + B
```

打开内置浏览器。打开某个职位后可以直接说：

```text
评估当前浏览器中的职位。使用本文件夹中的候选人资料作为事实来源，不要编造资格。
```

## 申请控制与隐私

这个 starter kit 可以搜索职位、做 fit evaluation、tailor resume、写 cover letter、做 company research 和 interview prep，但默认**不会替你最终提交申请**，不会替你接受法律条款，不会自动回答 EEO/demographic，也不会在你未明确提供时声明 work authorization / sponsorship。

GitHub 上只包含公开安全信息。Email、电话、地址、签证/工作许可等私人字段不要提交到公开仓库。需要时可把 `PRIVATE_PROFILE_TEMPLATE.json` 复制成 `PRIVATE_PROFILE.json` 并只保存在本地；`.gitignore` 已排除它。

如果 Codex 需要保存结果，建议写到：

```text
output/
company_research/
```

这两个位置默认被 git-ignore。

---

# English Quick Start

This is a **no-API, no-Python, no-install** context package for ChatGPT Desktop.

Recommended: download/extract the branch ZIP → open the folder in **Codex** or **Work** → paste `START_PROMPT_EN.txt`.

For a normal Chat/Work conversation without folder access, upload only `CHATGPT_UPLOAD_SINGLE_FILE.md`; it contains the public-safe candidate facts, search strategy, fit rules, and tailoring guidance needed for job-search work.

No OpenAI API key is required for this direct Desktop workflow. The full repository's optional Python/API automation is intentionally not included in this starter branch.
