# 漏洞说明文件（medium-06）

- 难度级别：medium
- 业务场景：电子合同下载中心
- 主漏洞：IDOR in Document Download（修改 docId 可下载他人合同）
- 次要漏洞：
  - Missing Access Logging（下载行为缺少用户维度日志）
  - Export Without Masking（下载 PDF 未脱敏）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：contract_no, signer_id_card, signer_phone
  - 非必要字段：favorite_color
- 预期接口与页面范围：
  - API：GET /api/contracts/download/:docId, GET /api/contracts
  - 页面：contract_list.ejs, contract_preview.ejs
- 预期严重级别分布：
  - critical: 1（IDOR in Document Download）
  - high: 1（Export Without Masking）
  - medium: 1（Missing Access Logging）
- 备注：本批次 medium 主漏洞类别唯一（IDOR in Document Download）。
