# 漏洞说明文件（hard-10）

- 难度级别：hard
- 业务场景：敏感信息加密存储与密钥轮换平台
- 主漏洞：Cryptographic Key Management Failure（密钥硬编码且轮换失效，导致历史数据可被批量解密）
- 次要漏洞：
  - Predictable IV Usage（固定 IV 导致密文模式可分析）
  - Insecure Backup Handling（备份文件包含明文旧密钥）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：encrypted_id_card, encrypted_phone, master_key_id
  - 非必要字段：encrypt_display_style
- 预期接口与页面范围：
  - API：POST /api/crypto/encrypt, POST /api/crypto/rotate-key, GET /api/crypto/export-backup
  - 页面：key_management.ejs, crypto_audit.ejs
- 预期严重级别分布：
  - critical: 1（Cryptographic Key Management Failure）
  - high: 2（Predictable IV Usage, Insecure Backup Handling）
  - medium: 0
- 备注：本批次 hard 主漏洞类别唯一（Cryptographic Key Management Failure）。
