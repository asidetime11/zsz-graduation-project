# Easy 级别：数据合规性问题代码生成指导（Django）

## 文档用途（IMPORTANT）

本文件 **不是给人类阅读的教程**，而是用于指导 AI 生成含数据合规问题的 Django 样本项目的执行规范。

生成时必须同时使用：

1. 对应 `vuln_plan_easy_xx.md`
2. 本 guide（复杂度、流程、输出格式）

冲突处理优先级：

- 漏洞场景、主漏洞、字段、接口：以 `vuln_plan` 为准
- 复杂度、工程结构、产出格式：以本 guide 为准

---

## AI 角色定义（Role）

- Django 后端工程师
- 数据合规风险引入者（intentionally）
- 数据合规审计分析器

目标：在可控范围内生成“带合规缺陷”的样本代码，用于数据集构建；**不是** 生成安全最佳实践项目。

---

## 0. 与 vuln_plan 的字段对齐规则（新增，必须执行）

每次开始生成前，先将 `vuln_plan_easy_xx.md` 解析为以下映射表：

| vuln_plan 字段 | 必做动作 | 输出落点 |
| --- | --- | --- |
| 难度级别 | 必须校验为 easy；不一致则停止生成 | `compliance_report.json -> difficulty_level` |
| 业务场景 | 作为页面文案、接口语义与示例数据来源 | `views.py` / 模板文件 |
| 主漏洞 | 必须 100% 出现且可定位到具体代码行 | `issues[]` 第一优先项 |
| 次要漏洞 | 至少落地 2 个（若计划中给出） | `issues[]` |
| 涉及模型与字段 | 字段名必须逐一出现，不得改名 | `models.py` |
| API/页面 | 路由、视图、模板必须全部落地 | `urls.py` / `views.py` / `templates/` |
| 严重级别分布 | `issues` 统计需严格匹配 | `summary.by_severity` |
| 备注 | 作为强约束执行，不得忽略 | 全项目 |

### 字段一致性硬性要求

- `vuln_plan` 中列出的模型名、字段名、接口路径、模板名必须原样出现。
- 不允许私自替换主漏洞类别。
- Easy 级别必须包含 **Sensitive Data Exposure（敏感数据明文存储）**。
- **生成的业务代码中严禁出现“说明漏洞/提示漏洞/标注漏洞类型”的注释**（包括中文与英文注释，如“故意不加密”“vulnerability here”“for demo insecure”等）。
- 可以保留正常业务说明注释，但不得直接或间接透露“这是漏洞点”。

---

## 1. Easy 复杂度约束

- **业务代码文件数**：建议 1-2 个核心文件（通常 `models.py` + `views.py`）
- **Model 数量**：1-2 个
- **View/API 数量**：1-2 个
- **数据库交互**：简单 CRUD
- **权限复杂度**：无需复杂鉴权
- **工程完整性**：必须是可运行 Django 项目，且包含完整 HTML 模板

> 说明：Django 工程基础文件（`settings.py`、`urls.py`、`manage.py` 等）不计入“业务代码文件数”。

---

## 2. 问题分布要求

### 严重性分布（默认）

| 等级 | 数量 | 说明 |
| --- | ---: | --- |
| critical | 1-2 | 例如敏感数据明文存储 |
| high | 1-2 | 例如数据最小化缺失、无同意机制 |
| medium | 0-1 | 可选 |

### 类别分布

- 至少 3 个不同类别问题
- 若 `vuln_plan` 已明确类别与数量，必须按计划覆盖

---

## 3. 标准生成流程（SOP）

1. 读取目标 `vuln_plan_easy_xx.md`
2. 提取并记录：场景、主/次漏洞、模型字段、接口与页面、严重级别分布
3. 初始化 Django 项目与 app
4. 按字段清单编写 `models.py`，确保主漏洞代码可定位
5. 按接口清单编写 `views.py` 与 `urls.py`
6. 创建模板（至少含表单页与列表页）
7. 执行迁移与运行校验
8. 生成 `compliance_report.json`
9. 对照清单做最终一致性检查

---

## 4. 命令行落地建议（可复现）

建议顺序：

1. 创建并进入目录
2. 初始化 Django 项目（含 `manage.py`）
3. 创建业务 app（如 `core`）
4. 在 `settings.py` 注册 app
5. 执行 `makemigrations` / `migrate`
6. 启动服务验证

参考命令：

```bash
mkdir easy_example && cd easy_example
django-admin startproject project .
python manage.py startapp core
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

补充要求：

- 目录编号与计划编号一致（如 `easy/example11` 对应 `vuln_plan_easy_11.md`）
- 若 `vuln_plan` 指定字段/接口，代码必须逐项实现

---

## 5. 目录与文件最小清单

至少包含：

- `manage.py`
- `project/settings.py`
- `project/urls.py`
- `core/models.py`
- `core/views.py`
- `core/urls.py`
- `templates/register.html`
- `templates/user_list.html`
- `compliance_report.json`

---

## 6. 快速检查清单

生成完成后必须全部满足：

- [ ] 主漏洞已在代码中出现，且能定位文件与行号
- [ ] 次要漏洞数量与类别满足 `vuln_plan`
- [ ] 模型字段与 `vuln_plan` 一致（名称完全匹配）
- [ ] 路由与页面完整可访问（注册页、列表页）
- [ ] 数据库迁移成功
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
  "project_name": "easy_example_project",
  "difficulty_level": "easy",
  "source_vuln_plan": "vuln_plan_easy_01.md",
  "generated_date": "2026-03-18",
  "total_issues": 3,
  "summary": {
    "by_severity": {
      "critical": 1,
      "high": 2,
      "medium": 0,
      "low": 0
    },
    "by_category": {
      "Sensitive Data Exposure": 1,
      "Data Minimization": 1,
      "Missing Consent": 1,
      "Data Over-exposure": 0,
      "Unauthorized Access": 0,
      "Data Lifecycle": 0,
      "SQL Injection": 0,
      "XSS": 0,
      "Sensitive Logging": 0,
      "Hardcoded Secrets": 0
    }
  },
  "issues": [
    {
      "issue_id": "DC-001",
      "location": {
        "file": "core/models.py",
        "line": 8,
        "class_or_function": "UserProfile"
      },
      "category": "Sensitive Data Exposure",
      "description": "ID card, phone and bank account are stored in plaintext.",
      "severity": "critical",
      "related_fields": ["id_card", "phone", "bank_account"],
      "impact": "Sensitive personal data can be directly leaked if database is exposed.",
      "code_snippet": "id_card = models.CharField(max_length=20)\\nphone = models.CharField(max_length=20)\\nbank_account = models.CharField(max_length=50)",
      "fixed_code_snippet": "id_card = encrypt_field(id_card); phone = encrypt_field(phone); bank_account = mask_value(bank_account)"
    }
  ]
}
```

---

## 8. 基于 `vuln_plan_easy_01` 的落地提示（示例）

若输入为 `vuln_plan_easy_01.md`，应至少满足：

- 模型 `UserProfile` 含字段：`name`, `id_card`, `phone`, `bank_account`, `family_members`, `created_at`
- 接口：`POST /register/` 与 `GET /users/`
- 页面：`register.html` 与 `user_list.html`
- 问题：
  - critical：`Sensitive Data Exposure`
  - high：`Data Minimization`、`Missing Consent`

