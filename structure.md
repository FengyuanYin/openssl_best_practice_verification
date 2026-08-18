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
三级标题[A][B] A最多有四种选择([?], [Unmet], [Met], [N/A])。如果把[?]替换成其他选项，必须在该条目的最后一行补充[dependancy]，并说明证据。

<!-- OpenSSF source: https://www.bestpractices.dev/en/projects/5301/silver#analysis -->

# Basics

## Prerequisites

### [Met] [MUST]
The project MUST achieve a passing level badge. [achieve_passing]

[dependancy]: Karmada 在 OpenSSF Best Practices 项目 #5301 已获得并保持 Passing 徽章（2022-01-21 获得），README 亦展示该徽章；本次审计目标为 Silver 级标准。https://www.bestpractices.dev/en/projects/5301 ; https://github.com/karmada-io/karmada/blob/master/README.md
## Basic project website content

### [Met] [MUST]
The information on how to contribute MUST include the requirements for acceptable contributions (e.g., a reference to any required coding standard). (URL required) [contribution_requirements]

[dependancy]: CONTRIBUTING.md 说明了 PR 流程、提交前需通过 make verify/make test，并在 Code Review 章节要求遵循 Go coding guidelines（CodeReviewComments），满足“可接受贡献要求”的文档化。https://github.com/karmada-io/karmada/blob/master/CONTRIBUTING.md
## Project oversight

### [Unmet] [SHOULD]
The project SHOULD have a legal mechanism where all developers of non-trivial amounts of project software assert that they are legally authorized to make these contributions. The most common and easily-implemented approach for doing this is by using a Developer Certificate of Origin (DCO) , where users add "signed-off-by" in their commits and the project links to the DCO website. However, this MAY be implemented as a Contributor License Agreement (CLA), or other legal mechanism. (URL required) [dco]

The DCO is the recommended mechanism because it's easy to implement, tracked in the source code, and git directly supports a "signed-off" feature using "commit -s". To be most effective it is best if the project documentation explains what "signed-off" means for that project. A CLA is a legal agreement that defines the terms under which intellectual works have been licensed to an organization or project. A contributor assignment agreement (CAA) is a legal agreement that transfers rights in an intellectual work to another party; projects are not required to have CAAs, since having CAA increases the risk that potential contributors will not contribute, especially if the receiver is a for-profit organization. The Apache Software Foundation CLAs (the individual contributor license and the corporate CLA) are examples of CLAs, for projects which determine that the risks of these kinds of CLAs to the project are less than their benefits.

[dependancy]: 主仓库 CONTRIBUTING.md 与 .github/PULL_REQUEST_TEMPLATE.md 均未要求 DCO/Signed-off-by，也没有 DCO 检查流程；仅 CNCF 历史文档提及 DCO，当前贡献指引未落实该法律机制，故不能填 Met。https://github.com/karmada-io/karmada/blob/master/CONTRIBUTING.md ; https://github.com/karmada-io/karmada/blob/master/.github/PULL_REQUEST_TEMPLATE.md
### [Met] [MUST]
The project MUST clearly define and document its project governance model (the way it makes decisions, including key roles). (URL required) [governance]

There needs to be some well-established documented way to make decisions and resolve disputes. In small projects, this may be as simple as "the project owner and lead makes all final decisions". There are various governance models, including benevolent dictator and formal meritocracy; for more details, see Governance models . Both centralized (e.g., single-maintainer) and decentralized (e.g., group maintainers) approaches have been successfully used in projects. The governance information does not need to document the possibility of creating a project fork, since that is always possible for FLOSS projects.

[dependancy]: community 仓库 GOVERNANCE.md 公开定义了治理价值、成员体系、维护者投票（重大事项 2/3 多数）、路线图变更与章程修改流程，决策机制清晰。https://github.com/karmada-io/community/blob/main/GOVERNANCE.md
### [Met] [MUST]
The project MUST adopt a code of conduct and post it in a standard location. (URL required) [code_of_conduct]

Projects may be able to improve the civility of their community and to set expectations about acceptable conduct by adopting a code of conduct. This can help avoid problems before they occur and make the project a more welcoming place to encourage contributions. This should focus only on behavior within the community/workplace of the project. Example codes of conduct are the Linux kernel code of conduct , the Contributor Covenant Code of Conduct , the Debian Code of Conduct , the Ubuntu Code of Conduct , the Fedora Code of Conduct , the GNOME Code Of Conduct , the KDE Community Code of Conduct , the Python Community Code of Conduct , The Ruby Community Conduct Guideline , and The Rust Code of Conduct .

[dependancy]: 主仓库根目录 CODE_OF_CONDUCT.md 采用标准位置并链接 Karmada/CNCF Code of Conduct。https://github.com/karmada-io/karmada/blob/master/CODE_OF_CONDUCT.md ; https://github.com/karmada-io/community/blob/main/CODE_OF_CONDUCT.md
### [Met] [MUST]
The project MUST clearly define and publicly document the key roles in the project and their responsibilities, including any tasks those roles must perform. It MUST be clear who has which role(s), though this might not be documented in the same way. (URL required) [roles_responsibilities]

The documentation for governance and roles and responsibilities may be in one place.

[dependancy]: community-membership.md 定义了 Member/Reviewer/Approver/Maintainer 的职责、要求与权限，MAINTAINERS.md/REVIEWERS.md/APPROVERS.md 公开了具体人员名单。https://github.com/karmada-io/community/blob/main/community-membership.md ; https://github.com/karmada-io/community/blob/main/MAINTAINERS.md ; https://github.com/karmada-io/community/blob/main/APPROVERS.md
### [?] [MUST]
The project MUST be able to continue with minimal interruption if any one person dies, is incapacitated, or is otherwise unable or unwilling to continue support of the project. In particular, the project MUST be able to create and close issues, accept proposed changes, and release versions of software, within a week of confirmation of the loss of support from any one individual. This MAY be done by ensuring someone else has any necessary keys, passwords, and legal rights to continue the project. Individuals who run a FLOSS project MAY do this by providing keys in a lockbox and a will providing any needed legal rights (e.g., for DNS names). (URL required) [access_continuity]

### [Met] [SHOULD]
The project SHOULD have a "bus factor" of 2 or more. (URL required) [bus_factor]

A "bus factor" (aka "truck factor") is the minimum number of project members that have to suddenly disappear from a project ("hit by a bus") before the project stalls due to lack of knowledgeable or competent personnel. The truck-factor tool can estimate this for projects on GitHub. For more information, see Assessing the Bus Factor of Git Repositories by Cosentino et al.

[dependancy]: MAINTAINERS.md 列出 13 名 active maintainers，来自华为、ByteDance、Bloomberg、Alibaba Cloud、DaoCloud、Trip.com、CECloud 等多家机构，另有大量 reviewer/approver，可证明 bus factor >= 2。https://github.com/karmada-io/community/blob/main/MAINTAINERS.md ; https://github.com/karmada-io/community/blob/main/APPROVERS.md
## Documentation

### [Unmet] [MUST]
The project MUST have a documented roadmap that describes what the project intends to do and not do for at least the next year. (URL required) [documentation_roadmap]

The project might not achieve the roadmap, and that's fine; the purpose of the roadmap is to help potential users and contributors understand the intended direction of the project. It need not be detailed.

[dependancy]: community ROADMAP.md 当前仅包含“2026 feature plan”；以 2026-08-18 为审计日，其未覆盖之后至少一整年，Pending 列表也没有时间范围，因此不满足“未来至少一年”的路线图要求。https://github.com/karmada-io/community/blob/main/ROADMAP.md
### [Met] [MUST]
The project MUST include documentation of the architecture (aka high-level design) of the software produced by the project. If the project does not produce software, select "not applicable" (N/A). (URL required) [documentation_architecture]

A software architecture explains a program's fundamental structures, i.e., the program's major components, the relationships among them, and the key properties of these components and relationships.

[dependancy]: README 提供架构图并说明控制面组件及其关系；安全自评描述 Host Cluster/控制面/Member Cluster 与 Push/Pull 模式下的组件和数据流。https://github.com/karmada-io/karmada/blob/master/README.md ; https://github.com/karmada-io/community/blob/main/security-team/assessments/self-assessment.md
### [Unmet] [MUST]
The project MUST document what the user can and cannot expect in terms of security from the software produced by the project (its "security requirements"). (URL required) [documentation_security]

These are the security requirements that the software is intended to meet.

[dependancy]: 安全自评的 Non-goals 章节为空，Security Considerations 主要是部署加固建议，未明确文档化用户“能与不能期待”的安全需求/边界，故不满足 security requirements 文档要求。https://github.com/karmada-io/community/blob/main/security-team/assessments/self-assessment.md ; https://karmada.io/docs/administrator/security/security-considerations/
### [Met] [MUST]
The project MUST provide a "quick start" guide for new users to help them quickly do something with the software. (URL required) [documentation_quick_start]

The idea is to show users how to get started and make the software do anything at all. This is critically important for potential users to get started.

[dependancy]: README Quick Start 提供 clone、hack/local-up-karmada.sh 搭建控制面并运行示例的步骤；官网 Installation 文档提供 karmadactl/Helm/Operator 快速安装方式。https://github.com/karmada-io/karmada/blob/master/README.md ; https://karmada.io/docs/installation/
### [Met] [MUST]
The project MUST make an effort to keep the documentation consistent with the current version of the project results (including software produced by the project). Any known documentation defects making it inconsistent MUST be fixed. If the documentation is generally current, but erroneously includes some older information that is no longer true, just treat that as a defect, then track and fix as usual. [documentation_current]

The documentation MAY include information about differences or changes between versions of the software and/or link to older versions of the documentation. The intent of this criterion is that an effort is made to keep the documentation consistent, not that the documentation must be perfect.

[dependancy]: 官网按版本维护文档（含 next 版本）并同步发布版本；文档源码在 karmada-io/website 仓库通过 issue/PR 跟踪，仓库 CI 还校验被提升文档（verify-lifted 等），体现持续维护文档一致性的努力。https://karmada.io/docs/ ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci.yml
### [Met] [MUST]
The project repository front page and/or website MUST identify and hyperlink to any achievements, including this best practices badge, within 48 hours of public recognition that the achievement has been attained. (URL required) [documentation_achievements]

An achievement is any set of external criteria that the project has specifically worked to meet, including some badges. This information does not need to be on the project website front page. A project using GitHub can put achievements on the repository front page by adding them to the README file.

[dependancy]: 当前 master README 徽章区包含 CII Best Practices 徽章并链接项目 #5301（另有 OpenSSF Scorecard、Codecov、FOSSA、CLOMonitor 等徽章），符合“识别并超链接成就”的要求。https://github.com/karmada-io/karmada/blob/master/README.md ; https://www.bestpractices.dev/en/projects/5301
## Accessibility and internationalization

### [?] [SHOULD]
The project (both project sites and project results) SHOULD follow accessibility best practices so that persons with disabilities can still participate in the project and use the project results where it is reasonable to do so. [accessibility_best_practices]

For web applications, see the Web Content Accessibility Guidelines (WCAG 2.0) and its supporting document Understanding WCAG 2.0 ; see also W3C accessibility information . For GUI applications, consider using the environment-specific accessibility guidelines (such as Gnome , KDE , XFCE , Android , iOS , Mac , and Windows ). Some TUI applications (e.g. `ncurses` programs) can do certain things to make themselves more accessible (such as `alpine`'s `force-arrow-cursor` setting). Most command-line applications are fairly accessible as-is. This criterion is often N/A, e.g., for program libraries. Here are some examples of actions to take or issues to consider: Provide text alternatives for any non-text content so that it can be changed into other forms people need, such as large print, braille, speech, symbols or simpler language ( WCAG 2.0 guideline 1.1 ) Color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element. ( WCAG 2.0 guideline 1.4.1 ) The visual presentation of text and images of text has a contrast ratio of at least 4.5:1, except for large text, incidental text, and logotypes ( WCAG 2.0 guideline 1.4.3 ) Make all functionality available from a keyboard (WCAG guideline 2.1) A GUI or web-based project SHOULD test with at least one screen-reader on the target platform(s) (e.g. NVDA, Jaws, or WindowEyes on Windows; VoiceOver on Mac & iOS; Orca on Linux/BSD; TalkBack on Android). TUI programs MAY work to reduce overdraw to prevent redundant reading by screen-readers.

### [Unmet] [SHOULD]
The software produced by the project SHOULD be internationalized to enable easy localization for the target audience's culture, region, or language. If internationalization (i18n) does not apply (e.g., the software doesn't generate text intended for end-users and doesn't sort human-readable text), select "not applicable" (N/A). [internationalization]

Localization "refers to the adaptation of a product, application or document content to meet the language, cultural and other requirements of a specific target market (a locale)." Internationalization is the "design and development of a product, application or document content that enables easy localization for target audiences that vary in culture, region, or language." (See W3C's "Localization vs. Internationalization" .) Software meets this criterion simply by being internationalized. No localization for another specific language is required, since once software has been internationalized it's possible for others to work on localization.

[dependancy]: karmadactl 仅少量命令使用 k8s.io/kubectl/pkg/util/i18n 包装，核心软件与 CLI 面向用户的输出没有系统性 i18n/本地化框架或资源目录，不能证明已国际化；此为 SHOULD 项，暂记 Unmet。https://github.com/karmada-io/karmada/tree/master/pkg/karmadactl
## Other

### [N/A] [MUST]
If the project sites (website, repository, and download URLs) store passwords for authentication of external users, the passwords MUST be stored as iterated hashes with a per-user salt by using a key stretching (iterated) algorithm (e.g., Argon2id, Bcrypt, Scrypt, or PBKDF2). If the project sites do not store passwords for this purpose, select "not applicable" (N/A). [sites_password_security]

Note that the use of GitHub meets this criterion. This criterion only applies to passwords used for authentication of external users into the project sites (aka inbound authentication). If the project sites must log in to other sites (aka outbound authentication), they may need to store authorization tokens for that purpose differently (since storing a hash would be useless). This applies criterion crypto_password_storage to the project sites, similar to sites_https.

[dependancy]: 项目站点为文档站，代码托管、issue 与身份认证均由 GitHub/CNCF 提供，项目自身不存储外部用户密码；OpenSSF 注明使用 GitHub 即满足本项，故 N/A。https://karmada.io/ ; https://github.com/karmada-io/karmada
# Change Control

## Previous versions

### [Met] [MUST]
The project MUST maintain the most often used older versions of the product or provide an upgrade path to newer versions. If the upgrade path is difficult, the project MUST document how to perform the upgrade (e.g., the interfaces that have changed and detailed suggested steps to help upgrade). [maintenance_or_update]

[dependancy]: SECURITY.md 声明维护最近三个 minor release 分支（release-1.16/1.17/1.18）并定期补丁（约每 3 个月），遵循 SemVer；官网提供升级/兼容性文档。https://github.com/karmada-io/community/blob/main/security-team/SECURITY.md ; https://karmada.io/docs/administrator/compatibility/
# Reporting

## Bug-reporting process

### [Met] [MUST]
The project MUST use an issue tracker for tracking individual issues. [report_tracker]

[dependancy]: 项目使用 GitHub Issues 作为问题跟踪器，并提供多类 issue 模板（bug/feature 等）。https://github.com/karmada-io/karmada/issues ; https://github.com/karmada-io/karmada/tree/master/.github/ISSUE_TEMPLATE
## Vulnerability report process

### [N/A] [MUST]
The project MUST give credit to the reporter(s) of all vulnerability reports resolved in the last 12 months, except for the reporter(s) who request anonymity. If there have been no vulnerabilities resolved in the last 12 months, select "not applicable" (N/A). (URL required) [vulnerability_report_credit]

[dependancy]: 以 2026-08-18 为审计截止日，公开 GitHub Security Advisories 中最近一次发布于 2025-01-03（GHSA-cwrh-575j-8vr3、GHSA-mg7w-c9x2-xh7r），近 12 个月（2025-08-18 之后）无已解决并披露的漏洞，故按官方规则选 N/A；请维护者确认私有漏洞记录。https://github.com/karmada-io/karmada/security/advisories
### [Met] [MUST]
The project MUST have a documented process for responding to vulnerability reports. (URL required) [vulnerability_response_process]

This is strongly related to vulnerability_report_process, which requires that there be a documented way to report vulnerabilities. It also related to vulnerability_report_response, which requires response to vulnerability reports within a certain time frame.

[dependancy]: community/security-team 文档化定义了漏洞报告渠道（cncf-karmada-security@lists.cncf.io）、2 个工作日确认、严重性评估与 CVE 流程、补丁/发布/披露时间线及私人分销商通知机制。https://github.com/karmada-io/community/blob/main/security-team/security-release-process.md ; https://github.com/karmada-io/community/blob/main/security-team/SECURITY.md
# Quality

## Coding standards

### [Met] [MUST]
The project MUST identify the specific coding style guides for the primary languages it uses, and require that contributions generally comply with it. (URL required) [coding_standards]

In most cases this is done by referring to some existing style guide(s), possibly listing differences. These style guides can include ways to improve readability and ways to reduce the likelihood of defects (including vulnerabilities). Many programming languages have one or more widely-used style guides. Examples of style guides include Google's style guides and SEI CERT Coding Standards .

[dependancy]: CONTRIBUTING.md 的 Code Review 章节明确要求贡献者遵循 Go 官方 CodeReviewComments 编码规范，满足“识别主要语言编码风格指南”的要求。https://github.com/karmada-io/karmada/blob/master/CONTRIBUTING.md
### [Met] [MUST]
The project MUST automatically enforce its selected coding style(s) if there is at least one FLOSS tool that can do so in the selected language(s). [coding_standards_enforced]

This MAY be implemented using static analysis tool(s) and/or by forcing the code through code reformatters. In many cases the tool configuration is included in the project's repository (since different projects may choose different configurations). Projects MAY allow style exceptions (and typically will); where exceptions occur, they MUST be rare and documented in the code at their locations, so that these exceptions can be reviewed and so that tools can automatically handle them in the future. Examples of such tools include ESLint (JavaScript), Rubocop (Ruby), and devtools check (R).

[dependancy]: .golangci.yml 配置 golangci-lint（含 gofmt/gci/goimports 格式化、revive/staticcheck 等），CI 的 golangci job 在 push/PR 上强制运行 hack/verify-staticcheck.sh，违规即失败。https://github.com/karmada-io/karmada/blob/master/.golangci.yml ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci.yml
## Working build system

### [Met] [MUST]
Build systems for native binaries MUST honor the relevant compiler and linker (environment) variables passed in to them (e.g., CC, CFLAGS, CXX, CXXFLAGS, and LDFLAGS) and pass them to compiler and linker invocations. A build system MAY extend them with additional flags; it MUST NOT simply replace provided values with its own. If no native binaries are being generated, select "not applicable" (N/A). [build_standard_variables]

It should be easy to enable special build features like Address Sanitizer (ASAN), or to comply with distribution hardening best practices (e.g., by easily turning on compiler flags to do so).

[dependancy]: 项目生成 Go 原生二进制；hack/build.sh 显式将 LDFLAGS 透传至 go build -ldflags 并尊重 GOOS/GOARCH/CGO_ENABLED，Go 工具链自行处理编译标志，未覆盖或替换调用者传入值。https://github.com/karmada-io/karmada/blob/master/hack/build.sh
### [Met] [SHOULD]
The build and installation system SHOULD preserve debugging information if they are requested in the relevant flags (e.g., "install -s" is not used). If there is no build or installation system (e.g., typical JavaScript libraries), select "not applicable" (N/A). [build_preserve_debug]

E.G., setting CFLAGS (C) or CXXFLAGS (C++) should create the relevant debugging information if those languages are used, and they should not be stripped during installation. Debugging information is needed for support and analysis, and also useful for measuring the presence of hardening features in the compiled binaries.

[dependancy]: hack/build.sh 与 hack/release.sh 未使用 -s -w 等剥离选项，Go 构建默认保留 DWARF/符号调试信息，打包仅 tar+sha256。https://github.com/karmada-io/karmada/blob/master/hack/build.sh ; https://github.com/karmada-io/karmada/blob/master/hack/release.sh
### [Met] [MUST]
The build system for the software produced by the project MUST NOT recursively build subdirectories if there are cross-dependencies in the subdirectories. If there is no build or installation system (e.g., typical JavaScript libraries), select "not applicable" (N/A). [build_non_recursive]

The project build system's internal dependency information needs to be accurate, otherwise, changes to the project may not build correctly. Incorrect builds can lead to defects (including vulnerabilities). A common mistake in large build systems is to use a "recursive build" or "recursive make", that is, a hierarchy of subdirectories containing source files, where each subdirectory is independently built. Unless each subdirectory is fully independent, this is a mistake, because the dependency information is incorrect.

[dependancy]: 构建基于 Go modules，Makefile 对每个目标直接调用 go build，不存在递归 make 造成的交叉依赖问题。https://github.com/karmada-io/karmada/blob/master/Makefile ; https://github.com/karmada-io/karmada/blob/master/hack/build.sh
### [Unmet] [MUST]
The project MUST be able to repeat the process of generating information from source files and get exactly the same bit-for-bit result. If no building occurs (e.g., scripting languages where the source code is used directly instead of being compiled), select "not applicable" (N/A). [build_repeatable]

GCC and clang users may find the -frandom-seed option useful; in some cases, this can be resolved by forcing some sort order. More suggestions can be found at the reproducible build site.

[dependancy]: hack/util.sh 的 version_ldflags 注入 BUILDDATE（当前时间戳）且未使用 -trimpath/-buildid 固定，CI 也没有可复现构建校验，因此不能保证“逐位相同”的可重复构建。https://github.com/karmada-io/karmada/blob/master/hack/util.sh
## Installation system

### [Met] [MUST]
The project MUST provide a way to easily install and uninstall the software produced by the project using a commonly-used convention. [installation_common]

Examples include using a package manager (at the system or language level), "make install/uninstall" (supporting DESTDIR), a container in a standard format, or a virtual machine image in a standard format. The installation and uninstallation process (e.g., its packaging) MAY be implemented by a third party as long as it is FLOSS.

[dependancy]: 提供 Helm charts、karmada-operator、karmadactl（含 krew 索引）及 Docker 容器镜像等常见安装方式，均支持安装与卸载。https://github.com/karmada-io/karmada/tree/master/charts ; https://github.com/karmada-io/karmada/tree/master/operator ; https://karmada.io/docs/installation/
### [Met] [MUST]
The installation system for end-users MUST honor standard conventions for selecting the location where built artifacts are written to at installation time. For example, if it installs files on a POSIX system it MUST honor the DESTDIR environment variable. If there is no installation system or no standard convention, select "not applicable" (N/A). [installation_standard_variables]

[dependancy]: Helm chart 遵循 --namespace/values/release 等标准约定，operator 与 karmadactl 提供参数化安装位置与卸载流程，安装系统按标准约定选择产物写入位置。https://github.com/karmada-io/karmada/tree/master/charts/karmada ; https://github.com/karmada-io/karmada/tree/master/pkg/karmadactl
### [Met] [MUST]
The project MUST provide a way for potential developers to quickly install all the project results and support environment necessary to make changes, including the tests and test environment. This MUST be performed with a commonly-used convention. [installation_development_quick]

This MAY be implemented using a generated container and/or installation script(s). External dependencies would typically be installed by invoking system and/or language package manager(s), per external_dependencies.

[dependancy]: README 提供开发环境搭建步骤，hack/local-up-karmada.sh 一键启动本地控制面与成员集群，make test / make verify 可快速运行测试与校验，符合常用开发安装约定。https://github.com/karmada-io/karmada/blob/master/README.md ; https://github.com/karmada-io/karmada/blob/master/Makefile
## Externally-maintained components

### [Met] [MUST]
The project MUST list external dependencies in a computer-processable way. (URL required) [external_dependencies]

Typically this is done using the conventions of package manager and/or build system. Note that this helps implement installation_development_quick .

[dependancy]: go.mod/go.sum/vendor 以计算机可处理方式列出依赖，发布产物另附 SPDX SBOM（sbom-karmada.spdx）。https://github.com/karmada-io/karmada/blob/master/go.mod ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/release.yml
### [Met] [MUST]
Projects MUST monitor or periodically check their external dependencies (including convenience copies) to detect known vulnerabilities, and fix exploitable vulnerabilities or verify them as unexploitable. [dependency_monitoring]

This can be done using an origin analyzer / dependency checking tool / software composition analysis tool such as OWASP's Dependency-Check , Sonatype's Nexus Auditor , Synopsys' Black Duck Software Composition Analysis , and Bundler-audit (for Ruby) . Some package managers include mechanisms to do this. It is acceptable if the components' vulnerability cannot be exploited, but this analysis is difficult and it is sometimes easier to simply update or fix the part.

[dependancy]: CI 在 PR 合并后及每周定时对镜像执行 Trivy 漏洞扫描（覆盖 release-1.16/1.17/1.18 分支）并上传 SARIF 到 GitHub Security tab；FOSSA 负责依赖与许可证分析；SECURITY.md 记录依赖 CVE 处理政策。https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci-image-scanning.yaml ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/fossa.yml ; https://github.com/karmada-io/community/blob/main/security-team/SECURITY.md
### [Met] [MUST]
The project MUST either: make it easy to identify and update reused externally-maintained components; or use the standard components provided by the system or programming language. Then, if a vulnerability is found in a reused component, it will be easy to update that component. [updateable_reused_components]

A typical way to meet this criterion is to use system and programming language package management systems. Many FLOSS programs are distributed with "convenience libraries" that are local copies of standard libraries (possibly forked). By itself, that's fine. However, if the program *must* use these local (forked) copies, then updating the "standard" libraries as a security update will leave these additional copies still vulnerable. This is especially an issue for cloud-based systems; if the cloud provider updates their "standard" libraries but the program won't use them, then the updates don't actually help. See, e.g., "Chromium: Why it isn't in Fedora yet as a proper package" by Tom Callaway .

[dependancy]: 使用 Go modules + vendor 与标准语言包管理，Dependabot 自动更新 GitHub Actions/Docker 依赖（含 release 分支），SBOM 便于识别和更新被复用组件。https://github.com/karmada-io/karmada/blob/master/.github/dependabot.yml ; https://github.com/karmada-io/karmada/blob/master/go.mod
### [Met] [SHOULD]
The project SHOULD avoid using deprecated or obsolete functions and APIs where FLOSS alternatives are available in the set of technology it uses (its "technology stack") and to a supermajority of the users the project supports (so that users have ready access to the alternative). [interfaces_current]

[dependancy]: .golangci.yml 启用 modernize 与 staticcheck 全量检查，depguard 明确禁止已废弃/归档的 io/ioutil、gopkg.in/yaml.v3 等 API，体现避免过时接口的努力。https://github.com/karmada-io/karmada/blob/master/.golangci.yml
## Automated test suite

### [Met] [MUST]
An automated test suite MUST be applied on each check-in to a shared repository for at least one branch. This test suite MUST produce a report on test success or failure. [automated_integration_testing]

This requirement can be viewed as a subset of test_continuous_integration, but focused on just testing, without requiring continuous integration.

[dependancy]: CI Workflow 在 push/PR 上运行 lint、codegen、编译、单元测试与 e2e（k8s 1.34/1.35/1.36 矩阵），并上传 Codecov 报告，测试结果可见。https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci.yml
### [?] [MUST]
The project MUST add regression tests to an automated test suite for at least 50% of the bugs fixed within the last six months. [regression_tests_added50]

### [Unmet] [MUST]
The project MUST have FLOSS automated test suite(s) that provide at least 80% statement coverage if there is at least one FLOSS tool that can measure this criterion in the selected language. [test_statement_coverage80]

Many FLOSS tools are available to measure test coverage, including gcov/lcov, Blanket.js, Istanbul, JCov, and covr (R). Note that meeting this criterion is not a guarantee that the test suite is thorough, instead, failing to meet this criterion is a strong indicator of a poor test suite.

[dependancy]: Codecov 显示 master 分支当前语句覆盖率约 42%（2026-08-18 实测 badge 数值），低于 80% 阈值。https://codecov.io/gh/karmada-io/karmada ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci.yml
## New functionality testing

### [Met] [MUST]
The project MUST have a formal written policy that as major new functionality is added, tests for the new functionality MUST be added to an automated test suite. [test_policy_mandated]

[dependancy]: CONTRIBUTING.md 明确要求“develop the code/fix and add new test cases”，并需通过 make verify/make test，构成新增功能须补测试的书面政策。https://github.com/karmada-io/karmada/blob/master/CONTRIBUTING.md
### [Met] [MUST]
The project MUST include, in its documented instructions for change proposals, the policy that tests are to be added for major new functionality. [tests_documented_added]

However, even an informal rule is acceptable as long as the tests are being added in practice.

[dependancy]: 变更提案/贡献工作流文档（CONTRIBUTING.md）包含“新增主要功能须添加测试”的政策说明，PR 流程亦要求运行测试。https://github.com/karmada-io/karmada/blob/master/CONTRIBUTING.md
## Warning flags

### [Met] [MUST]
Projects MUST be maximally strict with warnings in the software produced by the project, where practical. [warnings_strict]

Some warnings cannot be effectively enabled on some projects. What is needed is evidence that the project is striving to enable warning flags where it can, so that errors are detected early.

[dependancy]: golangci-lint 启用 staticcheck（checks: all）与 revive 等规则并设置 max-issues 为 0，CI lint job 失败即阻断合并，体现尽量严格的警告策略。https://github.com/karmada-io/karmada/blob/master/.golangci.yml ; https://github.com/karmada-io/karmada/blob/master/hack/verify-staticcheck.sh
# Security

## Secure development knowledge

### [Met] [MUST]
The project MUST implement secure design principles (from "know_secure_design"), where applicable. If the project is not producing software, select "not applicable" (N/A). [implement_secure_design]

For example, the project results should have fail-safe defaults (access decisions should deny by default, and projects' installation should be secure by default). They should also have complete mediation (every access that might be limited must be checked for authority and be non-bypassable). Note that in some cases principles will conflict, in which case a choice must be made (e.g., many mechanisms can make things more complex, contravening "economy of mechanism" / keep it simple).

[dependancy]: 安全自评与官方文档体现最小权限 RBAC、验证/变更 webhook、证书框架、TLS 默认安全、组件权限最小化等安全设计原则的应用。https://github.com/karmada-io/community/blob/main/security-team/assessments/self-assessment.md ; https://karmada.io/docs/administrator/security/component-permission/
## Use basic good cryptographic practices

### [Met] [MUST]
The default security mechanisms within the software produced by the project MUST NOT depend on cryptographic algorithms or modes with known serious weaknesses (e.g., the SHA-1 cryptographic hash algorithm or the CBC mode in SSH). [crypto_weaknesses]

Concerns about CBC mode in SSH are discussed in CERT: SSH CBC vulnerability .

[dependancy]: 官方部署为 apiserver/search/metrics-adapter 等设置最低 TLS 1.3，TLS 栈来自 Go/Kubernetes 成熟实现；发布校验使用 SHA-256 与 cosign/SLSA，未发现默认依赖 MD5/SHA-1/RC4/单 DES 等已知严重弱点。https://karmada.io/docs/administrator/security/security-considerations/#tls-configuration ; https://karmada.io/docs/administrator/security/verify-artifacts/
### [Met] [SHOULD]
The project SHOULD support multiple cryptographic algorithms, so users can quickly switch if one is broken. Common symmetric key algorithms include AES, Twofish, and Serpent. Common cryptographic hash algorithm alternatives include SHA-2 (including SHA-224, SHA-256, SHA-384 AND SHA-512) and SHA-3. [crypto_algorithm_agility]

[dependancy]: 组件支持 --tls-min-version 与 --cipher-suites 等参数，用户无需重编译即可切换 TLS 版本与算法套件。https://karmada.io/docs/administrator/security/security-considerations/#tls-configuration ; https://github.com/karmada-io/karmada/tree/master/docs/command-line-flags
### [Met] [MUST]
The project MUST support storing authentication credentials (such as passwords and dynamic tokens) and private cryptographic keys in files that are separate from other information (such as configuration files, databases, and logs), and permit users to update and replace them without code recompilation. If the project never processes authentication credentials and private cryptographic keys, select "not applicable" (N/A). [crypto_credential_agility]

[dependancy]: 凭证存于 kubeconfig、Kubernetes Secret 及独立证书/密钥文件；证书框架与轮换机制支持不重新编译代码即可更新替换凭证。https://karmada.io/docs/administrator/security/cert-framework/ ; https://karmada.io/docs/administrator/security/certificate-rotation/overview/
### [Met] [SHOULD]
The software produced by the project SHOULD support secure protocols for all of its network communications, such as SSHv2 or later, TLS1.2 or later (HTTPS), IPsec, SFTP, and SNMPv3. Insecure protocols such as FTP, HTTP, telnet, SSLv3 or earlier, and SSHv1 SHOULD be disabled by default, and only enabled if the user specifically configures it. If the software produced by the project does not support network communications, select "not applicable" (N/A). [crypto_used_network]

[dependancy]: 控制面 API、聚合 API、webhook、scheduler-estimator 与 agent 等通信基于 HTTPS/TLS/mTLS，默认部署不依赖 FTP/telnet/SSLv3/SSHv1 等不安全协议。https://karmada.io/docs/administrator/security/security-considerations/ ; https://github.com/karmada-io/community/blob/main/security-team/assessments/self-assessment.md
### [Met] [SHOULD]
The software produced by the project SHOULD, if it supports or uses TLS, support at least TLS version 1.2. Note that the predecessor of TLS was called SSL. If the software does not use TLS, select "not applicable" (N/A). [crypto_tls12]

[dependancy]: 官方安全文档为 karmada-apiserver/aggregated-apiserver/search/metrics-adapter 设置 --tls-min-version=VersionTLS13，高于最低 TLS 1.2 要求。https://karmada.io/docs/administrator/security/security-considerations/#tls-configuration
### [Met] [MUST]
The software produced by the project MUST, if it supports TLS, perform TLS certificate verification by default when using TLS, including on subresources. If the software does not use TLS, select "not applicable" (N/A). [crypto_certificate_verification]

Note that incorrect TLS certificate verification is a common mistake. For more information, see "The Most Dangerous Code in the World: Validating SSL Certificates in Non-Browser Software" by Martin Georgiev et al. and "Do you trust this application?" by Michael Catanzaro .

[dependancy]: 组件基于 Go crypto/tls 与 client-go/kubeconfig 默认校验服务器证书；InsecureSkipVerify 仅出现在用户显式配置的 cluster proxy（InsecureSkipTLSVerification）与 gRPC（InsecureSkipServerVerify）路径，非默认行为。https://github.com/karmada-io/karmada/blob/master/pkg/util/proxy/proxy.go ; https://github.com/karmada-io/karmada/blob/master/pkg/util/grpcconnection/config.go
### [Met] [MUST]
The software produced by the project MUST, if it supports TLS, perform certificate verification before sending HTTP headers with private information (such as secure cookies). If the software does not use TLS, select "not applicable" (N/A). [crypto_verification_private]

[dependancy]: Go HTTP transport 在 TLS 握手与证书验证成功后才发送请求头，Karmada 复用标准 client-go transport，未发现先发送敏感 header 再验证证书的自定义网络栈。https://github.com/karmada-io/karmada/tree/master/pkg/util ; https://karmada.io/docs/administrator/security/cert-framework/
## Secure release

### [Met] [MUST]
The project MUST cryptographically sign releases of the project results intended for widespread use, and there MUST be a documented process explaining to users how they can obtain the public signing keys and verify the signature(s). The private key for these signature(s) MUST NOT be on site(s) used to directly distribute the software to the public. If releases are not intended for widespread use, select "not applicable" (N/A). [signed_releases]

The project results include both source code and any generated deliverables where applicable (e.g., executables, packages, and containers). Generated deliverables MAY be signed separately from source code. These MAY be implemented as signed git tags (using cryptographic digital signatures). Projects MAY provide generated results separately from tools like git, but in those cases, the separate results MUST be separately signed.

[dependancy]: v1.7+ 使用 Cosign keyless（OIDC）签名发布镜像；v1.10.3+ 发布附 SLSA provenance（karmada-cli/crds/charts/sbom.intoto.jsonl）与 sha256 校验和；官网提供 cosign verify 与 slsa-verifier 的完整验证命令，私钥不存放于分发站点。https://karmada.io/docs/administrator/security/verify-artifacts/ ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/release.yml ; https://github.com/karmada-io/karmada/releases/tag/v1.18.2
### [Unmet] [SHOULD]
It is SUGGESTED that in the version control system, each important version tag (a tag that is part of a major release, minor release, or fixes publicly noted vulnerabilities) be cryptographically signed and verifiable as described in signed_releases . [version_tags_signed]

[dependancy]: 实测 v1.18.2 为 lightweight tag（git cat-file -t 返回 commit，指向一个由 GitHub 签名过的 commit），tag 对象本身未经 GPG/SSH/Sigstore 签名，且无 git tag -v 验证说明；该 SHOULD 项暂记 Unmet。https://github.com/karmada-io/karmada/releases/tag/v1.18.2 ; https://github.com/karmada-io/karmada/tags
## Other security issues

### [?] [MUST]
The project results MUST check all inputs from potentially untrusted sources to ensure they are valid (an *allowlist*), and reject invalid inputs, if there are any restrictions on the data at all. [input_validation]

Note that comparing input against a list of "bad formats" (aka a *denylist*) is normally not enough, because attackers can often work around a denylist. In particular, numbers are converted into internal formats and then checked if they are between their minimum and maximum (inclusive), and text strings are checked to ensure that they are valid text patterns (e.g., valid UTF-8, length, syntax, etc.). Some data may need to be "anything at all" (e.g., a file uploader), but these would typically be rare.

### [Met] [SHOULD]
Hardening mechanisms SHOULD be used in the software produced by the project so that software defects are less likely to result in security vulnerabilities. [hardening]

Hardening mechanisms may include HTTP headers like Content Security Policy (CSP), compiler flags to mitigate attacks (such as -fstack-protector), or compiler flags to eliminate undefined behavior. For our purposes least privilege is not considered a hardening mechanism (least privilege is important, but separate).

[dependancy]: artifacts/deploy 与 chart 为控制面组件设置 allowPrivilegeEscalation: false 与 seccompProfile（RuntimeDefault），构建禁用 CGO（CGO_ENABLED=0），符合加固要求。https://github.com/karmada-io/karmada/tree/master/artifacts/deploy ; https://github.com/karmada-io/karmada/blob/master/hack/build.sh
### [Unmet] [MUST]
The project MUST provide an assurance case that justifies why its security requirements are met. The assurance case MUST include: a description of the threat model, clear identification of trust boundaries, an argument that secure design principles have been applied, and an argument that common implementation security weaknesses have been countered. (URL required) [assurance_case]

An assurance case is "a documented body of evidence that provides a convincing and valid argument that a specified set of critical claims regarding a system’s properties are adequately justified for a given application in a given environment" ( "Software Assurance Using Structured Assurance Case Models", Thomas Rhodes et al, NIST Interagency Report 7608 ). Trust boundaries are boundaries where data or execution changes its level of trust, e.g., a server's boundaries in a typical web application. It's common to list secure design principles (such as Saltzer and Schroeer) and common implementation security weaknesses (such as the OWASP top 10 or CWE/SANS top 25), and show how each are countered. The BadgeApp assurance case may be a useful example. This is related to documentation_security, documentation_architecture, and implement_secure_design.

[dependancy]: 安全自评的 Non-goals 为空，未完整给出威胁模型、明确信任边界，以及“安全需求→设计原则→常见弱点→控制/测试证据”的论证链，因此现有材料还不能视为满足定义的 assurance case。https://github.com/karmada-io/community/blob/main/security-team/assessments/self-assessment.md ; https://github.com/karmada-io/community/blob/main/security-team/assessments/OSTIF-Karmada-Report.pdf
# Analysis

## Static code analysis

### [Met] [MUST]
The project MUST use at least one static analysis tool with rules or approaches to look for common vulnerabilities in the analyzed language or environment, if there is at least one FLOSS tool that can implement this criterion in the selected language. [static_analysis_common_vulnerabilities]

Static analysis tools that are specifically designed to look for common vulnerabilities are more likely to find them. That said, using any static tools will typically help find some problems, so we are suggesting but not requiring this for the 'passing' level badge.

[dependancy]: .golangci.yml 启用 gosec（针对常见漏洞模式的 Go 安全规则）与 staticcheck，CI 通过 golangci-lint run 持续强制执行。https://github.com/karmada-io/karmada/blob/master/.golangci.yml ; https://github.com/karmada-io/karmada/blob/master/hack/verify-staticcheck.sh
## Dynamic code analysis

### [N/A] [MUST]
If the software produced by the project includes software written using a memory-unsafe language (e.g., C or C++), then at least one dynamic tool (e.g., a fuzzer or web application scanner) MUST be routinely used in combination with a mechanism to detect memory safety problems such as buffer overwrites. If the project does not produce software written in a memory-unsafe language, choose "not applicable" (N/A). [dynamic_analysis_unsafe]

Examples of mechanisms to detect memory safety problems include Address Sanitizer (ASAN) (available in GCC and LLVM), Memory Sanitizer , and valgrind . Other potentially-used tools include thread sanitizer and undefined behavior sanitizer . Widespread assertions would also work.
[dependancy]: 项目交付软件以 Go 为主，hack/build.sh 显式设置 CGO_ENABLED=0，未包含由项目维护并交付的 C/C++ 内存不安全代码，故按官方规则选 N/A。https://github.com/karmada-io/karmada ; https://github.com/karmada-io/karmada/blob/master/hack/build.sh
