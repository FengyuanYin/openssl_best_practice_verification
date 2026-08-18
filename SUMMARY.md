# Karmada 是否符合 OpenSSF Best Practices Silver 水平 —— 审计总结

## 审计信息

- 审计日期：2026-08-18
- 审计对象：OpenSSF Best Practices 项目 [#5301（Silver 标准页）](https://www.bestpractices.dev/en/projects/5301/silver) 与仓库 [karmada-io/karmada](https://github.com/karmada-io/karmada)（含 [karmada-io/community](https://github.com/karmada-io/community) 配套文档）
- 审计基线 commit：`1819ee7bd392a7e2c750897b57b47acda4dc005c`（master，2026-08-18）
- 审计依据：仓库源码/文档/CI 配置、官方治理与安全文档、GitHub API（发布、安全公告）、Codecov、karmada.io 官方文档
- 详细逐条判定见 [structure.md](./structure.md)

## 总体结论

**当前 Karmada 尚不符合 Silver 水平。**

Silver 徽章要求所有 MUST 标准满足、SHOULD 标准满足或给出可接受的理由。本次审计共 55 条标准，判定结果如下：

| 判定 | 数量 | 说明 |
|------|------|------|
| Met | 40 | 已证实满足 |
| Unmet | 8 | 未满足或未充分满足 |
| N/A | 3 | 官方允许且触发条件不适用 |
| ? | 4 | 公开证据不足以判定，需进一步核实 |

## 直接阻碍 Silver 的 MUST 缺口（5 项）

1. **路线图（documentation_roadmap）**：`community/ROADMAP.md` 仅覆盖 2026 年 feature plan，以 2026-08-18 为审计日未覆盖之后至少一整年；Pending 列表无时间范围。
2. **安全需求文档（documentation_security）**：安全自评的 Non-goals 章节为空，Security Considerations 主要是部署加固建议，未明确说明用户“能与不能期待”的安全保障。
3. **可重复构建（build_repeatable）**：构建脚本将当前时间戳（BUILDDATE）注入二进制且无 `-trimpath`/可复现性校验，无法保证逐位一致。
4. **测试覆盖率（test_statement_coverage80）**：Codecov 当前 master 语句覆盖率约 **42%**，远低于 80% 阈值。
5. **保证论证（assurance_case）**：安全自评缺少完整的威胁模型、明确信任边界及“安全需求→设计原则→常见弱点→控制/测试证据”论证链。

## 尚待确认的项（?，4 项）

- **access_continuity**：单点失能时一周内接管 issue/发布所需的密钥、密码等安排属私有信息，需维护者确认。
- **accessibility_best_practices**：未发现 WCAG 审计或可访问性测试证据。
- **regression_tests_added50**：需对最近 6 个月 bug 修复做样本统计，公开信息不足。
- **input_validation**：虽有 CRD schema、validating webhook、结构化 CLI 解析，但无法从公开信息证明所有信任边界均使用 allowlist。

## SHOULD 缺口（3 项）

- **DCO（dco）**：CONTRIBUTING.md 与 PR 模板未要求 Signed-off-by，也无 DCO 检查（CNCF 历史文档虽提及，但当前贡献指引未落实）。
- **国际化（internationalization）**：karmadactl 仅少量命令使用 kubectl i18n 包装，无系统性 i18n/本地化框架。
- **签名版本标签（version_tags_signed）**：实测 v1.18.2 为 lightweight tag（tag 对象未签名，仅指向的 commit 由 GitHub 签名）。

## 已满足的亮点（摘录）

- 治理、成员职责、行为准则、bus factor（13 名多机构 active maintainers）均文档化。
- CI 在 push/PR 上执行 lint（golangci-lint 含 gosec/staticcheck）、单元测试与多版本 e2e。
- 依赖以 go.mod/SBOM 计算机可处理方式列出；Trivy 每周 + 合入后扫描，FOSSA 做许可证分析，Dependabot 自动更新。
- 漏洞响应流程完整（2 个工作日确认、CVE、私人分销商披露）；近 12 个月无新披露漏洞（N/A）。
- 发布自 v1.7 起 Cosign keyless 签名镜像，v1.10.3 起附 SLSA provenance 与 SBOM，并提供官方验证文档。
- 控制面部署默认 TLS 1.3、证书默认校验、seccomp/禁止提权等加固机制到位。

## 建议的下一步

1. 将 ROADMAP.md 更新为覆盖至少未来一年的、带时间范围的计划。
2. 补齐安全自评的 Non-goals，并形成正式的 assurance case（威胁模型 + 信任边界 + 安全论证链）。
3. 提升测试覆盖率至 80% 以上（当前约 42%）。
4. 移除构建时间戳或提供可复现构建流程与验证。
5. 在 CONTRIBUTING/PR 流程中引入 DCO 要求，并对发布 tag 使用签名 annotated tag。
6. 请维护者确认 access_continuity、私有漏洞记录等私有证据，并补充可访问性测试与近 6 个月回归测试样本统计。

> 说明：覆盖率、版本、公告等为 2026-08-18 快照；涉及私有记录的事项仍需维护者确认。逐条证据与 URL 见 structure.md。
