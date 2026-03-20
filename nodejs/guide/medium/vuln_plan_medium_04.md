# 漏洞说明文件（medium-04）

- 难度级别：medium
- 业务场景：在线投保系统
- 主漏洞：CSRF on Sensitive Operations（保单受益人修改接口缺少 CSRF 防护）
- 次要漏洞：
  - Missing Re-authentication（高危操作无需二次验证）
  - Insecure Cookie Flags（Cookie 未设置 SameSite）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：policy_no, beneficiary_name, beneficiary_id_card
  - 非必要字段：beneficiary_hobby
- 预期接口与页面范围：
  - API：POST /api/policy/update-beneficiary
  - 页面：policy_edit.ejs, beneficiary_manage.ejs
- 预期严重级别分布：
  - critical: 1（CSRF on Sensitive Operations）
  - high: 1（Missing Re-authentication）
  - medium: 1（Insecure Cookie Flags）
- 备注：本批次 medium 主漏洞类别唯一（CSRF on Sensitive Operations）。
