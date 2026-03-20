# 漏洞说明文件（easy-10）

- 难度级别：easy
- 业务场景：电商会员积分系统与第三方营销平台对接
- 主漏洞：Third-party Sharing Without Notice（向第三方共享用户手机号与消费偏好但未告知）
- 次要漏洞：
  - Missing Consent（无单独对外共享授权）
  - Purpose Limitation Violation（共享超出积分业务目的）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：user_id, phone, order_tags
  - 非必要字段：house_type, child_age
- 预期接口与页面范围：
  - API：POST /api/points/bind, POST /api/partner/push-profile
  - 页面：points_center.ejs, partner_sync.ejs
- 预期严重级别分布：
  - critical: 0
  - high: 2（Third-party Sharing Without Notice, Missing Consent）
  - medium: 1（Purpose Limitation Violation）
- 备注：本批次 easy 主漏洞类别唯一（Third-party Sharing Without Notice）。
