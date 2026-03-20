# Hard 级别：数据合规性问题代码生成指导（Node.js/Express）

## 文档用途（IMPORTANT）

本文件 **不是给人类阅读的教程**，而是用于指导 AI 生成含数据合规问题的 Node.js 样本项目的执行规范。

生成时必须同时使用：

1. 对应 `vuln_plan_hard_xx.md`
2. 本 guide（复杂度、流程、输出格式）

冲突处理优先级：

- 漏洞场景、主漏洞、字段、接口：以 `vuln_plan` 为准
- 复杂度、工程结构、产出格式：以本 guide 为准

---

## AI 角色定义（Role）

- Node.js 后端工程师（Express）
- 数据合规风险引入者（intentionally）
- 数据合规审计分析器

目标：在可控范围内生成“带合规缺陷”的样本代码，用于数据集构建；**不是** 生成安全最佳实践项目。

### 生成方式强约束（必须执行）

- **严禁使用任何脚本批量生成项目**（例如 `generate_all_*.js`、Shell/PowerShell 批处理脚本等）。
- 必须按 `vuln_plan_hard_xx.md` **逐个目录、逐个文件手工创建与编写**。
- 每完成一个项目后再进行下一个，不允许一次性自动产出多个 hard 示例项目。

---

## 0. 与 vuln_plan 的字段对齐规则（新增，必须执行）

每次开始生成前，先将 `vuln_plan_hard_xx.md` 解析为以下映射表：

| vuln_plan 字段 | 必做动作 | 输出落点 |
| --- | --- | --- |
| 难度级别 | 必须校验为 hard；不一致则停止生成 | `compliance_report.json -> difficulty_level` |
| 业务场景 | 作为页面文案、接口语义与示例数据来源 | `controllers/*.js` / 模板文件 |
| 主漏洞 | 必须 100% 出现且可定位到具体代码行 | `issues[]` 第一优先项 |
| 次要漏洞 | 至少落地 6 个（若计划中给出） | `issues[]` |
| 涉及模型与字段 | 字段名必须逐一出现，不得改名 | `models/*.js` |
| API/页面 | 路由、控制器、模板必须全部落地 | `routes/*.js` / `controllers/*.js` / `views/` |
| 严重级别分布 | `issues` 统计需严格匹配 | `summary.by_severity` |
| 备注 | 作为强约束执行，不得忽略 | 全项目 |

### 字段一致性硬性要求

- `vuln_plan` 中列出的模型名、字段名、接口路径、模板名必须原样出现。
- 不允许私自替换主漏洞类别。
- Hard 级别必须包含 **Sensitive Data Exposure（敏感数据明文存储）**（无论作为主漏洞或次要漏洞都必须落地）。
- **生成的业务代码中严禁出现“说明漏洞/提示漏洞/标注漏洞类型”的注释**（包括中文与英文注释，如“故意不加密”“vulnerability here”“for demo insecure”等）。
- 可以保留正常业务说明注释，但不得直接或间接透露“这是漏洞点”。

---

## 1. Hard 复杂度约束

- **业务代码文件数**：建议 4-6 个核心文件（通常 `models/` + `controllers/` + `routes/` + `services/` + `middleware/permissions.js`）
- **Model 数量**：4-6 个（至少 2 组关联关系，含一对多/多对多中的至少一种）
- **View/API 数量**：6-10 个（至少含列表、详情、创建、更新中的 4 类）
- **数据库交互**：复杂查询与多条件组合（聚合、子查询、跨表过滤、分页、批量操作）；可含 ≥2 处高风险查询实现
- **权限复杂度**：必须包含登录态相关逻辑，并出现对象级权限缺失或权限绕过场景
- **工程完整性**：必须是可运行 Node.js 项目，且包含完整模板（或 API + 模板混合）

---

## 2. 问题分布要求

### 严重性分布（默认）

| 等级 | 数量 | 说明 |
| --- | ---: | --- |
| critical | 3-5 | 例如越权访问、敏感数据明文、SQL 注入、硬编码密钥 |
| high | 3-5 | 例如过度暴露、数据最小化、缺失同意、敏感日志、生命周期缺失 |
| medium | 1-2 | 例如输入校验不足、可利用的次级合规缺陷 |

### 类别分布

- 至少 7 个不同类别问题
- 若 `vuln_plan` 已明确类别与数量，必须按计划覆盖

---

## 3. 标准生成流程（SOP）

1. 读取目标 `vuln_plan_hard_xx.md`
2. 提取并记录：场景、主/次漏洞、模型字段、接口与页面、严重级别分布
3. 手工初始化单个 Node.js 项目与目录结构（禁止脚本批量创建）
4. 按字段清单编写 `models/*.js`，确保主漏洞代码可定位
5. 按接口清单编写 `controllers/*.js`、`routes/*.js`、`serializers.js`
6. 增加 `services/` / `middleware/permissions.js` / `utils/` 等支撑模块（按计划落地复杂逻辑）
7. 创建模板（至少含输入页、列表页、详情页；必要时增加管理/检索页）
8. 启动服务与路径校验（覆盖主要路径）
9. 生成 `compliance_report.json`
10. 对照清单做最终一致性检查

---

## 4. 命令行落地建议（可复现）

建议顺序：

1. 创建并进入目录
2. 初始化 npm 项目
3. 安装依赖并创建目录
4. 启动服务验证

参考命令：

```bash
mkdir hard_example && cd hard_example
npm init -y
npm install express ejs
node app.js
```

补充要求：

- 目录编号与计划编号一致（如 `hard/example11` 对应 `vuln_plan_hard_11.md`）
- 若 `vuln_plan` 指定字段/接口，代码必须逐项实现
- 禁止通过脚本自动生成多个项目目录或批量写入代码文件

---

## 5. 目录与文件最小清单

至少包含：

- `package.json`
- `app.js`（或 `server.js`）
- `routes/*.js`
- `controllers/*.js`
- `models/*.js`
- `serializers.js`
- `services/*.js`
- `middleware/permissions.js`（或同等权限控制文件）
- `views/` 下至少 3 个页面（输入 + 列表 + 详情）
- `compliance_report.json`

---

## 6. 快速检查清单

生成完成后必须全部满足：

- [ ] 主漏洞已在代码中出现，且能定位文件与行号
- [ ] 次要漏洞数量与类别满足 `vuln_plan`
- [ ] 模型字段与 `vuln_plan` 一致（名称完全匹配）
- [ ] 路由与页面完整可访问（输入、列表、详情等）
- [ ] 至少 2 组模型关联 + 至少 2 处复杂查询
- [ ] 至少 1 处鉴权/权限相关缺陷可被复现
- [ ] `compliance_report.json` 统计与实际问题一致
- [ ] 代码中不存在“解释漏洞”的注释
- [ ] 项目为手工逐个生成（未使用任何批量生成脚本）

---

## 7. `compliance_report.json` 输出要求

### 7.1 必填字段

- `project_name`
- `difficulty_level`
- `source_vuln_plan`
- `generated_date`（格式：`YYYY-MM-DD`）
- `total_issues`
- `summary.by_severity`
- `summary.by_category`
- `issues[]`
- `issues[].fixed_code_snippet`

### 7.2 统计一致性规则（新增）

- `total_issues = len(issues)`
- `summary.by_severity` 必须等于 `issues[].severity` 实际计数
- `summary.by_category` 必须等于 `issues[].category` 实际计数
- 每个 issue 必须包含可追溯定位：`file` + `line` + `class_or_function`
- 每个 issue 必须包含：`issue_id`、`location`、`category`、`description`、`severity`、`related_fields`、`impact`、`code_snippet`、`fixed_code_snippet`

### 7.3 格式对齐要求（新增）

- `compliance_report.json` 使用 4 空格缩进（pretty JSON）。
- 顶层键顺序建议固定为：`project_name`、`difficulty_level`、`source_vuln_plan`、`generated_date`、`total_issues`、`summary`、`issues`。
- `summary` 下顺序建议为：`by_severity` 后 `by_category`。
- `issues[]` 中键顺序建议与示例一致，确保数据集格式统一。

### 7.4 输出示例

```json
{
    "project_name": "hard_example_project",
    "difficulty_level": "hard",
    "source_vuln_plan": "vuln_plan_hard_01.md",
    "generated_date": "2026-03-19",
    "total_issues": 8,
    "summary": {
        "by_severity": {
            "critical": 4,
            "high": 3,
            "medium": 1,
            "low": 0
        },
        "by_category": {
            "Sensitive Data Exposure": 1,
            "Data Minimization": 1,
            "Data Over-exposure": 1,
            "Missing Consent": 1,
            "Unauthorized Access": 1,
            "Data Lifecycle": 1,
            "SQL Injection": 1,
            "XSS": 0,
            "Sensitive Logging": 1,
            "Hardcoded Secrets": 0
        }
    },
    "issues": [
        {
            "issue_id": "DC-001",
            "location": {
                "file": "controllers/profileController.js",
                "line": 88,
                "class_or_function": "customerProfileDetail"
            },
            "category": "Unauthorized Access",
            "description": "Profile details are fetched by ID without verifying ownership or role scope.",
            "severity": "critical",
            "related_fields": ["profile_id"],
            "impact": "Attackers can access personal records of other users.",
            "code_snippet": "const profile = await CustomerProfile.findByPk(profileId);",
            "fixed_code_snippet": "const profile = await CustomerProfile.findOne({ where: { id: profileId, owner_id: req.user.id } });"
        }
    ]
}
```

---

## 8. 基于 `vuln_plan_hard_01` 的落地提示（示例）

若输入为 `vuln_plan_hard_01.md`，应至少满足：

- 模型不少于 4 个，且包含跨表关联与敏感字段（如证件、联系方式、支付信息、地址等）
- 接口不少于 6 个，覆盖查询、创建、更新、导出或检索等场景
- 页面不少于 3 个：输入页、列表页、详情页（可扩展审计/管理页）
- 问题覆盖至少 7 类，且包含：
  - critical：`Unauthorized Access`、`Sensitive Data Exposure`、`SQL Injection`（示例）
  - high：`Data Over-exposure`、`Data Minimization`、`Missing Consent`、`Sensitive Logging`（示例）
