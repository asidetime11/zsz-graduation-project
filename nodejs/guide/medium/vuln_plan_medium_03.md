# 漏洞说明文件（medium-03）

- 难度级别：medium
- 业务场景：社区论坛实名发帖
- 主漏洞：Stored XSS（个人签名字段持久化脚本）
- 次要漏洞：
  - Missing CSP（页面未启用内容安全策略）
  - Sensitive Data Exposure（被窃取的会话可读取实名资料）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：real_name, id_card_masked, session_id
  - 非必要字段：zodiac
- 预期接口与页面范围：
  - API：POST /api/posts, POST /api/profile/signature
  - 页面：post_detail.ejs, profile_center.ejs
- 预期严重级别分布：
  - critical: 1（Stored XSS）
  - high: 1（Sensitive Data Exposure）
  - medium: 1（Missing CSP）
- 备注：本批次 medium 主漏洞类别唯一（Stored XSS）。
