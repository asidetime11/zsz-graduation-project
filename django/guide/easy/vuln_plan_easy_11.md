# vuln_plan_easy_11

- 难度级别：easy
- 业务场景：个人信息修改系统（用户在登录状态下修改姓名、手机号、邮箱等个人资料）
- 主漏洞：CSRF（跨站请求伪造）（修改个人信息的 POST 接口使用 @csrf_exempt 装饰器关闭了 CSRF 校验，攻击者可构造恶意页面诱导已登录用户在不知情的情况下提交修改请求，篡改其个人敏感信息）
- 次要漏洞：
  - Sensitive Data Exposure（手机号、身份证号明文存储，无加密）
  - Missing Consent（收集手机号、出生日期时无同意记录字段）
  - Data Over-exposure（用户信息查询接口返回全部字段，含身份证和手机号）
- 涉及模型与字段：
  - UserProfile: name, id_card, phone, email, birth_date, created_at
- API/页面：
  - POST /profile/update/（修改个人信息，@csrf_exempt 关闭 CSRF 保护）
  - GET /profile/（查看个人信息，返回全部字段）
  - 页面：个人信息展示页（profile.html）、信息修改页（edit_profile.html）
- 严重级别分布：
  - critical: 1（Sensitive Data Exposure）
  - high: 3（CSRF, Missing Consent, Data Over-exposure）
  - medium: 0
- 备注：主漏洞为 CSRF，前 10 个文件均未使用此类别，本批次新增第 11 个，与 easy_01~10 不重复。
