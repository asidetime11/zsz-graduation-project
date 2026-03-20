# 漏洞说明文件（hard-09）

- 难度级别：hard
- 业务场景：支付回调与账务入账系统
- 主漏洞：Webhook Replay Attack（签名时间窗校验缺失导致重复入账）
- 次要漏洞：
  - Weak Signature Verification（仅校验部分字段）
  - Missing Nonce Store（无随机串去重机制）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：payment_id, amount, signature, callback_timestamp
  - 非必要字段：payment_note_color
- 预期接口与页面范围：
  - API：POST /api/payment/webhook, GET /api/payment/reconcile
  - 页面：payment_log.ejs, reconcile.ejs
- 预期严重级别分布：
  - critical: 1（Webhook Replay Attack）
  - high: 1（Weak Signature Verification）
  - medium: 1（Missing Nonce Store）
- 备注：本批次 hard 主漏洞类别唯一（Webhook Replay Attack）。
