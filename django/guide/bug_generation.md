# Django 合规样本说明文件生成要求（面向 AI）

## 目标

本文件只定义一件事：

生成“不同难度的漏洞说明文件”（不生成项目代码）。

---

## 仅生成漏洞说明文件

### AI 必须执行

- 分别为 easy、medium、hard 生成漏洞说明文件。
- 当前步骤严禁创建/修改项目代码文件（如 models.py、views.py、urls.py、settings.py、模板等）。
- 只输出“说明文件”，用于后续项目生成输入。

### 输出目录与命名

- guide/easy: vuln_plan_easy_xx.md
- guide/medium: vuln_plan_medium_xx.md
- guide/hard: vuln_plan_hard_xx.md

### 每份漏洞说明文件最低内容

- 难度级别
- 业务场景
- 主漏洞（同一难度内不可重复）
- 次要漏洞（2~3 个）
- 关键数据字段（敏感字段/非必要字段）
- 预期接口与页面范围
- 预期严重级别分布

### 去重规则（强制）

- 同一难度的同一批次里，主漏洞类别不得重复。
- 若某漏洞已作为主漏洞出现，其他文件中只能作为次要漏洞。

### 示例文件(vuln_plan_easy_01)

- 难度级别：easy
- 业务场景：用户注册系统（收集姓名、证件号、手机号、银行卡）
- 主漏洞：Sensitive Data Exposure（身份证号、手机号、银行卡号明文存储，无任何加密）
- 次要漏洞：
  - Data Minimization（收集与注册无关的家庭成员数量字段）
  - Missing Consent（无同意字段，无法追踪用户是否同意数据采集）
- 涉及模型与字段：
  - UserProfile: name, id_card, phone, bank_account, family_members, created_at
- API/页面：
  - POST /register/（用户注册提交）
  - GET /users/（用户列表查询）
  - 页面：注册表单页（register.html）、用户列表页（user_list.html）
- 严重级别分布：
  - critical: 1（Sensitive Data Exposure）
  - high: 2（Data Minimization, Missing Consent）
  - medium: 0
- 备注：主漏洞为 Sensitive Data Exposure，本批次唯一，其他项目此类别只能作为次要漏洞出现
