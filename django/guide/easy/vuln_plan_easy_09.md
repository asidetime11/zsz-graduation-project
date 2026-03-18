# vuln_plan_easy_09

- 难度级别：easy
- 业务场景：优惠券领取系统（用户填写信息领取优惠券，后台可查看领取记录）
- 主漏洞：Data Lifecycle（无任何数据删除或过期清理策略，用户数据和过期优惠券记录无限期保留）
- 次要漏洞：
  - Sensitive Data Exposure（手机号、身份证号明文存储）
  - Data Minimization（额外收集职业、收入水平等与领取优惠券无关的字段）
- 涉及模型与字段：
  - CouponUser: name, phone, id_card, occupation, income_level, coupon_code, claimed_at
- API/页面：
  - POST /coupon/claim/（领取优惠券，提交个人信息）
  - GET /coupons/（后台记录列表，无分页无删除）
  - 页面：领取表单页（claim.html）、后台记录页（record_list.html）
- 严重级别分布：
  - critical: 1（Sensitive Data Exposure）
  - high: 1（Data Minimization）
  - medium: 1（Data Lifecycle - 无清除机制）
- 备注：主漏洞为 Data Lifecycle，本批次唯一。
