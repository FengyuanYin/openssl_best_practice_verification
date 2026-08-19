# Unmet 明细（8 条）

## dco — SHOULD

- 要求：项目应具备法律机制（DCO/CLA 等），使非平凡贡献者声明其有权贡献。
- 现状：karmada 主仓库 `CONTRIBUTING.md` 未采用或链接 DCO/CLA，未要求 `git commit -s`
  /`Signed-off-by`，CI 无 DCO 检查；cncf_process 文档虽有 DCO 表述但未落实到贡献指南。
- 改进路径：在 `CONTRIBUTING.md` 与 PR 模板中采纳 DCO（链接
  https://developercertificate.org/），要求提交加 Signed-off-by 并解释其含义，
  启用 DCO 机器人（如 probot/dco）在 CI 强制校验。
- 涉及文件：`karmada/CONTRIBUTING.md`、`.github/PULL_REQUEST_TEMPLATE`（如存在）、
  `.github/workflows/ci.yml`

## documentation_roadmap — MUST

- 要求：必须有公开路线图，说明未来至少一年内打算做与不做什么。
- 现状：`community/ROADMAP.md` 仅描述“2026 feature plan”，以 2026-08-19 为审计日
  不足一整年，且未明确时间窗与排除范围。
- 改进路径：将 `community/ROADMAP.md` 更新为覆盖审计日起至少一整年（至 2027-08 及以后）
  的分阶段计划，写明每项时间窗、优先级与明确排除的范围。
- 涉及文件：`community/ROADMAP.md`

## documentation_security — MUST

- 要求：必须文档化用户能期待与不能期待的软件安全保障（security requirements）。
- 现状：security self-assessment 列出 Goals 与安全功能，但 Non-goals 为空；
  官网 Security Considerations 以部署建议为主，未形成 guarantees/non-guarantees 文档。
- 改进路径：补全 `community/security-team/assessments/self-assessment.md` 的 Non-goals，
  新增 security requirements 文档（保证与非保证、信任边界、适用版本），并在
  `SECURITY.md` 与官网安全章节公开链接。
- 涉及文件：`community/security-team/assessments/self-assessment.md`、
  `community/security-team/SECURITY.md`、website 安全文档

## internationalization — SHOULD

- 要求：软件应国际化以支持本地化。
- 现状：官网有中文等本地化内容，但核心软件与 `karmadactl` 面向用户的输出无公开
  i18n 框架或资源目录。
- 改进路径：为 `karmadactl` 与核心面向用户输出建立系统化 i18n/本地化框架与资源目录，
  覆盖全部用户可见字符串并提供本地化入口。
- 涉及文件：`karmada/pkg/karmadactl`（用户输出）、`karmada/pkg/util`（如需）

## build_repeatable — MUST

- 要求：从源码生成产物的过程必须可重复且 bit-for-bit 一致。
- 现状：`hack/util.sh` 的 `version_ldflags` 注入 `BUILDDATE=$(date -u ...)` 时间戳，
  两次构建产物不同；未使用 `SOURCE_DATE_EPOCH`，无可复现构建文档。
- 改进路径：以 `SOURCE_DATE_EPOCH` 固定 buildDate（或从版本/commit 派生），记录
  `go build` 参数，发布可复现构建说明，并用同一提交两次构建比对验证一致性。
- 涉及文件：`karmada/hack/util.sh`、`karmada/hack/build.sh`、`karmada/Makefile`

## test_statement_coverage80 — MUST

- 要求：FLOSS 自动化测试套件须提供至少 80% 语句覆盖率。
- 现状：Codecov 徽章显示 master 分支覆盖率为 42%（2026-08-19 抓取），低于 80%。
- 改进路径：为主要包（`pkg/`、`cmd/`、`operator/`）补充单元测试，将语句覆盖率提升至
  ≥80%；在 CI 加覆盖率门禁（如 Codecov threshold），并在 README 公示覆盖率。
- 涉及文件：`karmada/Makefile`（test target）、`karmada/.github/workflows/ci.yml`、
  `karmada/.codecov.yml`

## version_tags_signed — SHOULD

- 要求：重要版本 tag 应加密签名并可验证。
- 现状：对最新发布 tag `v1.18.2` 执行 `git cat-file -t` 返回 `commit`，为 lightweight
  tag；仓库无 tag 级 GPG/SSH/Sigstore 签名验证说明。
- 改进路径：发布流程为重要版本创建签名 annotated tag（GPG/SSH/Sigstore），在发布文档
  提供 `git tag -v` 或对应验证方法，确保 tag 对象本身可验证。
- 涉及文件：`.github/workflows/release.yml`、发布文档

## assurance_case — MUST

- 要求：必须提供 assurance case，含威胁模型、信任边界、安全设计原则论证与常见弱点
  应对论证。
- 现状：self-assessment 有 actors/goals/安全功能清单与 OSTIF 审计，但缺少明确威胁模型、
  完整信任边界、设计原则论证与 OWASP/CWE 弱点映射；Non-goals 为空。
- 改进路径：在 `community/security-team/assessments/` 新增 `assurance-case.md`：
  威胁模型、逐项信任边界、安全 claim → 设计原则 → 常见弱点 → 控制/测试证据的论证结构，
  经 Security Team 评审后以公开 URL 作为依据。
- 涉及文件：`community/security-team/assessments/assurance-case.md`（新建）、
  `community/security-team/assessments/self-assessment.md`
