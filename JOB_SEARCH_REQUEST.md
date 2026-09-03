# JOB_SEARCH_REQUEST.md — 本次求职需求 / Search Request

这个文件是**可选的**。你也可以直接在 ChatGPT / Codex 对话里用自然语言告诉它本次需求。

`CANDIDATE_PROFILE.md` 和 `MASTER_CV.md` 描述“我是谁”；这个文件描述“**这一次我想找什么**”。

没有填写的项目应当被视为“开放探索”，而不是自动套用固定 internship 范围。

## 1. 本次目标 / Goal

- 我现在想找：`[例如：任何适合我的工作 / full-time / internship / research role / consulting / quant / 不确定，请先推荐]`
- 是否先推荐工作类别：`Yes`（默认） / `No，直接搜索`
- 推荐类别后：`等我确认`（默认） / `自动按推荐优先级继续搜索`

## 2. Employment type / career stage

可多选，也可以填 `Any`：

- `Any`
- Full-time
- Internship
- Part-time
- Contract / temporary
- Fellowship
- Research assistant / pre-doc / post-doc（如适用）
- Academic / industry / government / nonprofit / international organization
- Other: `[填写]`

## 3. Geography / work mode

- 地理范围：`[例如 US-wide / Canada / NYC only / global / 无限制]`
- Remote：`Yes / No / Either`
- Hybrid：`Yes / No / Either`
- Onsite：`Yes / No / Either`
- 是否愿意 relocation：`[Yes / No / Depends]`

## 4. Timing

- 希望开始时间：`[例如 2027 summer / after graduation / anytime / unspecified]`
- 搜索窗口：`[current openings / last 7 days / last 30 days / upcoming programs]`
- 是否考虑未来尚未开放的 pipeline：`Yes / No`

## 5. Role / industry preferences

- 特别想要的工作类别：`[可留空]`
- 特别想要的行业/公司：`[可留空]`
- 想探索的相邻方向：`[可留空；默认 Yes]`
- 明确不想要：`[可留空]`

## 6. Priorities / constraints

按重要性填写即可：

- Technical/research intensity: `[high / medium / any]`
- Economics relevance: `[high / medium / any]`
- Finance relevance: `[high / medium / any]`
- Compensation priority: `[high / medium / low / unspecified]`
- Brand / employer prestige: `[high / medium / low / unspecified]`
- Work-life balance: `[high / medium / low / unspecified]`
- Sponsorship / work authorization：**不要在公开 GitHub 文件中填写私人信息**；如需要，请在当前聊天里提供，或只放在本地 `PRIVATE_PROFILE.json`。
- Other hard constraints: `[填写]`

## 7. Output preference

- 推荐工作类别数量：`10`（默认）
- 最终职位结果数量：`20`（默认）
- 是否显示低匹配但值得探索的类别：`Yes`（默认）
- 是否给每个类别典型 job titles：`Yes`
- 是否给 employer families / example employers：`Yes`
- 是否给 skill gaps / preparation suggestions：`Yes`

## 最简写法

你完全可以不编辑本文件，只对 ChatGPT / Codex 说：

```text
根据我的背景，我现在想找美国范围内的工作，不限 internship 或 full-time。
先不要搜索具体职位。先推荐 10 个最适合我的工作类别，分成 Core / Adjacent / Exploratory，
每类给典型 title、为什么适合、我的 gap 和适合的公司类型。等我确认后再搜。
```

或者：

```text
我这次只想找纽约的 full-time quant / research / finance roles，2027 年可以开始。
先推荐类别，然后按你的推荐自动继续搜索当前 open positions。
```
