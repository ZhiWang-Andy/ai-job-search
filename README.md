# ChatGPT Desktop Adaptive Job Search Starter Kit — Zhi Wang

这是一个**无需 OpenAI API Key、无需 Python、无需安装依赖**的轻量职业探索 + 求职资料包。

它现在不是一个“Summer 2027 internship 搜索器”，而是一个 **Adaptive Job Search Workspace**：

> **背景 + 本次需求 → 推荐工作类别 → 你确认/自动采用 → 搜索真实开放岗位 → fit / application / interview**

可以搜索 internship，也可以搜索 full-time、fellowship、research appointment、government、consulting、finance、tech、policy、international organization，或者任何与你背景有合理联系的工作。

## 推荐工作流

### Phase 1：提供背景

你的长期背景已经放在：

- `CANDIDATE_PROFILE.md`
- `MASTER_CV.md`

通常不需要每次重新描述。

### Phase 2：提供“这次我要找什么”

有两种方法：

1. 直接对 ChatGPT / Codex 用自然语言说；或
2. 编辑可选模板 `JOB_SEARCH_REQUEST.md`。

例如：

```text
我现在想找任何适合我的工作，不限 internship 或 full-time。
美国范围，remote/hybrid/onsite 都可以。
先不要搜索具体职位，先推荐最适合我的工作类别。
```

也可以非常具体：

```text
我只想看 NYC 的 full-time quant / finance / research roles，2027 年可以开始。
先推荐类别，然后按你的推荐自动继续搜索。
```

### Phase 3：先生成推荐工作类别

如果你的需求是开放式的，ChatGPT / Codex 默认先生成约 8–12 个方向，分成：

- **Core** — 与现有研究/技能/经历直接匹配；
- **Adjacent** — 可以利用 transferable skills 转入；
- **Exploratory** — 不那么显然，但值得测试的方向。

每一类会给：

- 工作类别；
- typical job titles / title variants；
- 为什么适合；
- 用到你哪些真实背景；
- gap / risk；
- 常见 employer families；
- 推荐优先级。

默认**先不搜索 vacancy**，等你选择。

你可以回复：

```text
搜索 Core 里的 1、2、4，再加 Adjacent 的 2。
```

或者：

```text
按你的推荐继续。
```

后者会自动用推荐的优先级开始搜职位。

如果你从一开始就已经知道范围，可以说：

```text
不要做类别规划，直接搜索。
```

## 方法 A：Codex Desktop（最推荐）

1. 下载本分支 ZIP 并解压，例如到 `D:\job-search-desktop-kit`。
2. 打开 ChatGPT Desktop。
3. 左上角切换到 **Codex**。
4. 打开刚才解压后的文件夹。
5. 复制 `START_PROMPT_CN.txt` 作为第一条消息。
6. 然后直接描述本次需求。

**不需要运行 Python，也不需要设置 `OPENAI_API_KEY`。**

## 方法 B：Work Desktop

在 ChatGPT Desktop 中切换到 **ChatGPT → Work**，打开解压后的本地文件夹，然后使用 `START_PROMPT_CN.txt`。之后可以直接做职业方向推荐、公开职位搜索、职位比较和申请材料准备。

## 方法 C：普通 Chat，只上传一个文件

如果你不想打开整个文件夹，只上传：

```text
CHATGPT_UPLOAD_SINGLE_FILE.md
```

然后说：

```text
使用这个文件作为我的背景和求职规则。
我这次没有固定 job title，也不限 internship/full-time。
先根据我的背景推荐 10 个工作类别，分 Core / Adjacent / Exploratory，
给典型 title、为什么适合、gap 和 employer types。先不要搜具体职位。
```

确认方向后再让它搜索。

## 方法 D：模块化文件

如果你希望资料分开管理，使用：

1. `CHATGPT_CONTEXT.md`
2. `CANDIDATE_PROFILE.md`
3. `MASTER_CV.md`
4. `SEARCH_PREFERENCES.json`
5. 可选 `JOB_SEARCH_REQUEST.md`

## 搜索范围如何决定

优先级是：

1. **你当前消息明确说的需求**；
2. `JOB_SEARCH_REQUEST.md` 中本次填写的需求；
3. `SEARCH_PREFERENCES.json` 中的默认值；
4. 根据你的真实背景做开放式职业发现。

因此：

- `Summer 2027 internship` 仍然是一个重要方向，但**不再是硬编码默认范围**；
- `US-wide` 是你没有提供 geography 时的默认值，但可以完全改成 Canada、NYC、global 等；
- employment type 默认是 `Any`；
- 不会因为过去重点找实习而自动排除 full-time。

## 文件说明

| 文件 | 用途 |
|---|---|
| `AGENTS.md` | Codex Desktop 项目级 adaptive workflow |
| `CHATGPT_CONTEXT.md` | 类别发现、搜索、fit、申请、安全和隐私规则 |
| `CHATGPT_UPLOAD_SINGLE_FILE.md` | 普通 Chat/Work 上传这一份即可 |
| `CANDIDATE_PROFILE.md` | 公开安全版候选人事实 |
| `MASTER_CV.md` | Resume tailoring 事实来源 |
| `SEARCH_PREFERENCES.json` | 默认偏好、role discovery seeds、source/status 规则 |
| `JOB_SEARCH_REQUEST.md` | 可选的“本次搜索需求”模板 |
| `PROMPTS.md` | 中英文 ready-to-use prompts |
| `START_PROMPT_CN.txt` | 中文第一条 prompt |
| `START_PROMPT_EN.txt` | 英文第一条 prompt |
| `PRIVATE_PROFILE_TEMPLATE.json` | 可选本地私人字段模板 |
| `job_search_tracker.csv` | 本地职位追踪表模板 |

## 搜索具体岗位时的规则

ChatGPT / Codex 会被要求：

- 只搜索本次选定的类别和约束；
- 支持 full-time、internship、part-time、contract、fellowship、research、academic、government、nonprofit、international-organization 等 employment types；
- 优先使用**雇主官方 careers 页面和官方 ATS requisition**；
- 只有存在当前有效 application path / active requisition 才标为 `open`；
- 尽可能记录 employment type、job/requisition ID、location、posted date/deadline、status、fit score 和官方链接；
- 对同一 requisition 去重；
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

Starter kit 可以做职业方向发现、职位搜索、fit evaluation、resume tailoring、cover letter、company research 和 interview prep，但默认**不会替你最终提交申请**，不会替你接受法律条款，不会自动回答 EEO/demographic，也不会在你未明确提供时声明 work authorization / sponsorship。

GitHub 上只包含公开安全信息。私人字段可保存在本地 `PRIVATE_PROFILE.json`；不要提交到公开仓库。

如果 Codex 需要保存结果，建议写到：

```text
output/
company_research/
```

这两个位置默认被 git-ignore。

---

# English Quick Start

This is a **no-API, no-Python, no-install adaptive career-discovery and job-search package** for ChatGPT Desktop.

Recommended workflow:

**candidate background + current request → Core/Adjacent/Exploratory role recommendations → user selection or auto-continue → current-opening search → fit/application/interview work.**

The kit is not internship-only. The user's current request overrides all defaults. `SEARCH_PREFERENCES.json` contains discovery seeds and fallback preferences rather than hard scope restrictions.

For Codex/Work, open the extracted folder and paste `START_PROMPT_EN.txt`. For normal Chat, upload only `CHATGPT_UPLOAD_SINGLE_FILE.md`.
