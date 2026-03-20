# 漏洞说明文件（hard-04）

- 难度级别：hard
- 业务场景：多模块 Node.js 企业平台构建流水线
- 主漏洞：Dependency Confusion / Supply Chain Attack（内部包名被公共仓库同名包劫持）
- 次要漏洞：
  - Inadequate Dependency Pinning（未锁定精确版本）
  - Missing Artifact Verification（构建产物无签名校验）
- 关键数据字段（敏感字段/非必要字段）：
  - 敏感字段：npm_token, ci_secret, build_artifact
  - 非必要字段：build_theme
- 预期接口与页面范围：
  - API：POST /api/build/trigger, GET /api/build/history
  - 页面：build_pipeline.ejs, dependency_dashboard.ejs
- 预期严重级别分布：
  - critical: 1（Dependency Confusion / Supply Chain Attack）
  - high: 2（Inadequate Dependency Pinning, Missing Artifact Verification）
  - medium: 0
- 备注：本批次 hard 主漏洞类别唯一（Dependency Confusion / Supply Chain Attack）。
