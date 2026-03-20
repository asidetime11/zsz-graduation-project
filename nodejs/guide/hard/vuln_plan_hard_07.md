# 漏洞说明文件（hard-07）

- 难度级别：hard
- 业务场景：GraphQL 数据聚合网关
- 主漏洞：GraphQL Authorization Bypass via Nested Query（嵌套查询绕过字段级鉴权）
- 次要漏洞：
  - Over-fetching Sensitive Data（一次查询返回过多隐私字段）
  - Introspection Exposure（生产环境开放 schema 枚举）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：salary, id_card, medical_record, permission_scope
  - 非必要字段：avatar_border
- 预期接口与页面范围：
  - API：POST /graphql
  - 页面：graphql_playground.ejs, user_data_view.ejs
- 预期严重级别分布：
  - critical: 1（GraphQL Authorization Bypass via Nested Query）
  - high: 1（Over-fetching Sensitive Data）
  - medium: 1（Introspection Exposure）
- 备注：本批次 hard 主漏洞类别唯一（GraphQL Authorization Bypass via Nested Query）。
