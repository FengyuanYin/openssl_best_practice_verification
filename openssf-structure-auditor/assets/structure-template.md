# Symbols
## 项目是否具备选项
[?] 不确定
[Unmet] 未实现
[Met] 已实现
[N/A] 没有这个功能or不需要考虑这一点

## 项目是否必须满足这一条要求
[SHOULD] 不强制要求
[MUST] 强制要求

## 做出选项的依据
[dependancy]: 做出选项的依据，用于已经做出选择的问卷内容
三级标题[A][B] A最多有四种选择([?], [Unmet], [Met], [N/A]) [?]代表还没去核实项目应该选哪个选项，如果把[?]替换成其他选项，需要在三级标题这一章节的最后一行补充[dependancy]，描述清楚做出选择的依据。


# Prerequisites
### [Met] [MUST]
The project MUST achieve a passing level badge. [achieve_passing] 

[dependancy]: OpenSSF Best Practices 项目 #5301 显示 Karmada 已于 2022-01-21 获得并保持 Passing badge。https://www.bestpractices.dev/en/projects/5301

# Basic project website content
### [Met] [MUST]
The information on how to contribute MUST include the requirements for acceptable contributions (e.g., a reference to any required coding standard). (URL required) [contribution_requirements] [Met] [MUST]

[dependancy]: Karmada CONTRIBUTING.md 说明了 PR 流程、提交前验证和测试要求，并在 Code Review 章节要求遵循 Go coding guidelines。https://github.com/karmada-io/karmada/blob/master/CONTRIBUTING.md

# Project oversight

### [Unmet] [SHOULD]
The project SHOULD have a legal mechanism where all developers of non-trivial amounts of project software assert that they are legally authorized to make these contributions. The most common and easily-implemented approach for doing this is by using a Developer Certificate of Origin (DCO), where users add "signed-off-by" in their commits and the project links to the DCO website. However, this MAY be implemented as a Contributor License Agreement (CLA), or other legal mechanism. (URL required) [dco] 
The DCO is the recommended mechanism because it's easy to implement, tracked in the source code, and git directly supports a "signed-off" feature using "commit -s". To be most effective it is best if the project documentation explains what "signed-off" means for that project. A CLA is a legal agreement that defines the terms under which intellectual works have been licensed to an organization or project. A contributor assignment agreement (CAA) is a legal agreement that transfers rights in an intellectual work to another party; projects are not required to have CAAs, since having CAA increases the risk that potential contributors will not contribute, especially if the receiver is a for-profit organization. The Apache Software Foundation CLAs (the individual contributor license and the corporate CLA) are examples of CLAs, for projects which determine that the risks of these kinds of CLAs to the project are less than their benefits.
 项目必须明确采用 DCO 作为法律机制, 需要解释 “Signed-off-by” 的含义, 标准针对的是 “non-trivial amounts of project software”，即非少量代码贡献。项目可以规定所有提交都必须签署，也可以只对达到一定规模的贡献要求签署。这一点最好在项目文档中说明清楚。 如果项目：1.在 README、CONTRIBUTING 或治理文档中明确说明采用 DCO,2.提供了 DCO 链接或说明, 3.要求贡献者使用 git commit -s 或手动添加 Signed-off-by；并解释了签署的法律含义；那么就可以认为已经达到了该要求。

[dependancy]: Karmada 当前的 CONTRIBUTING.md 没有采用 DCO、链接 Developer Certificate of Origin 或要求贡献者使用 `git commit -s`/`Signed-off-by`，因此不能填 Met。https://github.com/karmada-io/karmada/blob/master/CONTRIBUTING.md
[improvement]: 在 CONTRIBUTING.md 与 PR 模板中明确采用 DCO，链接 Developer Certificate of Origin，要求提交使用 `git commit -s` 添加 Signed-off-by，并解释其法律含义。


### [Met] [MUST]
The project MUST clearly define and document its project governance model (the way it makes decisions, including key roles). (URL required) [governance] 
There needs to be some well-established documented way to make decisions and resolve disputes. In small projects, this may be as simple as "the project owner and lead makes all final decisions". There are various governance models, including benevolent dictator and formal meritocracy; for more details, see Governance models. Both centralized (e.g., single-maintainer) and decentralized (e.g., group maintainers) approaches have been successfully used in projects. The governance information does not need to document the possibility of creating a project fork, since that is always possible for FLOSS projects.
开源项目必须清晰定义并书面记录其治理模型，也就是项目如何做决策、有哪些关键角色，并且要提供可访问的 URL。 项目需要一份公开的治理文档，说明“谁说了算、怎么决策、争议怎么解决”；小项目可以从简，但必须存在并清晰可查。

[dependancy]: Karmada 的 GOVERNANCE.md 公开说明了治理价值、成员体系、maintainer 治理机构、路线图变更、投票事项、表决比例以及治理章程修改流程。https://github.com/karmada-io/community/blob/main/GOVERNANCE.md


### [Met] [MUST]
The project MUST adopt a code of conduct and post it in a standard location. (URL required) [code_of_conduct] 

[dependancy]: Karmada 在仓库根目录的标准位置公开了 CODE_OF_CONDUCT.md。https://github.com/karmada-io/karmada/blob/master/CODE_OF_CONDUCT.md

### [Met] [MUST]
The project MUST clearly define and publicly document the key roles in the project and their responsibilities, including any tasks those roles must perform. It MUST be clear who has which role(s), though this might not be documented in the same way. (URL required) [roles_responsibilities] 
The documentation for governance and roles and responsibilities may be in one place.
治理模型说明“项目怎么决策”，角色职责说明“谁在具体执行和管理”。两者可以写在同一个文档里，也可以分开，但都必须公开可访问，所以有 URL required 的要求。

[dependancy]: community-membership.md 定义了 Member、Reviewer、Approver、Maintainer 的要求、职责和权限；MAINTAINERS.md、REVIEWERS.md、APPROVERS.md 公开了具体人员。https://github.com/karmada-io/community/blob/main/community-membership.md ; https://github.com/karmada-io/community/blob/main/MAINTAINERS.md ; https://github.com/karmada-io/community/blob/main/REVIEWERS.md ; https://github.com/karmada-io/community/blob/main/APPROVERS.md

### [?] [MUST]
The project MUST be able to continue with minimal interruption if any one person dies, is incapacitated, or is otherwise unable or unwilling to continue support of the project. In particular, the project MUST be able to create and close issues, accept proposed changes, and release versions of software, within a week of confirmation of the loss of support from any one individual. This MAY be done by ensuring someone else has any necessary keys, passwords, and legal rights to continue the project. Individuals who run a FLOSS project MAY do this by providing keys in a lockbox and a will providing any needed legal rights (e.g., for DNS names). (URL required) 
项目必须提前做好“万一核心人物不在了”的准备，确保其他人能在一周内接手，继续管理 issue、合并代码和发布版本。

### [Met] [SHOULD]
The project SHOULD have a "bus factor" of 2 or more. (URL required) [bus_factor] 
A "bus factor" (aka "truck factor") is the minimum number of project members that have to suddenly disappear from a project ("hit by a bus") before the project stalls due to lack of knowledgeable or competent personnel. The truck-factor tool can estimate this for projects on GitHub. For more information, see Assessing the Bus Factor of Git Repositories by Cosentino et al.
项目避免过度依赖单个人，确保至少有两个或以上的人了解项目关键知识、拥有必要权限，从而降低项目因成员突然离开而停滞的风险。

[dependancy]: Karmada 的公开名单包含 13 名 active maintainers，来自多个组织；项目还公开了多名 reviewer 和 approver，足以证明 bus factor 不低于 2。https://github.com/karmada-io/community/blob/main/MAINTAINERS.md ; https://github.com/karmada-io/community/blob/main/APPROVERS.md


# Documentation

### [Unmet] [MUST]
The project MUST have a documented roadmap that describes what the project intends to do and not do for at least the next year. (URL required) [documentation_roadmap] 
The project might not achieve the roadmap, and that's fine; the purpose of the roadmap is to help potential users and contributors understand the intended direction of the project. It need not be detailed.
项目必须有一份公开的、书面化的路线图（roadmap），用来说明项目在未来至少一年内打算做什么、不打算做什么。

[dependancy]: Karmada 已公开 ROADMAP.md，但当前内容是“2026 feature plan”。以 2026-08-18 为核验时间，它没有覆盖之后至少完整一年的计划，而且 Pending 列表不能替代带时间范围的未来一年路线图，因此当前不能填 Met。https://github.com/karmada-io/community/blob/main/ROADMAP.md
[improvement]: 将 community/ROADMAP.md 更新为覆盖审计日后至少一整年、带明确时间范围的计划，并写明不打算做的范围。


### [Met] [MUST]
The project MUST include documentation of the architecture (aka high-level design) of the software produced by the project. If the project does not produce software, select "not applicable" (N/A). (URL required) [documentation_architecture] 
A software architecture explains a program's fundamental structures, i.e., the program's major components, the relationships among them, and the key properties of these components and relationships.
项目会产出软件，就必须提供一份软件架构文档，用来说明软件的高层设计。如果项目不产出软件，则可以选择“不适用”（N/A）。

[dependancy]: Karmada 公开了总体架构图和安全自评；安全自评说明 Host Cluster、Karmada control plane、Member Cluster、主要组件以及 Push/Pull 模式下组件之间的关系和数据流。https://github.com/karmada-io/karmada/blob/master/docs/images/architecture.png ; https://github.com/karmada-io/community/blob/main/security-team/assessments/self-assessment.md


### [Unmet] [MUST]
The project MUST document what the user can and cannot expect in terms of security from the software produced by the project (its "security requirements"). (URL required) [documentation_security] 
These are the security requirements that the software is intended to meet.
项目产出软件，就必须公开文档化该软件的安全需求，明确说明用户在使用该软件时可以期待哪些安全保障，不能期待哪些安全保障。

[dependancy]: Karmada 的 Security Self-Assessment 已列出若干 Security Goals 和安全功能，但其中 Non-goals 章节为空，没有完整说明用户不能期待的安全保证；现有 Security Considerations 主要是部署建议，尚不能完全替代明确的 security requirements 与边界说明。https://github.com/karmada-io/community/blob/main/security-team/assessments/self-assessment.md ; https://karmada.io/docs/administrator/security/security-considerations/
[improvement]: 补全 security-team/assessments/self-assessment.md 的 Non-goals，并新增明确的 security requirements 文档，说明用户能与不能期待的保证。

### [Met] [MUST]
The project MUST provide a "quick start" guide for new users to help them quickly do something with the software. (URL required) [documentation_quick_start] 
The idea is to show users how to get started and make the software do anything at all. This is critically important for potential users to get started.
项目必须提供一份“快速入门”指南，帮助新用户快速上手，让软件至少能跑起来、做出一点事情。

[dependancy]: Karmada 官网的 Installation 文档提供环境准备、安装方式和可执行步骤，新用户可以使用 karmadactl、Helm 或 Operator 快速安装并开始使用 Karmada。https://karmada.io/docs/installation/

### [Met] [MUST]
The project MUST make an effort to keep the documentation consistent with the current version of the project results (including software produced by the project). Any known documentation defects making it inconsistent MUST be fixed. If the documentation is generally current, but erroneously includes some older information that is no longer true, just treat that as a defect, then track and fix as usual. [documentation_current] 
The documentation MAY include information about differences or changes between versions of the software and/or link to older versions of the documentation. The intent of this criterion is that an effort is made to keep the documentation consistent, not that the documentation must be perfect.
项目不能只写文档，还要持续维护文档，确保它跟得上项目发展。发现文档过时或错误时，要当作缺陷来跟踪和修复。同时，不要求文档完美，但必须体现出持续维护的努力。

[dependancy]: Karmada 官网提供按版本维护的文档以及 next 文档，当前版本文档与发布版本同步；文档源码公开维护，文档问题和修改通过 GitHub issue/PR 跟踪。https://karmada.io/docs/ ; https://github.com/karmada-io/website

### [Unmet] [MUST]
The project repository front page and/or website MUST identify and hyperlink to any achievements, including this best practices badge, within 48 hours of public recognition that the achievement has been attained. (URL required) [documentation_achievements] 
An achievement is any set of external criteria that the project has specifically worked to meet, including some badges. This information does not need to be on the project website front page. A project using GitHub can put achievements on the repository front page by adding them to the README file.
项目一旦获得某项公开认可（尤其是徽章），必须在两天内把该成就的标识和链接放到仓库首页或网站上，让访问者可以看到并点击验证。

[dependancy]: Karmada 已获得 OpenSSF Best Practices Passing，但主仓库 README 当前展示 OpenSSF Scorecard、Codecov 等徽章，没有展示并链接项目 #5301 的 OpenSSF Best Practices badge，因此当前不能填 Met。https://github.com/karmada-io/karmada/blob/master/README.md ; https://www.bestpractices.dev/en/projects/5301
[improvement]: 在仓库 README 或官网首页增加并超链接 OpenSSF Best Practices badge（项目 #5301）。

# Accessibility and internationalization

### [?] [SHOULD]
The project (both project sites and project results) SHOULD follow accessibility best practices so that persons with disabilities can still participate in the project and use the project results where it is reasonable to do so. [accessibility_best_practices] 
For web applications, see the Web Content Accessibility Guidelines (WCAG 2.0) and its supporting document Understanding WCAG 2.0; see also W3C accessibility information. For GUI applications, consider using the environment-specific accessibility guidelines (such as Gnome, KDE, XFCE, Android, iOS, Mac, and Windows). Some TUI applications (e.g. `ncurses` programs) can do certain things to make themselves more accessible (such as `alpine`'s `force-arrow-cursor` setting). Most command-line applications are fairly accessible as-is. This criterion is often N/A, e.g., for program libraries. Here are some examples of actions to take or issues to consider:
Provide text alternatives for any non-text content so that it can be changed into other forms people need, such as large print, braille, speech, symbols or simpler language ( WCAG 2.0 guideline 1.1)
Color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element. ( WCAG 2.0 guideline 1.4.1)
The visual presentation of text and images of text has a contrast ratio of at least 4.5:1, except for large text, incidental text, and logotypes ( WCAG 2.0 guideline 1.4.3)
Make all functionality available from a keyboard (WCAG guideline 2.1)
A GUI or web-based project SHOULD test with at least one screen-reader on the target platform(s) (e.g. NVDA, Jaws, or WindowEyes on Windows; VoiceOver on Mac & iOS; Orca on Linux/BSD; TalkBack on Android). TUI programs MAY work to reduce overdraw to prevent redundant reading by screen-readers.
鼓励项目在合理的范围内提升可访问性，让残障人士也能顺利使用项目成果和参与项目。具体做法取决于项目类型：Web 应用参考 WCAG，GUI 应用参考平台指南，TUI 应用可做一些优化，命令行应用通常天然可访问，而程序库则通常不适用。原文还给出了一些具体的 WCAG 指南作为示例，包括文本替代、不用颜色作为唯一信息手段、对比度要求和键盘操作等。

### [Unmet] [SHOULD]
The software produced by the project SHOULD be internationalized to enable easy localization for the target audience's culture, region, or language. If internationalization (i18n) does not apply (e.g., the software doesn't generate text intended for end-users and doesn't sort human-readable text), select "not applicable" (N/A). [internationalization] 
Localization "refers to the adaptation of a product, application or document content to meet the language, cultural and other requirements of a specific target market (a locale)." Internationalization is the "design and development of a product, application or document content that enables easy localization for target audiences that vary in culture, region, or language." (See W3C's "Localization vs. Internationalization".) Software meets this criterion simply by being internationalized. No localization for another specific language is required, since once software has been internationalized it's possible for others to work on localization.
目产出的软件应当进行国际化（i18n），以便后续能轻松地针对不同文化、地区或语言进行本地化。这是一个推荐性要求（SHOULD），而不是强制性的“MUST”。

[dependancy]: Karmada 官网文档已有中文等本地化内容，但 Karmada 核心软件和 karmadactl 面向用户输出的文本没有公开、系统化的 i18n/localization 框架或资源目录，因此“软件 produced by the project 已国际化”尚不能填 Met。https://github.com/karmada-io/karmada ; https://karmada.io/zh/docs/
[improvement]: 为 karmadactl 与核心面向用户输出建立系统化 i18n/本地化框架和资源目录，覆盖全部面向用户文本。

### [N/A] [MUST]
If the project sites (website, repository, and download URLs) store passwords for authentication of external users, the passwords MUST be stored as iterated hashes with a per-user salt by using a key stretching (iterated) algorithm (e.g., Argon2id, Bcrypt, Scrypt, or PBKDF2). If the project sites do not store passwords for this purpose, select "not applicable" (N/A). [sites_password_security] 
Note that the use of GitHub meets this criterion. This criterion only applies to passwords used for authentication of external users into the project sites (aka inbound authentication). If the project sites must log in to other sites (aka outbound authentication), they may need to store authorization tokens for that purpose differently (since storing a hash would be useless). This applies criterion crypto_password_storage to the project sites, similar to sites_https.
项目网站自己管理用户密码，就必须用带独立盐值的强迭代哈希算法来存储，不能存明文或弱哈希。如果项目不自己存密码，这条就不适用。

[dependancy]: Karmada 的公开项目网站是文档站点，代码托管、issue 和贡献身份认证由 GitHub 提供；Karmada 项目站点本身不建立外部用户密码数据库。OpenSSF 条目说明使用 GitHub 满足该条件，因此应选择 N/A。https://karmada.io/ ; https://github.com/karmada-io/karmada



# Change Control - Previous versions

### [Met] [MUST]
The project MUST maintain the most often used older versions of the product or provide an upgrade path to newer versions. If the upgrade path is difficult, the project MUST document how to perform the upgrade (e.g., the interfaces that have changed and detailed suggested steps to help upgrade). [maintenance_or_update]
项目不能只顾着开发新版本，而把现有用户抛在身后。它要么继续支持最常用的旧版本，要么给出一条清晰、有文档支持的升级路径，确保用户能够平滑过渡。

[dependancy]: Karmada Security Policy 明确维护最近三个 minor release branch，并说明适用修复会回移到受支持版本；官网同时提供版本化升级文档。https://github.com/karmada-io/community/blob/main/security-team/SECURITY.md ; https://karmada.io/docs/administrator/upgrading/

#  Reporting

## Bug-reporting process

### [MET] [MUST]
The project MUST use an issue tracker for tracking individual issues. 
[dependancy]: https://github.com/karmada-io/karmada/milestones


## Vulnerability report process

### [N/A] [MUST]

The project MUST give credit to the reporter(s) of all vulnerability reports resolved in the last 12 months, except for the reporter(s) who request anonymity. If there have been no vulnerabilities resolved in the last 12 months, select "not applicable" (N/A). (URL required) 
项目必须对过去 12 个月内已解决的所有漏洞报告者给予公开致谢，除非报告者本人要求匿名。如果项目在过去 12 个月内没有解决任何漏洞，则可以选择“不适用”（N/A）。

[dependancy]: 截至 2026-08-18，Karmada 公开 Security Advisories 中最近发布的已修复漏洞为 2025-01-03，已超过 12 个月；历史 advisory 也包含 reporter credits。公开记录中最近 12 个月没有已解决漏洞，因此本次可选 N/A，但最终提交前应由 Security Team 再确认私密记录。https://github.com/karmada-io/karmada/security/advisories

### [Met] [MUST]
The project MUST have a documented process for responding to vulnerability reports. (URL required) 
项目必须有一份文档化的流程，说明如何响应漏洞报告。该流程必须公开可访问，因此要求提供 URL。

[dependancy]: Karmada Security Policy 和 Security Release Process 公开说明了私密报告渠道、2 个工作日确认、漏洞分级、修复、embargo、CVE、发布以及公开沟通流程。https://github.com/karmada-io/community/blob/main/security-team/SECURITY.md ; https://github.com/karmada-io/community/blob/main/security-team/security-release-process.md

# Quality

## Coding standards

### [Met] [MUST]
The project MUST identify the specific coding style guides for the primary languages it uses, and require that contributions generally comply with it. (URL required) [coding_standards] 
In most cases this is done by referring to some existing style guide(s), possibly listing differences. These style guides can include ways to improve readability and ways to reduce the likelihood of defects (including vulnerabilities). Many programming languages have one or more widely-used style guides. Examples of style guides include Google's style guides and SEI CERT Coding Standards.
项目不能对代码风格没有要求，必须明确告诉贡献者代码应该写成什么样，并且要有公开文档说明遵循哪套标准。
通过指定风格指南并持续执行，项目能提升代码质量、一致性和安全性，也让新贡献者更容易融入。

[dependancy]: Karmada CONTRIBUTING.md 明确要求贡献遵循 Go Code Review Comments，并要求提交前运行 `make verify` 和 `make test`。https://github.com/karmada-io/karmada/blob/master/CONTRIBUTING.md ; https://go.dev/wiki/CodeReviewComments

### [Met] [MUST]
The project MUST automatically enforce its selected coding style(s) if there is at least one FLOSS tool that can do so in the selected language(s). [coding_standards_enforced] 
This MAY be implemented using static analysis tool(s) and/or by forcing the code through code reformatters. In many cases the tool configuration is included in the project's repository (since different projects may choose different configurations). Projects MAY allow style exceptions (and typically will); where exceptions occur, they MUST be rare and documented in the code at their locations, so that these exceptions can be reviewed and so that tools can automatically handle them in the future. Examples of such tools include ESLint (JavaScript), Rubocop (Ruby), and devtools check (R).
项目必须自动强制执行其选定的编码风格，前提是对于项目使用的编程语言，至少存在一个开源（FLOSS）工具能够自动检查或格式化代码风格。这是一个强制性要求（MUST），但有条件限制。
```
1. 必须自动执行编码风格
项目不能只靠人工提醒或代码审查来保证风格一致，而是要用工具自动检查或自动格式化。

条件：仅当所选语言存在至少一个可用的开源工具时，这项要求才强制适用。
如果某种语言根本没有合适的开源风格检查工具，那么项目可以豁免自动执行，但仍应尽量通过人工方式遵循风格指南。

2. 实现方式
可以通过以下一种或多种方式实现：

静态分析工具：例如 ESLint、Rubocop、Pylint 等，在代码提交或 CI 流程中检查风格问题。

代码格式化工具：例如 Prettier、Black、clang-format 等，直接自动重排代码格式，强制统一风格。

很多情况下，工具的具体配置（如 .eslintrc、.rubocop.yml、pyproject.toml）会包含在项目仓库中，确保所有贡献者使用相同的规则。

3. 允许例外，但必须罕见且记录
项目可以允许少数地方不遵循风格规则（例如某些特殊代码布局更清晰）。但例外必须满足：

罕见：不能到处都有例外，否则自动执行就失去意义。

在代码位置文档化：在例外发生的具体代码处添加注释，说明为什么这里例外。例如使用 // eslint-disable-next-line 并附上原因。

便于审查和未来处理：文档化的例外可以让代码审查者理解原因，也方便将来工具改进后自动处理这些位置。

4. 为什么要自动执行
保证一致性：人工检查容易遗漏，自动工具能持续、可靠地发现风格违规。

减少审查负担：代码审查可以专注于逻辑和设计，而不是纠结于空格、缩进等风格问题。

提升代码质量：许多风格规则本身有助于减少缺陷（如禁止未使用的变量、强制使用严格模式等）。

降低贡献门槛：清晰的自动检查让新贡献者能快速知道自己的代码是否符合要求。

5. 与上一条要求的关系
上一条（coding_standards）要求项目指定编码风格指南。

这一条（coding_standards_enforced）要求项目自动强制这些风格。

两者配合：先确定风格标准，再用工具落地执行。

6. 实际做法举例
在 CI 流程中加入 npm run lint 或 flake8 检查，未通过则不允许合并。

使用 pre-commit 钩子，在提交前自动运行格式化和检查工具。

在 README 或贡献指南中说明：“所有代码必须通过 ESLint 检查，配置见 .eslintrc，允许少量例外，但需在代码中注释原因。”
```

[dependancy]: Karmada 的 `.golangci.yml` 配置 gosec、Staticcheck、gofmt、goimports、gci 等检查；`hack/verify-staticcheck.sh` 执行 `golangci-lint run`，GitHub Actions 在 push 和 pull request 中自动运行该脚本，失败会使 CI job 失败。https://github.com/karmada-io/karmada/blob/master/.golangci.yml ; https://github.com/karmada-io/karmada/blob/master/hack/verify-staticcheck.sh ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci.yml


## Working build system

### [Met] [MUST]
Build systems for native binaries MUST honor the relevant compiler and linker (environment) variables passed in to them (e.g., CC, CFLAGS, CXX, CXXFLAGS, and LDFLAGS) and pass them to compiler and linker invocations. A build system MAY extend them with additional flags; it MUST NOT simply replace provided values with its own. If no native binaries are being generated, select "not applicable" (N/A). [build_standard_variables]

项目生成原生 Go 二进制，因此需要尊重与 Go 构建有关的环境变量。Karmada 的 `hack/build.sh` 接受 `BUILD_PLATFORMS`，并将目标拆分为 `GOOS` 和 `GOARCH` 传给 `go build`；调用方传入的 `LDFLAGS` 也会保留，只是在其前面追加版本信息，而不是直接覆盖。Go 工具链自身还会读取 `GOFLAGS` 等标准变量。由于发布构建显式设置 `CGO_ENABLED=0`，C/C++ 的 `CC`、`CFLAGS`、`CXXFLAGS` 对该构建不适用。基于这些实现，可以选择 `Met`。

[dependancy]: https://github.com/karmada-io/karmada/blob/master/hack/build.sh

### [Met] [SHOULD]
The build and installation system SHOULD preserve debugging information if it is requested in the relevant flags (e.g., "install -s" is not used). If there is no build or installation system, select "not applicable" (N/A). [build_preserve_debug]

项目的构建脚本没有默认给 Go linker 增加 `-s` 或 `-w`，因此不会主动删除符号表和 DWARF 调试信息。同时，脚本允许调用方通过 `LDFLAGS` 追加所需链接参数。项目既没有在安装时执行类似 `strip` 的操作，也没有强制替换调用方的调试设置，因此可以选择 `Met`。

[dependancy]: https://github.com/karmada-io/karmada/blob/master/hack/build.sh ; https://github.com/karmada-io/karmada/blob/master/hack/release.sh

### [Met] [MUST]
The build system for the software produced by the project MUST NOT recursively build subdirectories if there are cross-dependencies in the subdirectories. If there is no build or installation system, select "not applicable" (N/A). [build_non_recursive]

这一要求用于避免递归进入各子目录分别构建时，因为跨目录依赖关系不可见而产生错误或不稳定结果。Karmada 没有通过递归 `make` 逐目录构建 Go 源码；顶层构建脚本直接把完整 Go package 路径交给 `go build`，由 Go module 和 Go 构建图统一解析跨 package 依赖。因此不存在该标准所反对的递归子目录构建问题，可以选择 `Met`。

[dependancy]: https://github.com/karmada-io/karmada/blob/master/Makefile ; https://github.com/karmada-io/karmada/blob/master/hack/build.sh ; https://github.com/karmada-io/karmada/blob/master/go.mod

### [Unmet] [MUST]
The project MUST be able to repeat the process of generating information from source files and get exactly the same bit-for-bit result. If no building occurs, select "not applicable" (N/A). [build_repeatable]

该条要求同一份源码和同一组构建输入重复执行生成过程时，输出必须逐位完全相同。Karmada 当前的 `util::version_ldflags` 在每次构建时执行 `date -u`，把当前时间写入二进制的 `buildDate`。即使源码 commit 完全相同，只要构建时间不同，二进制内容也会不同；tar/gzip 制品的时间戳和文件元数据也需要进一步固定。因此当前不能选择 `Met`。

修复时可以让 `buildDate` 来自固定的 `SOURCE_DATE_EPOCH` 或 commit 时间，为 `go build` 使用稳定的 `-trimpath`/build-id 策略，并固定 tar 文件顺序、mtime、owner、group 与 gzip 时间戳。最后应在两个干净目录中构建同一 commit 并比较 SHA-256，把该验证加入 CI。

[dependancy]: https://github.com/karmada-io/karmada/blob/master/hack/util.sh ; https://github.com/karmada-io/karmada/blob/master/hack/release.sh
[improvement]: 让 buildDate 来自固定的 SOURCE_DATE_EPOCH 或 commit 时间，为 `go build` 使用 `-trimpath`/稳定 build-id，固定 tar/gzip 元数据，并在 CI 中对同一 commit 做两次构建的 SHA-256 对比。

## Installation system

### [Met] [MUST]
The project MUST provide a way to easily install and uninstall the software produced by the project using a commonly-used convention. [installation_common]

Karmada 提供多种常见安装方式，包括 Helm chart、`karmadactl init`、Karmada Operator 和二进制安装脚本；Helm 与 Operator 也提供标准的卸载/删除方式。用户无需手工复制大量内部文件即可完成安装和卸载，因此可以选择 `Met`。

[dependancy]: https://karmada.io/docs/installation/ ; https://github.com/karmada-io/karmada/tree/master/charts ; https://github.com/karmada-io/karmada/blob/master/hack/install-cli.sh

### [Met] [MUST]
The installation system for end-users MUST honor standard conventions for selecting the location where built artifacts are written to at installation time. For example, if it installs files on a POSIX system it MUST honor the DESTDIR environment variable. If there is no installation system or no standard convention, select "not applicable" (N/A). [installation_standard_variables]

Karmada 的 CLI 安装脚本使用 `INSTALL_LOCATION` 选择安装目录，默认值为 `/usr/local/bin`，用户可以通过环境变量改到任意目标目录。Kubernetes 控制面资源通过 Helm、Operator 或 Kubernetes API 安装，不对应传统 POSIX 文件树的 `DESTDIR` 语义。对于实际写入本地文件系统的 CLI 安装，项目已经提供等效的标准位置变量，因此可以选择 `Met`。

[dependancy]: https://github.com/karmada-io/karmada/blob/master/hack/install-cli.sh

### [Met] [MUST]
The project MUST provide a way for potential developers to quickly install all the project results and support environment necessary to make changes, including the tests and test environment. This MUST be performed with a commonly-used convention. [installation_development_quick]

项目提供 `Makefile` 作为统一开发入口，贡献者可使用 `make verify` 和 `make test` 执行提交前检查与单元测试。`hack/local-up-karmada.sh` 可以建立本地 Karmada 控制面和 E2E 环境，CI 也公开展示了相同环境的搭建及测试方法。贡献指南给出了 fork、提交 PR、验证和测试步骤，符合使用常见工具快速建立开发环境的要求。

[dependancy]: https://github.com/karmada-io/karmada/blob/master/CONTRIBUTING.md ; https://github.com/karmada-io/karmada/blob/master/Makefile ; https://github.com/karmada-io/karmada/blob/master/hack/local-up-karmada.sh ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci.yml

## Externally-maintained components

### [Met] [MUST]
The project MUST list external dependencies in a computer-processable way. [external_dependencies]

Karmada 的 Go 依赖记录在可机读的 `go.mod` 和 `go.sum` 中，同时提交 `vendor/modules.txt`。Helm chart 的依赖通过 `Chart.yaml` 和 `Chart.lock` 记录，GitHub Actions 依赖也以 workflow YAML 形式声明并固定到 commit。工具可以直接解析这些文件获得依赖名称、版本和校验信息，因此可以选择 `Met`。

[dependancy]: https://github.com/karmada-io/karmada/blob/master/go.mod ; https://github.com/karmada-io/karmada/blob/master/go.sum ; https://github.com/karmada-io/karmada/blob/master/vendor/modules.txt ; https://github.com/karmada-io/karmada/tree/master/charts

### [Met] [MUST]
Projects MUST monitor or periodically check their external dependencies, including convenience copies, to detect known vulnerabilities, and fix exploitable vulnerabilities or verify them as unexploitable. [dependency_monitoring]

项目配置 Dependabot 定期检查 Go modules、GitHub Actions、Docker 和多个受支持 release branch 的依赖更新。Trivy 在 pull request 合并后及定时 workflow 中扫描发布镜像，将结果以 SARIF 上传到 GitHub Security；发布流程还生成 SPDX SBOM。community 安全政策说明会评估依赖维护状态，并为适用于 Karmada 的依赖 CVE 修复受支持版本。因此可以选择 `Met`。

[dependancy]: https://github.com/karmada-io/karmada/blob/master/.github/dependabot.yml ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci-image-scanning.yaml ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci-image-scanning-on-schedule.yml ; https://github.com/karmada-io/community/blob/main/security-team/SECURITY.md

### [Met] [MUST]
The project MUST make it easy to identify and update reused externally-maintained components, or use the standard components provided by the system or programming language. [updateable_reused_components]

Go module 文件和 vendor 元数据可以把外部组件映射到明确版本；`hack/update-vendor.sh`、`hack/verify-vendor.sh` 负责更新和验证 vendor 内容。Dependabot 会针对依赖更新创建 PR，Helm lock 文件也保留依赖版本和 digest。发现漏洞后可以定位对应 module、更新版本并重新生成 vendor，而不需要从业务源码中人工寻找复制的第三方代码，因此可以选择 `Met`。

[dependancy]: https://github.com/karmada-io/karmada/blob/master/go.mod ; https://github.com/karmada-io/karmada/blob/master/hack/update-vendor.sh ; https://github.com/karmada-io/karmada/blob/master/hack/verify-vendor.sh ; https://github.com/karmada-io/karmada/blob/master/.github/dependabot.yml

### [Met] [SHOULD]
The project SHOULD avoid using deprecated or obsolete functions and APIs where FLOSS alternatives are available in its technology stack and to a supermajority of supported users. [interfaces_current]

Karmada 在 `golangci-lint` 中启用了 Staticcheck 的全部检查，其中包括发现已弃用 API 使用的检查，并启用了 `modernize`；CI 会对每个 push 和 pull request 执行这些规则。依赖由 Dependabot 持续更新，Karmada 自身的 API 变更则遵循 Kubernetes 风格的版本化、deprecation 和 release note 流程。项目有自动检测和持续迁移机制，可选择 `Met`。

[dependancy]: https://github.com/karmada-io/karmada/blob/master/.golangci.yml ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci.yml ; https://github.com/karmada-io/karmada/tree/master/docs/CHANGELOG

## Automated test suite

### [Met] [MUST]
An automated test suite MUST be applied on each check-in to a shared repository for at least one branch. This test suite MUST produce a report on test success or failure. [automated_integration_testing]

Karmada 的 `CI Workflow` 同时监听 push 和 pull request。流程会执行编译、单元测试、lint、代码生成验证和多个 Kubernetes 版本的 E2E 测试，每个 job 都在 GitHub Actions 中产生可见的成功或失败结果。至少 master 及 pull request 的每次变更都会触发自动测试，因此可以选择 `Met`。

[dependancy]: https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci.yml ; https://github.com/karmada-io/karmada/actions

### [?] [MUST]
The project MUST add regression tests to an automated test suite for at least 50% of the bugs fixed within the last six months. [regression_tests_added50]

这一项不是要求项目“存在很多测试”，而是要统计最近六个月修复的 bug，并证明其中至少 50% 增加了能够防止同类问题再次发生的自动化回归测试。仅凭仓库中存在大量 `_test.go` 和 E2E 用例，无法计算这个比例。

当前公开仓库没有发现持续发布的六个月 bug-fix/回归测试统计，PR 模板也没有强制记录某个 bug fix 对应的回归测试位置，因此暂时不能可靠地从 `?` 改为 `Met`。需要先定义 bug-fix PR 的分母、审计最近六个月合并 PR 的测试变更，并公开结果；如果比例不足 50%，则应填 `Unmet` 并补测试。

### [Unmet] [MUST]
The project MUST have FLOSS automated test suite(s) that provide at least 80% statement coverage if there is at least one FLOSS tool that can measure this criterion in the selected language. [test_statement_coverage80]

Go 自带 FLOSS 覆盖率工具，Karmada 的 `Makefile` 已对 `pkg`、`cmd`、`examples` 和 `operator` 生成 coverage profile，并由 CI 上传 Codecov，因此本条不能选择 N/A。调研时 master 分支的公开 Codecov badge 显示约 42%，明显低于 Silver 要求的 80%，当前应选择 `Unmet`。

修复时应优先补齐安全关键和核心控制器路径的测试，把项目 statement coverage 提升到至少 80%，并在 Codecov 中设置 project coverage required check。达到阈值后，需要用公开的 master commit 覆盖率报告作为依据再改为 `Met`。

[dependancy]: https://codecov.io/gh/karmada-io/karmada ; https://github.com/karmada-io/karmada/blob/master/Makefile ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci.yml ; https://github.com/karmada-io/karmada/blob/master/.codecov.yml
[improvement]: 优先补齐安全关键与核心控制器路径的测试，将语句覆盖率提升到至少 80%，并在 Codecov 设置 project coverage required check；达到阈值后以公开的 master commit 覆盖报告作为依据。

## New functionality testing

### [Met] [MUST]
The project MUST have a formal written policy that as major new functionality is added, tests for the new functionality MUST be added to an automated test suite. [test_policy_mandated]

Karmada 的贡献指南在 Creating Pull Requests 中要求提交者在开发代码或修复后添加新的测试用例，并在提交 PR 前运行 `make verify` 和 `make test`。这是一份公开的书面贡献政策，且测试会进入项目自动化测试套件。为了让 OpenSSF 审核证据更明确，建议后续把措辞进一步改成“Major new functionality MUST include automated tests”，但现有政策已经表达了贡献必须附带测试的要求，可以选择 `Met`。

[dependancy]: https://github.com/karmada-io/karmada/blob/master/CONTRIBUTING.md

### [Met] [MUST]
The project MUST include, in its documented instructions for change proposals, the policy that tests are to be added for major new functionality. [tests_documented_added]

这一项强调测试政策必须直接出现在提交变更的说明中，而不能只存在于维护者内部规则。Karmada 的 `CONTRIBUTING.md` 同时说明 PR workflow、添加新测试用例以及提交前运行测试，正是贡献者提交变更时会阅读的公开文档，因此可以选择 `Met`。建议同步在 PR template 中增加“新增/修改了哪些测试”和例外理由，使证据更直观。

[dependancy]: https://github.com/karmada-io/karmada/blob/master/CONTRIBUTING.md ; https://github.com/karmada-io/karmada/blob/master/.github/PULL_REQUEST_TEMPLATE.md

## Warning flags

### [Met] [MUST]
Projects MUST be maximally strict with warnings in the software produced by the project, where practical. [warnings_strict]

项目应尽可能启用语言和工具链中严格的警告与检查，并且不能长期忽略这些告警。Karmada 的 `golangci-lint` 配置启用了 `gosec`、Staticcheck 全部检查、revive、gocyclo、depguard、gofmt、goimports 等规则；`max-issues-per-linter` 和 `max-same-issues` 均设为 0，表示不截断问题数量。CI 运行 `hack/verify-staticcheck.sh`，任何未处理问题都会使 job 失败。配置中少数被禁用的规则附有具体原因，符合“在实际可行范围内尽可能严格”的要求，可以选择 `Met`。

[dependancy]: https://github.com/karmada-io/karmada/blob/master/.golangci.yml ; https://github.com/karmada-io/karmada/blob/master/hack/verify-staticcheck.sh ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci.yml

# Security

## Secure development knowledge

### [Met] [MUST]
The project MUST implement secure design principles, where applicable. If the project is not producing software, select "not applicable" (N/A). [implement_secure_design]

这一项要求项目不只是“有人知道安全设计”，还要在实际软件中落实安全设计原则。Karmada 采用 Kubernetes 原生认证、授权和 RBAC，将控制面、成员集群及各组件权限分离；官方文档列出了组件所需权限并强调最小权限。控制面通信使用 TLS/证书，凭据通过 Secret 或独立证书文件管理，发布制品使用 Cosign/SLSA 验证，安全自评也描述了关键组件、Push/Pull 模式、攻击面和安全目标。这些是最小权限、职责分离、安全默认值、纵深防御和完整性验证的实际实现，可以选择 `Met`。

不过，相关论据目前分散在多份文档中。为了同时满足 `assurance_case`，建议把每项安全原则、实现位置和测试证据集中映射到一份 assurance case。

[dependancy]: https://github.com/karmada-io/community/blob/main/security-team/assessments/self-assessment.md ; https://karmada.io/docs/administrator/security/component-permission/ ; https://karmada.io/docs/administrator/security/security-considerations/ ; https://karmada.io/docs/administrator/security/verify-artifacts/

## Use basic good cryptographic practices

### [Met] [MUST]
The default security mechanisms within the software produced by the project MUST NOT depend on cryptographic algorithms or modes with known serious weaknesses, such as SHA-1 or CBC mode in SSH. [crypto_weaknesses]

Karmada 不自行设计加密算法，而是使用 Go 和 Kubernetes 经过广泛审查的 TLS、X.509 和证书实现。官方安全配置为核心 API 组件设置 TLS 1.3 最低版本，并为组件提供受支持的 cipher suite 配置；发布制品完整性使用 SHA-256、Cosign 和 SLSA provenance。基于默认 TLS 配置和成熟密码库，项目的默认安全机制不依赖 MD5、SHA-1、RC4、单 DES 等已知严重弱算法，可以选择 `Met`。

填报前仍应对所有安装路径（Helm、Operator、`karmadactl init` 和脚本部署）的默认 TLS/cipher 配置做一次一致性检查，确保没有某个路径保留不安全默认值。

[dependancy]: https://karmada.io/docs/administrator/security/security-considerations/ ; https://karmada.io/docs/administrator/security/verify-artifacts/ ; https://github.com/karmada-io/karmada/tree/master/artifacts/deploy

### [Met] [SHOULD]
The project SHOULD support multiple cryptographic algorithms so users can quickly switch if one is broken. [crypto_algorithm_agility]

Karmada 通过 Kubernetes/Go TLS 栈支持多种现代 cipher suite，并为服务端组件提供 `--tls-min-version` 和 `--tls-cipher-suites`/`--cipher-suites` 等配置。用户可以在不修改或重新编译 Karmada 源码的情况下调整允许的 TLS 版本和算法；证书框架也支持由部署者选择和轮换符合要求的证书密钥。因此具备算法敏捷性，可以选择 `Met`。

[dependancy]: https://karmada.io/docs/administrator/security/security-considerations/ ; https://karmada.io/docs/administrator/security/cert-framework/ ; https://github.com/karmada-io/karmada/tree/master/docs/command-line-flags

### [Met] [MUST]
The project MUST support storing authentication credentials and private cryptographic keys in files separate from other information, and permit users to update and replace them without code recompilation. If the project never processes credentials or private keys, select "not applicable" (N/A). [crypto_credential_agility]

Karmada 会处理 kubeconfig、client certificate、token 和私钥，因此本条不能选择 N/A。项目通过 Kubernetes Secret、kubeconfig 和独立的证书/密钥文件保存凭据，而不是把凭据硬编码进二进制或普通业务配置。证书框架和证书轮换机制允许替换证书与密钥而无需重新编译代码，成员集群访问凭据也通过 Secret reference 管理，因此可以选择 `Met`。

[dependancy]: https://karmada.io/docs/administrator/security/cert-framework/ ; https://karmada.io/docs/administrator/security/certificate-rotation/overview/ ; https://karmada.io/docs/administrator/security/component-permission/

### [Met] [SHOULD]
The software produced by the project SHOULD support secure protocols for all network communications. Insecure protocols such as FTP, HTTP, telnet, SSLv3 or earlier, and SSHv1 SHOULD be disabled by default and enabled only through explicit configuration. [crypto_used_network]

Karmada 控制面 API、aggregated API、webhook、scheduler estimator、agent 与成员集群 API 等安全相关通信均基于 HTTPS/TLS 或 mTLS。官方安全文档描述了 TLS 配置和证书框架，默认部署不依赖 FTP、telnet、SSLv3 或 SSHv1 等不安全协议。健康检查等不携带敏感数据的本地 HTTP endpoint 不等同于用不安全协议传输认证数据。基于默认安全通信设计，可以选择 `Met`。

[dependancy]: https://karmada.io/docs/administrator/security/security-considerations/ ; https://karmada.io/docs/administrator/security/cert-framework/ ; https://github.com/karmada-io/community/blob/main/security-team/assessments/self-assessment.md

### [Met] [SHOULD]
The software produced by the project SHOULD, if it supports or uses TLS, support at least TLS version 1.2. If the software does not use TLS, select "not applicable" (N/A). [crypto_tls12]

Karmada 明确使用 TLS，所以本条不能选择 N/A。官方 Security Considerations 文档为 karmada-apiserver、karmada-aggregated-apiserver、karmada-search 和 karmada-metrics-adapter 配置的最低版本是 TLS 1.3，已高于 TLS 1.2 的最低要求；Go/Kubernetes TLS 栈也支持 TLS 1.2 及以上版本，因此可以选择 `Met`。

[dependancy]: https://karmada.io/docs/administrator/security/security-considerations/#tls-configuration

### [Met] [MUST]
The software produced by the project MUST, if it supports TLS, perform TLS certificate verification by default, including on subresources. If the software does not use TLS, select "not applicable" (N/A). [crypto_certificate_verification]

Karmada 基于 Go `crypto/tls`、Kubernetes `client-go` 和标准 kubeconfig 建立 TLS client；这些实现默认验证服务端证书链和目标身份。Karmada 的证书框架为各组件规定 CA、server certificate 和 client certificate 的信任关系，scheduler/descheduler 与 estimator 等 gRPC 通信也有证书校验。跳过验证必须由用户显式配置，而不是默认行为，因此可以选择 `Met`。

为提高填报可信度，建议在 assurance case 中列出所有主动发起 TLS 的 client path，并说明任何 `InsecureSkipVerify` 选项仅用于显式场景且默认关闭。

[dependancy]: https://karmada.io/docs/administrator/security/cert-framework/ ; https://github.com/karmada-io/community/blob/main/security-team/assessments/self-assessment.md ; https://github.com/karmada-io/karmada/search?q=InsecureSkipVerify&type=code

### [Met] [MUST]
The software produced by the project MUST, if it supports TLS, perform certificate verification before sending HTTP headers with private information such as secure cookies. If the software does not use TLS, select "not applicable" (N/A). [crypto_verification_private]

Go HTTP client 会在 TLS handshake 和证书验证成功后才发送 HTTP request headers；Karmada 通过标准 Go/Kubernetes transport 发送 bearer token、client credential 和 impersonation headers，不自行实现“先发送敏感 header、后验证证书”的网络栈。默认 transport 继承证书验证行为，因此敏感 header 只会在 TLS 验证成功并建立连接后发送，可以选择 `Met`。

该项需要较长说明，正式填报时应补充代表性的 Karmada client 初始化代码和 kubeconfig/TLS 配置链接，证明没有绕开 Go transport 的自定义实现。

[dependancy]: https://karmada.io/docs/administrator/security/cert-framework/ ; https://github.com/karmada-io/karmada/tree/master/pkg/util ; https://github.com/karmada-io/karmada/tree/master/pkg/karmadactl

## Secure release

### [Met] [MUST]
The project MUST cryptographically sign releases intended for widespread use and document how users obtain the verification material and verify signatures. The private signing key MUST NOT be stored on sites directly distributing the software. [signed_releases]

Karmada 从 v1.7 起使用 Cosign keyless signing 对发布镜像签名，验证时通过 GitHub Actions OIDC identity 和 Sigstore transparency log 校验，不需要把长期私钥存放在 Docker Hub 等分发站点。CLI、CRD、Helm chart 和 SBOM 从 v1.10.3 起附带由 SLSA GitHub Generator 产生的、经过密码学签名的 provenance。官方 Verify Artifacts 文档提供 `cosign verify` 和 `slsa-verifier verify-artifact` 的完整命令、identity/source URI 和 tag 参数，因此可以选择 `Met`。

[dependancy]: https://karmada.io/docs/administrator/security/verify-artifacts/ ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/release.yml ; https://github.com/karmada-io/karmada/releases

### [Unmet] [SHOULD]
It is SUGGESTED that each important version tag in the version control system be cryptographically signed and verifiable as described for signed releases. [version_tags_signed]

这一项检查的是 Git tag 对象本身是否经过 GPG、SSH 或其他可验证机制签名，而不是 release asset、SLSA provenance 或 tag 所指向 commit 是否显示 GitHub `Verified`。调研最新正式版本 `v1.18.2` 时，远端只返回单一 tag ref，没有 annotated tag 的解引用对象，表现为 lightweight tag；因此不能证明重要版本 tag 自身已签名，当前应选择 `Unmet`。

该项是 SUGGESTED，不会像 MUST 一样直接阻止 Silver，但必须明确填写。建议后续发布流程创建签名 annotated tags，并在发布文档中说明如何使用 `git tag -v` 或对应 Sigstore/SSH 方法验证。

[dependancy]: https://github.com/karmada-io/karmada/releases/tag/v1.18.2 ; https://github.com/karmada-io/karmada/tags
[improvement]: 在发布流程中为重要版本创建签名的 annotated tag（GPG/SSH/Sigstore），并在发布文档中提供 `git tag -v` 或对应验证说明。

## Other security issues

### [?] [MUST]
The project results MUST check all inputs from potentially untrusted sources to ensure they are valid using an allowlist, and reject invalid inputs if there are any restrictions on the data. [input_validation]

该项要求覆盖“所有潜在不可信输入”，不能仅用 denylist，也不能只举出一个 validator 就宣称整个项目满足。Karmada 已有大量正向验证机制：CRD OpenAPI schema 约束类型、枚举、长度和格式；Kubernetes API server 执行 schema/admission validation；Karmada validating webhook 对策略、集群和资源解释器等对象执行语义校验；CLI 使用结构化 flag/parser。以上表明项目具备较强基础。

但 Karmada 的输入面很广，还包括 cluster proxy、webhook、Lua/WASM 或 resource interpreter、自定义资源、kubeconfig、HTTP/gRPC endpoint 和外部搜索后端。现有公开文档没有给出覆盖所有 trust boundary 的输入清单及 allowlist 证据，因此暂时保持 `?` 更准确。正式改为 `Met` 前，应在 assurance case 中逐项列出不可信输入、允许格式、验证代码、拒绝路径和测试。

### [Met] [SHOULD]
Hardening mechanisms SHOULD be used so that software defects are less likely to result in security vulnerabilities. [hardening]

OpenSSF 对这一项所说的 hardening 包括 seccomp、编译/运行时保护、CSP 等；最小权限本身虽然重要，但不能单独作为本项证据。Karmada 的官方 deployment manifests 为多个控制面容器配置 `allowPrivilegeEscalation: false` 和 `seccompProfile: RuntimeDefault`，减少缺陷被利用后进行系统调用或权限提升的能力。Go 发布构建使用内存安全语言并禁用 CGO，也避免引入 C 运行时内存破坏面。已有明确的 hardening 机制，可以选择 `Met`。

建议进一步审计所有 Helm、Operator、脚本安装路径是否一致设置 `runAsNonRoot`、只读根文件系统和 drop capabilities，避免不同安装方式的加固程度不一致。

[dependancy]: https://github.com/karmada-io/karmada/tree/master/artifacts/deploy ; https://github.com/karmada-io/karmada/blob/master/hack/build.sh ; https://karmada.io/docs/administrator/security/component-permission/

### [Unmet] [MUST]
The project MUST provide an assurance case that justifies why its security requirements are met. It MUST include a threat model, clear trust boundaries, an argument that secure design principles have been applied, and an argument that common implementation security weaknesses have been countered. A URL is required. [assurance_case]

Karmada 已发布 CNCF Security Self-Assessment、组件架构、安全目标、漏洞响应流程和 OSTIF 安全评审，这些都是构建 assurance case 的高价值证据。但当前 self-assessment 没有明确、完整地标识所有 trust boundary，也没有按照“安全 claim → design principle → common weakness → control/test evidence”的结构论证为什么全部安全要求已经满足；其 Non-goals 部分也不完整。因此现有材料还不能直接视为满足 OpenSSF 所定义的完整 assurance case，当前应选择 `Unmet`。

建议在 `community/security-team/assessments/` 新增 `assurance-case.md`，至少包含：威胁参与者和能力、Push/Pull 模式数据流、控制面/成员集群/发布流水线的信任边界、Saltzer and Schroeder 等安全原则映射、OWASP/CWE 常见弱点映射、每个控制的代码/配置/测试证据、剩余风险和适用版本。完成并经 security team/maintainer review 后，再以该公开 URL 填 `Met`。

[dependancy]: https://github.com/karmada-io/community/blob/main/security-team/assessments/self-assessment.md ; https://github.com/karmada-io/community/blob/main/security-team/assessments/OSTIF-Karmada-Report.pdf ; https://github.com/karmada-io/community/tree/main/security-team
[improvement]: 在 community/security-team/assessments/ 新增 assurance-case.md，包含威胁模型、明确信任边界、安全设计原则与 OWASP/CWE 常见弱点映射及每项控制的证据，经评审后以公开 URL 作为依据。

# Analysis

## Static code analysis

### [Met] [MUST]
The project MUST use at least one static analysis tool with rules or approaches to look for common vulnerabilities in the analyzed language or environment, if there is at least one FLOSS tool that can implement this criterion in the selected language. [static_analysis_common_vulnerabilities]

项目必须至少使用一种静态分析工具，并启用能够检查项目主要语言或运行环境中常见安全漏洞的规则或分析方法。这里不能只依靠人工代码审查；如果该语言已有可用的开源工具，就必须在项目中实际使用。OpenSSF 页面还要求为这一项提供较完整的说明，不能只选择 `Met` 而不写依据。

Karmada 使用开源的 `golangci-lint` 对 Go 源代码进行静态分析，其 `.golangci.yml` 明确启用了 `gosec`。`gosec` 会检查 Go 代码中可能形成安全漏洞的模式，例如弱文件权限、不安全的随机数或加密算法使用、潜在命令执行、整数溢出转换和不安全的网络配置等。同时，配置还启用了 Staticcheck 全部检查以及其他质量规则，并排除了 vendor、third_party 和生成代码，分析目标主要是 Karmada 自己维护的代码。

项目的 `hack/verify-staticcheck.sh` 会安装固定版本的 `golangci-lint` 并执行 `golangci-lint run`；发现问题时脚本以非零状态退出。GitHub Actions 的 `CI Workflow` 在 push 和 pull request 上运行该脚本，因此静态安全分析是持续执行且会阻止对应 CI job 通过的自动化检查。基于 `gosec` 的安全规则、仓库内公开配置和 CI 自动执行，可以选择 `Met`。

[dependancy]: https://github.com/karmada-io/karmada/blob/master/.golangci.yml ; https://github.com/karmada-io/karmada/blob/master/hack/verify-staticcheck.sh ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci.yml

## Dynamic code analysis

### [N/A] [MUST]
If the software produced by the project includes software written using a memory-unsafe language (e.g., C or C++), then at least one dynamic tool (e.g., a fuzzer or web application scanner) MUST be routinely used in combination with a mechanism to detect memory safety problems such as buffer overwrites. If the project does not produce software written in a memory-unsafe language, choose "not applicable" (N/A). [dynamic_analysis_unsafe]

这一项只在项目交付的软件包含 C、C++ 等内存不安全语言时强制要求：项目需要定期运行动态分析工具，并配合 AddressSanitizer、MemorySanitizer、Valgrind 等机制检测缓冲区越界、非法内存访问等问题。如果项目不使用内存不安全语言，OpenSSF 原文明确要求选择 `N/A`，而不是为了表示项目进行了普通单元测试或端到端测试而选择 `Met`。

Karmada 的主要实现语言是 Go，其他仓库内容主要是 Shell、JavaScript、Makefile、Dockerfile 和配置文件，不包含由 Karmada 项目维护并作为产品构建的 C/C++ 源代码。Karmada 的正式 Go 构建脚本还显式设置 `CGO_ENABLED=0`，不会把通过 CGO 编译的 C 代码链接到发布二进制中。因此，该项目不存在本条所描述的“针对内存不安全语言使用动态内存错误检测工具”的适用前提，应选择 `N/A`。

仓库中的部分 Go 生成代码或依赖可能导入 Go 的 `unsafe` 包，但这不等同于项目使用 C/C++ 等内存不安全语言，也不会改变本条按实现语言判断是否适用的条件。普通的 Go 单元测试、E2E 测试和镜像漏洞扫描可以作为其他质量或安全条目的证据，但不应被用来把本条填写为 `Met`。

[dependancy]: https://github.com/karmada-io/karmada ; https://github.com/karmada-io/karmada/blob/master/hack/build.sh ; https://www.bestpractices.dev/en/projects/5301/silver#analysis
