# openssf-structure-auditor 技能说明

一个 Codex 技能（skill），用于 **OpenSSF Best Practices 徽章审计**：从官方标准页抓取标准全文，逐条核对开源项目仓库中的源码、文档、CI 与治理证据，给出 `Met` / `Unmet` / `N/A` / `?` 判定，并自动产出一套可交付的审计文档。

> 典型场景：申请/复核 OpenSSF **Passing / Silver / Gold** 徽章；或对某个项目做一次“是否达标”的摸底审计。

## 一、这个技能能做什么

- 从 OpenSSF 标准页（如 `https://www.bestpractices.dev/en/projects/<id>/silver`）抓取全部标准条目，生成 `structure.md` 骨架，默认所有条目为 `[?]`，避免把页面上的历史自评当作当前事实。
- 按照技能内置的**证据优先级**逐条审计（仓库源码/官方文档 > CI/覆盖/发布/公告页面 > 搜索摘要），把每条标准判定为：
  - `[Met]`：证据充分覆盖每个实质性条款；
  - `[Unmet]`：证据证明实践缺失或不充分；
  - `[N/A]`：官方标准允许且触发条件不适用；
  - `[?]`：公开证据不足，不猜测。
- 为每条已判定条目补充 `[dependancy]:` 证据行；为每条 `[Unmet]` 补充 `[improvement]:` 提升路径（怎么改、改哪个文件）。
- 自动校验 `structure.md` 是否符合规则（状态枚举、证据行、Unmet 提升行、criterion id 唯一性等）。
- 与“真值夹具”对比，输出结构召回率、判定召回率、状态一致率、证据覆盖率等量化指标。
- 生成三份**状态明细文档**：`unmet.md`（未满足项）、`na.md`（不适用项）、`unknown.md`（待确认项）。
- 全程**保留用户已有内容**：不会覆盖已存在的 `structure.md`，审计时只改状态标记和追加证据/提升行。

## 二、输入（需要什么）

| 输入 | 是否必填 | 说明 |
|------|----------|------|
| OpenSSF 标准/项目页 URL | 必填 | 例如 `https://www.bestpractices.dev/en/projects/5301/silver`；网络不通时可保存 HTML 后传 `file:///...` |
| 被审计项目仓库 URL | 必填 | 主仓库，例如 `https://github.com/karmada-io/karmada` |
| 关联仓库（community/website/security） | 按需 | 文档、治理、安全材料分散在多个仓库时一并提供 |
| 目标 `structure.md` 路径 | 必填 | 输出/审计目标文件 |
| 真值文档（truth） | 可选 | 用于评估召回率/一致率 |
| 审计日期与基线 commit | 建议 | 时间窗口类标准需要截止日期与基线 |

## 三、输出（会得到什么）

| 产物 | 内容 |
|------|------|
| `structure.md` | 全部标准逐条判定：三级标题 `### [状态] [MUST/SHOULD]`、criterion id、证据行 `[dependancy]:`、Unmet 提升行 `[improvement]:` |
| `unmet.md` | 每条未满足项：不满足原因、提升路径、涉及文件、证据 |
| `na.md` | 每条不适用项：不适用原因、触发条件为何不成立、证据 |
| `unknown.md` | 每条待确认项：缺失的证据、下一步核实步骤、涉及文件/渠道 |
| 校验报告 | `validate_structure.py` 输出：criteria/decided/unknown/dependencies/improvements/errors/warnings |
| 评估指标 | `evaluate_against_truth.py` 输出 JSON：结构召回、判定召回、状态一致率、证据覆盖率 |
| 审计摘要 | （本仓库示例）`audit-summary.md`：总体结论、MUST/SHOULD 分布、达标判断、优先改进路线 |

## 四、环境准备

需要 Python 3，依赖见 `requirements.txt`（`requests`、`beautifulsoup4`、`PyYAML`）。建议在任务工作区创建独立虚拟环境，不要装进被审计项目的仓库：

```powershell
python -m venv .openssf-audit-venv
.\.openssf-audit-venv\Scripts\python.exe -m pip install -r <skill目录>\requirements.txt
```

Linux/macOS 用 `.openssf-audit-venv/bin/python`。

## 五、使用流程（与 SKILL.md 的 Step 0–7 对应）

1. **收集输入**：标准页 URL、仓库 URL、目标 `structure.md` 路径；已有文件先读全文并记录 SHA-256。
2. **安装依赖**：见上一节。
3. **生成骨架**（仅当目标文件不存在）：

   ```powershell
   python <skill目录>\scripts\fetch_structure.py `
     --url "<openssf项目页URL>" `
     --output "<目标>\structure.md"
   ```

   生成器默认全部置为 `[?]`；只有用户明确要求时才用 `--status-source page` 复制页面上的旧选择。
4. **查阅证据规则**：审计前先读 `references/audit-rules.md`（证据优先级、N/A 触发器、时间窗口、DCO/覆盖率/可重复构建等难点规则）。
5. **逐条审计**：按 `structure.md` 文档顺序，用 `rg`/`rg --files` 找治理、贡献、安全、发布、CI、测试、覆盖、依赖、签名、架构、路线图等证据；必要时查实时公开数据（版本、公告、覆盖徽章、签名 tag、官方页面）。每条 `[?]` 判定后替换状态并补 `[dependancy]`；`[Unmet]` 再补 `[improvement]`。
6. **校验**：

   ```powershell
   python <skill目录>\scripts\validate_structure.py "<目标>\structure.md"
   ```

   必须做到 `errors=0`。有真值夹具时再做评估：

   ```powershell
   python <skill目录>\scripts\evaluate_against_truth.py `
     --candidate "<structure.md>" `
     --truth "<truth-structure.md>"
   ```
7. **生成状态明细文档**：产出 `unmet.md`、`na.md`、`unknown.md`，条目数与 MUST/SHOULD 拆分必须与 `structure.md` 和审计摘要完全一致。
8. **判定完成**：校验 0 错误、证据覆盖率 100%、Unmet 提升行 100%、三份明细文档覆盖 100% 非 Met 条目、且满足召回率/一致率阈值（结构召回 ≥95%、判定召回 ≥80%、状态一致 ≥90%）。剩余的 `[?]` 必须逐一列出缺失证据与下一步核实步骤。

## 六、规则速查

- 状态标记：`[?]`（未核实）、`[Unmet]`（未实现）、`[Met]`（已实现）、`[N/A]`（无此功能或不需要考虑）。
- 级别标记：`[MUST]`（强制）、`[SHOULD]`（建议，含 SUGGESTED）。
- 每条**已判定**条目必须有一行 `[dependancy]: <判定理由 + 直接证据 URL/路径>`；`[?]` 不加。
- 每条 **`[Unmet]`** 还必须有一行 `[improvement]: <具体改进步骤 + 涉及文件>`；`Met`/`N/A`/`?` 不加。
- 生成器**拒绝覆盖**已存在的 `structure.md`（除非显式 `--force`，技能工作流禁止对用户文件使用）。
- 已有 `structure.md` 的正文、标题顺序、用户注释必须逐字保留，只允许改状态标记和追加证据/提升行。
- 时间窗口类标准（如近 12 个月漏洞、近 6 个月回归测试）要写清截止日期，私有记录需请维护者确认。
- 不能仅凭 OpenSSF 页面上的“已选择”就把条目填 `Met`。

## 七、目录结构

```text
openssf-structure-auditor/
|-- SKILL.md                  # 技能主指令：Step 0–7 完整工作流
|-- requirements.txt          # Python 依赖
|-- README.md                 # 本文件
|-- agents/
|   `-- openai.yaml           # UI 元数据与默认提示词
|-- references/
|   `-- audit-rules.md        # 证据优先级、难点规则、状态明细文档规则
|-- scripts/
|   |-- fetch_structure.py        # 抓取标准页并生成 structure.md 骨架
|   |-- validate_structure.py     # 校验状态/证据/Unmet 提升行
|   |-- evaluate_against_truth.py # 与真值夹具对比出量化指标
|   `-- test_skill.py             # 确定性回归测试
`-- assets/
    `-- structure-template.md # 样式/真值夹具（只作对照，禁止把其中的项目结论复制到其他项目）
```

## 八、常见问题

- **抓不到页面**：网络受限时用浏览器打开标准页并保存 HTML，把 `--url` 换成 `file:///...` 本地路径。
- **真值夹具是什么**：`assets/structure-template.md` 是技能自带的样式与判定真值，只用于学习风格和评估一致性，不要把里面的 Karmada 具体结论套到别的项目。
- **评估指标不达标**：先看是结构召回（条目没对齐）、判定召回（有判定缺失）还是状态一致率（某条判定与真值不同），回到对应条目补充证据或修正判定；`documentation_achievements` 这类随被审计仓库状态变化的条目允许与夹具不一致，但要在摘要中说明理由。
- **验收一个已有审计**：直接读 `structure.md` → 运行校验 → 运行评估 → 检查三份明细文档与摘要一致 → 输出结论。

## 九、本仓库的示例交付物

本仓库同时包含一次完整审计的示例输出（被审计对象 Karmada，目标 Silver 级）：

- `structure.md`：55 条标准逐条判定与证据
- `audit-summary.md`：审计摘要（总体结论、MUST/SHOULD 分布、一致性指标、优先改进路线）
- `unmet.md`：8 条未满足项明细
- `na.md`：3 条不适用项明细
- `unknown.md`：4 条待确认项明细
