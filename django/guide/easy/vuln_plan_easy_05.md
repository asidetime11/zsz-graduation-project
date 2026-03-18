# vuln_plan_easy_05

- 难度级别：easy
- 业务场景：快递取件记录查询系统（用户凭单号查询取件信息）
- 主漏洞：Unauthorized Access（通过记录 id 直接读取他人取件记录，无对象级权限校验，即 IDOR）
- 次要漏洞：
  - Sensitive Data Exposure（手机号、身份证、地址明文存储）
  - Data Over-exposure（详情接口返回完整字段含联系人信息）
- 涉及模型与字段：
  - ParcelRecord: name, phone, id_card, address, parcel_no, status, created_at
- API/页面：
  - POST /parcel/create/（登记取件信息）
  - GET /parcel/查询路径/（查询取件详情，直接按主键查询，无权限检查）
  - 页面：取件登记页（register.html）、取件详情页（detail.html）
- 严重级别分布：
  - critical: 2（Unauthorized Access, Sensitive Data Exposure）
  - high: 1（Data Over-exposure）
  - medium: 0
- 备注：主漏洞为 Unauthorized Access，本批次唯一。
