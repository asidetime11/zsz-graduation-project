# Medium 级别：数据合规性问题代码生成指导（Spring Boot）

## 文档用途（IMPORTANT）

本文件不是给人类阅读的教程，而是用于指导 AI 生成含数据合规问题的 Spring Boot 样本项目的执行规范。

生成时必须同时使用：

1. 对应 `vuln_plan_medium_xx.md`
2. 本 guide（复杂度、流程、输出格式）

冲突处理优先级：

- 漏洞场景、主漏洞、字段、接口：以 `vuln_plan` 为准
- 复杂度、工程结构、产出格式：以本 guide 为准

---

## AI 角色定义（Role）

- Spring Boot 后端工程师
- 数据合规风险引入者（intentionally）
- 数据合规审计分析器

目标：在可控范围内生成“带合规缺陷”的样本代码，用于数据集构建；不是生成安全最佳实践项目。

---

## 0. 与 vuln_plan 的字段对齐规则（必须执行）

每次开始生成前，先将 `vuln_plan_medium_xx.md` 解析为以下映射表：

| vuln_plan 字段 | 必做动作 | 输出落点 |
| --- | --- | --- |
| 难度级别 | 必须校验为 medium；不一致则停止生成 | `compliance_report.json -> difficulty_level` |
| 业务场景 | 作为页面文案、接口语义与示例数据来源 | `controller` / 模板文件 |
| 主漏洞 | 必须 100% 出现且可定位到具体代码行 | `issues[]` 第一优先项 |
| 次要漏洞 | 至少落地 4 个（若计划中给出） | `issues[]` |
| 涉及模型与字段 | 字段名必须逐一出现，不得改名 | `entity` |
| API/页面 | 路由、控制器、模板必须全部落地 | `controller` / `templates` |
| 严重级别分布 | `issues` 统计需严格匹配 | `summary.by_severity` |
| 备注 | 作为强约束执行，不得忽略 | 全项目 |

### 字段一致性硬性要求

- `vuln_plan` 中列出的模型名、字段名、接口路径、模板名必须原样出现。
- 不允许私自替换主漏洞类别。
- Medium 级别必须包含 **Sensitive Data Exposure（敏感数据明文存储）**（若在计划中作为次要漏洞也必须落地）。
- 生成的业务代码中严禁出现“说明漏洞/提示漏洞/标注漏洞类型”的注释。
- 可以保留正常业务说明注释，但不得直接或间接透露“这是漏洞点”。

---

## 1. Medium 复杂度约束

- 业务代码文件数：建议 2-3 个核心文件（通常 `entity` + `controller` + `service`）
- Model 数量：2-3 个（至少 1 个关联关系）
- View/API 数量：2-3 个
- 数据库交互：中等复杂 CRUD（条件过滤、分页、关联查询）
- 权限复杂度：允许出现简单鉴权与对象级权限缺失
- 工程完整性：必须是可运行 Spring Boot 项目，且包含完整 HTML 模板

---

## 2. 问题分布要求

### 严重性分布（默认）

| 等级 | 数量 | 说明 |
| --- | ---: | --- |
| critical | 2-3 | 例如越权访问、敏感数据明文、SQL 注入 |
| high | 2-4 | 例如过度暴露、数据最小化、缺失同意、敏感日志 |
| medium | 0-1 | 可选 |

### 类别分布

- 至少 5 个不同类别问题
- 若 `vuln_plan` 已明确类别与数量，必须按计划覆盖

---

## 3. 标准生成流程（SOP）

1. 读取目标 `vuln_plan_medium_xx.md`
2. 提取并记录：场景、主/次漏洞、模型字段、接口与页面、严重级别分布
3. 初始化 Spring Boot 项目与目录结构
4. 按字段清单编写 `entity`，确保主漏洞代码可定位
5. 按接口清单编写 `controller` 与 `service`
6. 增加 `dto/mapper`（至少 1 个 all fields 返回场景）
7. 创建模板（至少含输入页与列表/详情页）
8. 启动服务与路径校验
9. 生成 `compliance_report.json`
10. 对照清单做最终一致性检查

---

## 4. 命令行落地建议（可复现）

建议顺序：

1. 创建并进入目录
2. 初始化 Spring Boot 工程
3. 安装依赖
4. 创建业务目录
5. 启动服务验证

补充要求：

- 目录编号与计划编号一致（如 `medium/example11` 对应 `vuln_plan_medium_11.md`）
- 若 `vuln_plan` 指定字段/接口，代码必须逐项实现

---

## 5. 目录与文件最小清单

至少包含：

- `pom.xml`（或 `build.gradle`）
- `src/main/java/.../controller/*.java`
- `src/main/java/.../service/*.java`
- `src/main/java/.../entity/*.java`
- `src/main/java/.../repository/*.java`
- `src/main/java/.../dto/*.java`（或 mapper）
- `src/main/resources/templates/` 下至少 2 个页面
- `src/main/resources/application.yml`
- `compliance_report.json`

---

## 6. 快速检查清单

- [ ] 主漏洞已在代码中出现，且能定位文件与行号
- [ ] 次要漏洞数量与类别满足 `vuln_plan`
- [ ] 模型字段与 `vuln_plan` 一致（名称完全匹配）
- [ ] 路由与页面完整可访问（输入页、列表/详情页）
- [ ] 至少 1 处关联模型 + 1 处中等复杂查询
- [ ] `compliance_report.json` 统计与实际问题一致

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

补充硬性约束：

- `issues[].fixed_code_snippet` 必须填写“修复后的代码片段”（可直接替换的代码内容），不得填写自然语言解释、修复思路或步骤说明。

### 7.2 统计一致性规则

- `total_issues = len(issues)`
- `summary.by_severity` 必须等于 `issues[].severity` 实际计数
- `summary.by_category` 必须等于 `issues[].category` 实际计数
- 每个 issue 必须包含可追溯定位：`file` + `line` + `class_or_function`
- 每个 issue 必须包含：`issue_id`、`location`、`category`、`description`、`severity`、`related_fields`、`impact`、`code_snippet`、`fixed_code_snippet`（且为代码片段，不得为自然语言）

### 7.3 格式对齐要求

- `compliance_report.json` 使用 4 空格缩进（pretty JSON）。
- 顶层键顺序建议固定为：`project_name`、`difficulty_level`、`source_vuln_plan`、`generated_date`、`total_issues`、`summary`、`issues`。
- `summary` 下顺序建议为：`by_severity` 后 `by_category`。
- `issues[]` 中键顺序建议与示例一致，确保数据集格式统一。
