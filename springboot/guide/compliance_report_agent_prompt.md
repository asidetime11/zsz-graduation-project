# Agent 测试 Prompt（生成 compliance_report.json）

你是一个代码合规审计助手。请你对我提供的 Spring Boot 项目进行静态审查，并生成 **1 份 JSON 报告**，文件名必须为：`compliance_report.json`。

## 1) 审查范围

- 仅分析当前项目目录中的代码与模板。
- 不要编造不存在的文件与行号。

## 2) 输出要求（强制）

- **只输出 JSON**，不要输出解释文字、Markdown、注释。
- JSON 顶层字段必须与以下结构完全一致，字段名不可增删改：
  - `project_name` (string)
  - `difficulty_level` (string: easy | medium | hard)
  - `source_vuln_plan` (string)
  - `generated_date` (string, 格式 `YYYY-MM-DD`)
  - `total_issues` (number)
  - `summary` (object)
    - `by_severity`:
      - `critical` (number)
      - `high` (number)
      - `medium` (number)
      - `low` (number)
    - `by_category`:
      - `Sensitive Data Exposure` (number)
      - `Data Minimization` (number)
      - `Missing Consent` (number)
      - `Data Over-exposure` (number)
      - `Unauthorized Access` (number)
      - `Data Lifecycle` (number)
      - `SQL Injection` (number)
      - `XSS` (number)
      - `Sensitive Logging` (number)
      - `Hardcoded Secrets` (number)
  - `issues` (array)
    - 每个 issue 必须包含：
      - `issue_id` (string, 格式 `DC-001`, `DC-002`...)
      - `location` (object)
        - `file` (string, 例如 `src/main/java/com/example/user/UserController.java`)
        - `line` (number)
        - `class_or_function` (string)
      - `category` (string)
      - `description` (string)
      - `severity` (string: critical | high | medium | low)
      - `related_fields` (array of string)
      - `impact` (string)
      - `code_snippet` (string)

    ## 3) 一致性校验（强制）

- `total_issues` 必须等于 `issues.length`。
- `summary.by_severity` 的计数必须与 `issues[*].severity` 完全一致。
- `summary.by_category` 的计数必须与 `issues[*].category` 完全一致。
- `issue_id` 必须从 `DC-001` 开始连续递增。
- `location.line` 必须是正整数，且与 `code_snippet` 所在位置一致。
- `code_snippet` 必须来自真实代码片段，不可伪造。

  ## 4) 严重级别建议

- `critical`: 明文存储高度敏感数据、可直接导致大规模泄露
- `high`: 明显违反最小化/授权/访问控制原则，影响较大
- `medium`: 存在可利用风险，但需要额外条件
- `low`: 影响较轻或利用条件苛刻

  ## 5) 分类集合（仅可使用以下值）

- `Sensitive Data Exposure`
- `Data Minimization`
- `Missing Consent`
- `Data Over-exposure`
- `Unauthorized Access`
- `Data Lifecycle`
- `SQL Injection`
- `XSS`
- `Sensitive Logging`
- `Hardcoded Secrets`

## 6) 输出示例骨架（字段顺序建议保持一致）

{
  "project_name": "easy_01",
  "difficulty_level": "easy",
  "source_vuln_plan": "vuln_plan_easy_01.md",
  "generated_date": "2026-03-19",
  "total_issues": 0,
  "summary": {
    "by_severity": {
      "critical": 0,
      "high": 0,
      "medium": 0,
      "low": 0
    },
    "by_category": {
      "Sensitive Data Exposure": 0,
      "Data Minimization": 0,
      "Missing Consent": 0,
      "Data Over-exposure": 0,
      "Unauthorized Access": 0,
      "Data Lifecycle": 0,
      "SQL Injection": 0,
      "XSS": 0,
      "Sensitive Logging": 0,
      "Hardcoded Secrets": 0
    }
  },
  "issues": []
}

## 7) 最终动作

- 完成审查后，输出最终 JSON 内容，供我直接保存为 `compliance_report.json`。
