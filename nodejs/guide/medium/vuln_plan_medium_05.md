# 漏洞说明文件（medium-05）

- 难度级别：medium
- 业务场景：员工证件上传与归档
- 主漏洞：Insecure File Upload（可上传伪装脚本文件并被静态目录访问）
- 次要漏洞：
  - No Antivirus Scan（无恶意文件检测）
  - Sensitive Data Exposure（上传目录可目录遍历浏览）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：id_card_front, id_card_back, labor_contract
  - 非必要字段：avatar_frame_style
- 预期接口与页面范围：
  - API：POST /api/files/upload, GET /uploads/:name
  - 页面：file_upload.ejs, file_archive.ejs
- 预期严重级别分布：
  - critical: 1（Insecure File Upload）
  - high: 1（Sensitive Data Exposure）
  - medium: 1（No Antivirus Scan）
- 备注：本批次 medium 主漏洞类别唯一（Insecure File Upload）。
