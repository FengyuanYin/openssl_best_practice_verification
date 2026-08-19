# N/A 明细（3 条）

## sites_password_security — MUST

- 要求：若项目站点存储外部用户密码，须使用带每用户盐的强迭代哈希。
- 为何 N/A：Karmada 项目网站（karmada.io）为 Docusaurus 静态文档站，无外部用户密码
  认证；代码托管、issue 与贡献身份认证由 GitHub 提供，OpenSSF 注明使用 GitHub 即满足
  本条，触发条件不适用。
- 触发条件缺失的证据：官网无登录/注册功能；仓库托管于 GitHub。

## vulnerability_report_credit — MUST

- 要求：对近 12 个月已解决漏洞的报告者致谢；若无已解决漏洞则 N/A。
- 为何 N/A：截至 2026-08-19，公开 Security Advisories 最近一次已解决漏洞发布于
  2025-01-03（CVE-2024-56513 / CVE-2024-56514），近 12 个月（2025-08-19 至
  2026-08-19）无已解决漏洞。
- 触发条件缺失的证据：GitHub Security Advisories 列表（最近 12 个月为空）；
  最终提交前建议由 Security Team 确认私有记录。

## dynamic_analysis_unsafe — MUST

- 要求：若交付软件含内存不安全语言（C/C++ 等），须例行使用动态工具检测内存问题。
- 为何 N/A：Karmada 交付软件以 Go 编写（其余为 Shell/Makefile/Dockerfile 等非内存
  不安全语言），构建显式 `CGO_ENABLED=0`，无 C/C++ 交付代码。
- 触发条件缺失的证据：`hack/build.sh` 中 `CGO_ENABLED=0`；仓库语言为 Go/Shell/
  JavaScript/Makefile/Dockerfile。
