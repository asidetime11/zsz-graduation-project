# 漏洞说明文件（easy-06）

- 难度级别：easy
- 业务场景：会员中心资料查询
- 主漏洞：Unauthorized Profile Access（通过自增 ID 可查看他人资料，基础 IDOR）
- 次要漏洞：
  - Logging Sensitive Data（访问日志记录完整手机号）
  - Missing Consent（资料共享给客服前无授权）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：user_id, phone, id_card, birthday
  - 非必要字段：favorite_brand
- 预期接口与页面范围：
  - API：GET /api/profile/:id, GET /api/admin/user/:id
  - 页面：profile.ejs, user_detail.ejs
- 预期严重级别分布：
  - critical: 1（Unauthorized Profile Access）
  - high: 1（Logging Sensitive Data）
  - medium: 1（Missing Consent）
- 备注：本批次 easy 主漏洞类别唯一（Unauthorized Profile Access）。
