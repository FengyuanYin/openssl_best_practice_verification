# 待确认明细（4 条）

## access_continuity — MUST

- 要求：任何一人失能时，项目须能在一周内继续管理 issue/PR/发布。
- 缺失证据：公开材料显示 13 名多组织 maintainer，但未公开 DNS 域名、容器镜像仓库、
  发布凭据、私密通信渠道的冗余控制与法律连续性安排（lockbox/密钥托管等）。
- 下一步：请维护者确认关键资产（域名 karmada.io、Docker Hub/OCI registry、GitHub
  release secrets、CNCF 资源）的冗余持有人与接手机制，并提供可核验证据。

## accessibility_best_practices — SHOULD

- 要求：项目站点与成果遵循可访问性最佳实践（合理范围内）。
- 缺失证据：网站基于 Docusaurus，但未见 WCAG 审计、对比度/键盘操作/屏幕阅读器测试
  等证据；CLI 产品无专门可访问性测试记录。
- 下一步：对 karmada.io 与 Dashboard 执行 WCAG 2.x 自查或第三方审计，记录关键页面
  的键盘与屏幕阅读器测试结果；CLI 说明其天然可访问性即可。

## regression_tests_added50 — MUST

- 要求：近 6 个月修复的 bug 中至少 50% 添加了回归测试。
- 缺失证据：无公开的 6 个月 bug-fix 采样统计（分子=添加回归测试的修复数，
  分母=已修复 bug 数）。
- 下一步：请维护者或 CI 数据提供近 6 个月（2026-02-19 至 2026-08-19）修复 PR 清单与
  其中附带回归测试的 PR 数，确认比例 ≥50%。

## input_validation — MUST

- 要求：对所有潜在不可信输入按 allowlist 校验并拒绝无效输入。
- 缺失证据：已有 CRD schema、validating webhook、CLI flag 等校验，但缺少覆盖全部
  信任边界（API、webhook、resource interpreter、kubeconfig、gRPC/HTTP 端点、外部
  搜索后端等）的输入清单与 allowlist 证据。
- 下一步：在 assurance case 中逐项列出不可信输入、允许格式、校验代码、拒绝路径与
  测试，经评审后转为 Met。
