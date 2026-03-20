# 漏洞说明文件（hard-02）

- 难度级别：hard
- 业务场景：低代码表单平台的脚本扩展功能
- 主漏洞：Unsafe Dynamic Code Execution（用户脚本经 eval/vm 执行导致 RCE 风险）
- 次要漏洞：
  - Sandbox Escape Misconfiguration（隔离上下文可访问 process）
  - Sensitive Data Exposure（环境变量包含密钥可被读取）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：api_secret, db_password, user_submission
  - 非必要字段：form_theme
- 预期接口与页面范围：
  - API：POST /api/forms/run-script, POST /api/forms/test
  - 页面：script_editor.ejs, execution_log.ejs
- 预期严重级别分布：
  - critical: 1（Unsafe Dynamic Code Execution）
  - high: 2（Sandbox Escape Misconfiguration, Sensitive Data Exposure）
  - medium: 0
- 备注：本批次 hard 主漏洞类别唯一（Unsafe Dynamic Code Execution）。
