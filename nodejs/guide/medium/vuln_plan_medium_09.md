# 漏洞说明文件（medium-09）

- 难度级别：medium
- 业务场景：物流状态回调配置
- 主漏洞：SSRF via Callback URL（回调地址未校验可探测内网）
- 次要漏洞：
  - Sensitive Metadata Exposure（可访问云元数据接口）
  - Missing Egress Control（无出站访问限制）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：callback_url, access_token, order_id
  - 非必要字段：callback_alias
- 预期接口与页面范围：
  - API：POST /api/webhook/config, POST /api/webhook/test
  - 页面：webhook_settings.ejs
- 预期严重级别分布：
  - critical: 1（SSRF via Callback URL）
  - high: 1（Sensitive Metadata Exposure）
  - medium: 1（Missing Egress Control）
- 备注：本批次 medium 主漏洞类别唯一（SSRF via Callback URL）。
