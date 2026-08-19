# Karmada OpenSSF Best Practices Silver 达标情况审计摘要

## 审计元数据

- 审计日期：2026-08-19
- 审计对象：https://github.com/karmada-io/karmada（含 community、website 关联仓库）
- 被审提交（浅克隆 HEAD）：
  - karmada：master `1819ee7bd392a7e2c750897b57b47acda4dc005c`（2026-08-18）
  - community：main `9edead7bbc78ad0a16a6231c5218db5114b33ae6`（2026-08-17）
  - website：main `747f80c48c9a8784ec679cf88ae15b935c7824a9`（2026-07-20）
- 标准来源：OpenSSF Best Practices Silver 标准页（55 条，含 Passing 级全部标准）
  https://www.bestpractices.dev/en/criteria/1
- 官方项目页：#5301，徽章级别 passing（2022-01-21 获得，从未失去），Silver 尚未达成
  https://www.bestpractices.dev/en/projects/5301

## 总览

| 状态 | MUST | SHOULD | 合计 |
|------|------|--------|------|
| Met  | 33   | 7      | 40   |
| Unmet | 5   | 3      | 8    |
| N/A  | 3    | 0      | 3    |
| ?    | 3    | 1      | 4    |
| 合计 | 44   | 11     | 55   |

已判定 51 条、未决 4 条。Silver 徽章要求所有 MUST 均达标，且满足 SHOULD 的比例要求；
当前存在 5 条 MUST 未达标（Unmet）与 3 条 MUST 待核（?），因此**尚未达到 Silver 标准**，
需要优先消除 MUST 缺口。

## 与技能真值夹具的一致性

- 结构召回：100%（55/55）
- 判定召回：100%（51/51）
- 状态一致率：98.0%（50/51）
- 证据覆盖：100%（51/51）

唯一差异为 `documentation_achievements`：真值夹具为 Unmet，本次审计按被审提交 README
中已展示并超链接 OpenSSF Best Practices 徽章的事实判定为 Met。

## MUST 未达标（阻塞 Silver）

1. `documentation_roadmap`：路线图仅覆盖 2026 年，不足审计日起一整年，且未明确排除范围。
2. `documentation_security`：security requirements 不完整，self-assessment 的 Non-goals 为空。
3. `build_repeatable`：构建注入时间戳，无法 bit-for-bit 复现。
4. `test_statement_coverage80`：Codecov 语句覆盖率 42%，低于 80%。
5. `assurance_case`：缺少威胁模型、信任边界、安全设计原则与常见弱点论证。

## SHOULD 未达标

- `dco`：未在贡献指南中采用并落实 DCO/CLA。
- `internationalization`：核心软件/karmadactl 缺少 i18n 框架。
- `version_tags_signed`：发布 tag 为 lightweight tag，未签名。

## 待确认（?）

- `access_continuity`：需维护者确认密钥/域名/发布凭据的冗余与法律连续性。
- `accessibility_best_practices`：需 WCAG/屏幕阅读器审计证据。
- `regression_tests_added50`：需近 6 个月 bug-fix 回归测试采样与比例。
- `input_validation`：需覆盖全部信任边界的 allowlist 证据。

## 优先改进路线（按对 Silver 的阻塞程度排序）

1. 覆盖率：将语句覆盖率提升至 ≥80% 并加 CI 门禁（改 `Makefile`/`ci.yml`，补单测）。
2. 路线图：`community/ROADMAP.md` 更新为覆盖未来至少一整年、含排除范围。
3. 安全文档：补全 `self-assessment.md` Non-goals，新增 `assurance-case.md`。
4. 可复现构建：用 `SOURCE_DATE_EPOCH` 固定 buildDate（改 `hack/util.sh`/`hack/build.sh`）。
5. DCO：在 `CONTRIBUTING.md`/PR 模板采纳 DCO 并加 CI 检查。
6. 签名 tag：发布流程创建签名 annotated tag 并文档化验证。
7. i18n：为 karmadactl 等用户可见输出建立本地化框架。

## 明细文档

- [unmet.md](unmet.md)：8 条未达标项的原因、改进路径与涉及文件
- [na.md](na.md)：3 条不适用项的依据
- [unknown.md](unknown.md)：4 条待确认项缺失的证据与下一步
- [structure.md](structure.md)：55 条标准逐条判定与证据
