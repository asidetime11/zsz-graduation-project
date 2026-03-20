# 漏洞说明文件（hard-06）

- 难度级别：hard
- 业务场景：金融信贷审批工作流
- 主漏洞：Business Logic Bypass in Approval Workflow（通过跳过关键状态直接放款）
- 次要漏洞：
  - Missing Step Integrity Check（流程节点签名缺失）
  - Privilege Abuse（审核与放款权限未分离）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：loan_id, approval_state, amount, borrower_id_card
  - 非必要字段：borrower_social_note
- 预期接口与页面范围：
  - API：POST /api/loan/submit, POST /api/loan/approve, POST /api/loan/disburse
  - 页面：loan_workflow.ejs, approval_console.ejs
- 预期严重级别分布：
  - critical: 1（Business Logic Bypass in Approval Workflow）
  - high: 2（Missing Step Integrity Check, Privilege Abuse）
  - medium: 0
- 备注：本批次 hard 主漏洞类别唯一（Business Logic Bypass in Approval Workflow）。
