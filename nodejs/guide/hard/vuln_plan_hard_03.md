# 漏洞说明文件（hard-03）

- 难度级别：hard
- 业务场景：用户隐私授权与撤回中心
- 主漏洞：Race Condition in Consent Revocation（撤回同意与数据处理任务并发导致撤回失效）
- 次要漏洞：
  - Eventual Consistency Gap（多节点同步延迟）
  - Missing Idempotency（重复请求覆盖状态）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：consent_status, revoke_time, processing_job_id
  - 非必要字段：consent_note
- 预期接口与页面范围：
  - API：POST /api/consent/revoke, POST /api/data/process
  - 页面：consent_center.ejs, processing_queue.ejs
- 预期严重级别分布：
  - critical: 1（Race Condition in Consent Revocation）
  - high: 1（Eventual Consistency Gap）
  - medium: 1（Missing Idempotency）
- 备注：本批次 hard 主漏洞类别唯一（Race Condition in Consent Revocation）。
