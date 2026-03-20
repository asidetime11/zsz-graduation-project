# 漏洞说明文件（medium-02）

- 难度级别：medium
- 业务场景：商家入驻审核后台
- 主漏洞：SQL Injection（搜索接口拼接 SQL 可读取商家隐私数据）
- 次要漏洞：
  - Weak Error Handling（数据库报错回显）
  - Missing Rate Limit（无请求限速）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：merchant_name, legal_person_id, bank_account
  - 非必要字段：office_decoration_level
- 预期接口与页面范围：
  - API：GET /api/merchants/search, GET /api/merchants/:id
  - 页面：merchant_search.ejs, merchant_detail.ejs
- 预期严重级别分布：
  - critical: 1（SQL Injection）
  - high: 1（Weak Error Handling）
  - medium: 1（Missing Rate Limit）
- 备注：本批次 medium 主漏洞类别唯一（SQL Injection）。
