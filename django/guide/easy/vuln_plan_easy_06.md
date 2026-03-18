# vuln_plan_easy_06

- 难度级别：easy
- 业务场景：图书馆借阅查询系统（读者和管理员可搜索借阅记录）
- 主漏洞：SQL Injection（搜索接口直接将用户输入拼接进 SQL 语句，未使用 ORM 参数化）
- 次要漏洞：
  - Sensitive Data Exposure（借阅人身份证号明文存储）
  - Data Over-exposure（搜索结果返回全部字段含证件信息）
- 涉及模型与字段：
  - BorrowRecord: name, id_card, phone, book_title, borrow_date, return_date, created_at
- API/页面：
  - GET /search/?keyword=（搜索借阅记录，拼接 SQL）
  - POST /borrow/（登记借阅信息）
  - 页面：借阅搜索页（search.html）、借阅登记页（borrow.html）
- 严重级别分布：
  - critical: 2（SQL Injection, Sensitive Data Exposure）
  - high: 1（Data Over-exposure）
  - medium: 0
- 备注：主漏洞为 SQL Injection，本批次唯一。
