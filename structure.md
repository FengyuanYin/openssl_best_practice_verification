### [Met] [MUST]
The project MUST achieve a passing level badge. [achieve_passing]
[dependancy]: OpenSSF Best Practices 项目 #5301 显示 Karmada 徽章级别为 passing，2022-01-21 获得且从未失去（badge_level=passing, achieved_passing_at=2022-01-21, lost_passing_at=null）。https://www.bestpractices.dev/en/projects/5301 ; https://www.bestpractices.dev/en/projects/5301.json

### [Met] [MUST]
The information on how to contribute MUST include the requirements for acceptable contributions (e.g., a reference to any required coding standard). [contribution_requirements]
[dependancy]: CONTRIBUTING.md 明确 PR 提交流程，要求提交前通过 make verify 与 make test，并要求遵循 Go CodeReviewComments 编码规范，满足“可接受贡献要求”的文档要求。https://github.com/karmada-io/karmada/blob/master/CONTRIBUTING.md

### [Unmet] [SHOULD]
The project SHOULD have a legal mechanism where all developers of non-trivial amounts of project software assert that they are legally authorized to make these contributions. The most common and easily-implemented approach for doing this is by using a Developer Certificate of Origin (DCO) , where users add "signed-off-by" in their commits and the project links to the DCO website. However, this MAY be implemented as a Contributor License Agreement (CLA), or other legal mechanism. [dco]

The DCO is the recommended mechanism because it's easy to implement, tracked in the source code, and git directly supports a "signed-off" feature using "commit -s". To be most effective it is best if the project documentation explains what "signed-off" means for that project. A CLA is a legal agreement that defines the terms under which intellectual works have been licensed to an organization or project. A contributor assignment agreement (CAA) is a legal agreement that transfers rights in an intellectual work to another party; projects are not required to have CAAs, since having CAA increases the risk that potential contributors will not contribute, especially if the receiver is a for-profit organization. The Apache Software Foundation CLAs (the individual contributor license and the corporate CLA) are examples of CLAs, for projects which determine that the risks of these kinds of CLAs to the project are less than their benefits.
[dependancy]: 主仓库 CONTRIBUTING.md 未采用或链接 DCO/CLA，未要求 git commit -s / Signed-off-by，CI 中也没有 DCO 检查；cncf_process 文档虽有 DCO 表述，但贡献者实际遵循的贡献指南未落实该机制。https://github.com/karmada-io/karmada/blob/master/CONTRIBUTING.md ; https://github.com/karmada-io/community/blob/main/cncf_process/incubation_dd/Karmada%20CNCF%20Due%20Diligence%20Doc.md
[improvement]: 在 CONTRIBUTING.md 与 PR 模板中明确采用 DCO：链接 https://developercertificate.org/，要求提交使用 git commit -s 添加 Signed-off-by 并解释其法律含义，同时启用 DCO 机器人（如 probot/dco）在 CI 中强制校验。

### [Met] [MUST]
The project MUST clearly define and document its project governance model (the way it makes decisions, including key roles). [governance]

There needs to be some well-established documented way to make decisions and resolve disputes. In small projects, this may be as simple as "the project owner and lead makes all final decisions". There are various governance models, including benevolent dictator and formal meritocracy; for more details, see Governance models . Both centralized (e.g., single-maintainer) and decentralized (e.g., group maintainers) approaches have been successfully used in projects. The governance information does not need to document the possibility of creating a project fork, since that is always possible for FLOSS projects.
[dependancy]: community/GOVERNANCE.md 公开定义了治理价值观、成员制、维护者选拔与投票、2/3 多数决策、懒人共识、CoC 处理、Security Response Team 与章程修改流程。https://github.com/karmada-io/community/blob/main/GOVERNANCE.md

### [Met] [MUST]
The project MUST adopt a code of conduct and post it in a standard location. [code_of_conduct]

Projects may be able to improve the civility of their community and to set expectations about acceptable conduct by adopting a code of conduct. This can help avoid problems before they occur and make the project a more welcoming place to encourage contributions. This should focus only on behavior within the community/workplace of the project. Example codes of conduct are the Linux kernel code of conduct , the Contributor Covenant Code of Conduct , the Debian Code of Conduct , the Ubuntu Code of Conduct , the Fedora Code of Conduct , the GNOME Code Of Conduct , the KDE Community Code of Conduct , the Python Community Code of Conduct , The Ruby Community Conduct Guideline , and The Rust Code of Conduct .
[dependancy]: 主仓库根目录标准位置存在 CODE_OF_CONDUCT.md，CONTRIBUTING.md 与 GOVERNANCE.md 均链接引用。https://github.com/karmada-io/karmada/blob/master/CODE_OF_CONDUCT.md

### [Met] [MUST]
The project MUST clearly define and publicly document the key roles in the project and their responsibilities, including any tasks those roles must perform. It MUST be clear who has which role(s), though this might not be documented in the same way. [roles_responsibilities]

The documentation for governance and roles and responsibilities may be in one place.
[dependancy]: community-membership.md 定义 Member/Reviewer/Approver/Maintainer 的职责、要求与权限；MAINTAINERS.md、APPROVERS.md、REVIEWERS.md 及仓库 OWNERS 文件公开了具体人员与职责范围。https://github.com/karmada-io/community/blob/main/community-membership.md ; https://github.com/karmada-io/community/blob/main/MAINTAINERS.md ; https://github.com/karmada-io/community/blob/main/APPROVERS.md

### [?] [MUST]
The project MUST be able to continue with minimal interruption if any one person dies, is incapacitated, or is otherwise unable or unwilling to continue support of the project. In particular, the project MUST be able to create and close issues, accept proposed changes, and release versions of software, within a week of confirmation of the loss of support from any one individual. This MAY be done by ensuring someone else has any necessary keys, passwords, and legal rights to continue the project. Individuals who run a FLOSS project MAY do this by providing keys in a lockbox and a will providing any needed legal rights (e.g., for DNS names). [access_continuity]

### [Met] [SHOULD]
The project SHOULD have a "bus factor" of 2 or more. [bus_factor]

A "bus factor" (aka "truck factor") is the minimum number of project members that have to suddenly disappear from a project ("hit by a bus") before the project stalls due to lack of knowledgeable or competent personnel. The truck-factor tool can estimate this for projects on GitHub. For more information, see Assessing the Bus Factor of Git Repositories by Cosentino et al.
[dependancy]: 13 名 active maintainers 来自华为、Bloomberg、字节跳动、阿里云、DaoCloud、CECloud、Trip.com 等多个组织，另有 27 名 approver；单一组织或单一个人无法阻塞 issue/PR/发布。https://github.com/karmada-io/community/blob/main/MAINTAINERS.md ; https://github.com/karmada-io/community/blob/main/APPROVERS.md

### [Unmet] [MUST]
The project MUST have a documented roadmap that describes what the project intends to do and not do for at least the next year. [documentation_roadmap]

The project might not achieve the roadmap, and that's fine; the purpose of the roadmap is to help potential users and contributors understand the intended direction of the project. It need not be detailed.
[dependancy]: community/ROADMAP.md 目前仅描述“2026 feature plan”；以 2026-08-19 为审计日，其时间范围不足未来一整年，也未明确写出“不做什么”的边界，Pending 列表不能替代带时间范围的路线图。https://github.com/karmada-io/community/blob/main/ROADMAP.md
[improvement]: 将 community/ROADMAP.md 更新为覆盖审计日起至少一整年（至 2027-08 及以后）的分阶段计划，为每项计划写明时间窗与优先级，并明确列出排除在范围之外的工作。

### [Met] [MUST]
The project MUST include documentation of the architecture (aka high-level design) of the software produced by the project. If the project does not produce software, select "not applicable" (N/A). [documentation_architecture]

A software architecture explains a program's fundamental structures, i.e., the program's major components, the relationships among them, and the key properties of these components and relationships.
[dependancy]: README 提供架构图并说明控制面组件（API Server、Controller Manager、Scheduler、ETCD 等）；官网 core-concepts/architecture 与 security self-assessment 详述 Host/Member Cluster、Push/Pull 模式、组件关系与数据流。https://github.com/karmada-io/karmada/blob/master/README.md ; https://karmada.io/docs/core-concepts/architecture/ ; https://github.com/karmada-io/community/blob/main/security-team/assessments/self-assessment.md

### [Unmet] [MUST]
The project MUST document what the user can and cannot expect in terms of security from the software produced by the project (its "security requirements"). [documentation_security]

These are the security requirements that the software is intended to meet.
[dependancy]: security self-assessment 列出 Security Goals 与安全功能，但 Non-goals 章节为空，未完整说明用户“不能期待”的安全保障；官网 Security Considerations 主要是部署建议，未形成明确的 security requirements 文档（guarantees 与 non-guarantees）。https://github.com/karmada-io/community/blob/main/security-team/assessments/self-assessment.md ; https://karmada.io/docs/administrator/security/security-considerations/
[improvement]: 补全 self-assessment.md 的 Non-goals，并新增明确的 security requirements 文档（保证与非保证、信任边界、适用版本），在 SECURITY.md 与官网安全章节链接公开。

### [Met] [MUST]
The project MUST provide a "quick start" guide for new users to help them quickly do something with the software. [documentation_quick_start]

The idea is to show users how to get started and make the software do anything at all. This is critically important for potential users to get started.
[dependancy]: README 提供 Quick Start（hack/local-up-karmada.sh 一键部署 + 示例应用传播），官网 installation 文档提供 karmadactl/Helm/Operator 安装步骤。https://github.com/karmada-io/karmada/blob/master/README.md ; https://karmada.io/docs/installation/

### [Met] [MUST]
The project MUST make an effort to keep the documentation consistent with the current version of the project results (including software produced by the project). Any known documentation defects making it inconsistent MUST be fixed. If the documentation is generally current, but erroneously includes some older information that is no longer true, just treat that as a defect, then track and fix as usual. [documentation_current]

The documentation MAY include information about differences or changes between versions of the software and/or link to older versions of the documentation. The intent of this criterion is that an effort is made to keep the documentation consistent, not that the documentation must be perfect.
[dependancy]: 官网按版本维护文档（versions.json 含 v1.13-v1.18 及 next），文档源码在公开 website 仓库持续维护，缺陷通过 issue/PR 跟踪修复。https://karmada.io/docs/ ; https://github.com/karmada-io/website/blob/main/versions.json

### [Met] [MUST]
The project repository front page and/or website MUST identify and hyperlink to any achievements, including this best practices badge, within 48 hours of public recognition that the achievement has been attained. [documentation_achievements]

An achievement is any set of external criteria that the project has specifically worked to meet, including some badges. This information does not need to be on the project website front page. A project using GitHub can put achievements on the repository front page by adding them to the README file.
[dependancy]: 主仓库 README 顶部已展示并超链接 OpenSSF Best Practices 徽章（项目 #5301），另有 OpenSSF Scorecard、Codecov、FOSSA 等徽章，满足“识别并超链接成就”的要求。https://github.com/karmada-io/karmada/blob/master/README.md ; https://www.bestpractices.dev/en/projects/5301

### [?] [SHOULD]
The project (both project sites and project results) SHOULD follow accessibility best practices so that persons with disabilities can still participate in the project and use the project results where it is reasonable to do so. [accessibility_best_practices]

For web applications, see the Web Content Accessibility Guidelines (WCAG 2.0) and its supporting document Understanding WCAG 2.0 ; see also W3C accessibility information . For GUI applications, consider using the environment-specific accessibility guidelines (such as Gnome , KDE , XFCE , Android , iOS , Mac , and Windows ). Some TUI applications (e.g. `ncurses` programs) can do certain things to make themselves more accessible (such as `alpine`'s `force-arrow-cursor` setting). Most command-line applications are fairly accessible as-is. This criterion is often N/A, e.g., for program libraries. Here are some examples of actions to take or issues to consider: Provide text alternatives for any non-text content so that it can be changed into other forms people need, such as large print, braille, speech, symbols or simpler language ( WCAG 2.0 guideline 1.1 ) Color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element. ( WCAG 2.0 guideline 1.4.1 ) The visual presentation of text and images of text has a contrast ratio of at least 4.5:1, except for large text, incidental text, and logotypes ( WCAG 2.0 guideline 1.4.3 ) Make all functionality available from a keyboard (WCAG guideline 2.1) A GUI or web-based project SHOULD test with at least one screen-reader on the target platform(s) (e.g. NVDA, Jaws, or WindowEyes on Windows; VoiceOver on Mac & iOS; Orca on Linux/BSD; TalkBack on Android). TUI programs MAY work to reduce overdraw to prevent redundant reading by screen-readers.

### [Unmet] [SHOULD]
The software produced by the project SHOULD be internationalized to enable easy localization for the target audience's culture, region, or language. If internationalization (i18n) does not apply (e.g., the software doesn't generate text intended for end-users and doesn't sort human-readable text), select "not applicable" (N/A). [internationalization]

Localization "refers to the adaptation of a product, application or document content to meet the language, cultural and other requirements of a specific target market (a locale)." Internationalization is the "design and development of a product, application or document content that enables easy localization for target audiences that vary in culture, region, or language." (See W3C's "Localization vs. Internationalization" .) Software meets this criterion simply by being internationalized. No localization for another specific language is required, since once software has been internationalized it's possible for others to work on localization.
[dependancy]: 官网已做 i18n（提供中文文档等本地化内容），但 Karmada 核心软件与 karmadactl 面向用户的输出没有公开的 i18n/localization 框架或资源目录，不能认定“软件 produced by the project 已国际化”。https://github.com/karmada-io/karmada ; https://karmada.io/zh/docs/
[improvement]: 为 karmadactl 与核心面向用户输出建立系统化 i18n/本地化框架和资源目录，覆盖全部用户可见字符串并提供本地化入口。

### [N/A] [MUST]
If the project sites (website, repository, and download URLs) store passwords for authentication of external users, the passwords MUST be stored as iterated hashes with a per-user salt by using a key stretching (iterated) algorithm (e.g., Argon2id, Bcrypt, Scrypt, or PBKDF2). If the project sites do not store passwords for this purpose, select "not applicable" (N/A). [sites_password_security]

Note that the use of GitHub meets this criterion. This criterion only applies to passwords used for authentication of external users into the project sites (aka inbound authentication). If the project sites must log in to other sites (aka outbound authentication), they may need to store authorization tokens for that purpose differently (since storing a hash would be useless). This applies criterion crypto_password_storage to the project sites, similar to sites_https.
[dependancy]: Karmada 项目网站为静态文档站（Docusaurus），无外部用户密码认证；代码托管、issue 与贡献身份认证由 GitHub 提供，OpenSSF 注明“使用 GitHub 即满足本条”，因此触发条件不适用。https://karmada.io/ ; https://github.com/karmada-io/karmada

### [Met] [MUST]
The project MUST maintain the most often used older versions of the product or provide an upgrade path to newer versions. If the upgrade path is difficult, the project MUST document how to perform the upgrade (e.g., the interfaces that have changed and detailed suggested steps to help upgrade). [maintenance_or_update]
[dependancy]: SECURITY.md 声明维护最近三个 minor release 分支并回移适用修复；官网提供 Helm/Operator 升级路径与详细升级文档（含 API 与组件升级步骤）。https://github.com/karmada-io/community/blob/main/security-team/SECURITY.md ; https://karmada.io/docs/administrator/upgrading/

### [Met] [MUST]
The project MUST use an issue tracker for tracking individual issues. [report_tracker]
[dependancy]: 使用 GitHub Issues 跟踪问题，并提供 milestones 与 bug-report 模板。https://github.com/karmada-io/karmada/issues ; https://github.com/karmada-io/karmada/milestones

### [N/A] [MUST]
The project MUST give credit to the reporter(s) of all vulnerability reports resolved in the last 12 months, except for the reporter(s) who request anonymity. If there have been no vulnerabilities resolved in the last 12 months, select "not applicable" (N/A). [vulnerability_report_credit]
[dependancy]: 截至 2026-08-19，公开 Security Advisories 中最近一次已解决漏洞发布于 2025-01-03（CVE-2024-56513/56514），近 12 个月内无已解决漏洞，符合“无漏洞则 N/A”的条件；最终提交前请 Security Team 确认私有记录。https://github.com/karmada-io/karmada/security/advisories

### [Met] [MUST]
The project MUST have a documented process for responding to vulnerability reports. [vulnerability_response_process]

This is strongly related to vulnerability_report_process, which requires that there be a documented way to report vulnerabilities. It also related to vulnerability_report_response, which requires response to vulnerability reports within a certain time frame.
[dependancy]: SECURITY.md 与 security-release-process.md 公开了私密报告渠道（cncf-karmada-security@lists.cncf.io）、2 个工作日响应承诺、漏洞分级、embargo/CVE 流程、私有分发商列表与公开披露流程。https://github.com/karmada-io/community/blob/main/security-team/SECURITY.md ; https://github.com/karmada-io/community/blob/main/security-team/security-release-process.md

### [Met] [MUST]
The project MUST identify the specific coding style guides for the primary languages it uses, and require that contributions generally comply with it. [coding_standards]

In most cases this is done by referring to some existing style guide(s), possibly listing differences. These style guides can include ways to improve readability and ways to reduce the likelihood of defects (including vulnerabilities). Many programming languages have one or more widely-used style guides. Examples of style guides include Google's style guides and SEI CERT Coding Standards .
[dependancy]: CONTRIBUTING.md 要求遵循 Go CodeReviewComments 编码规范并撰写规范的 commit message。https://github.com/karmada-io/karmada/blob/master/CONTRIBUTING.md ; https://go.dev/wiki/CodeReviewComments

### [Met] [MUST]
The project MUST automatically enforce its selected coding style(s) if there is at least one FLOSS tool that can do so in the selected language(s). [coding_standards_enforced]

This MAY be implemented using static analysis tool(s) and/or by forcing the code through code reformatters. In many cases the tool configuration is included in the project's repository (since different projects may choose different configurations). Projects MAY allow style exceptions (and typically will); where exceptions occur, they MUST be rare and documented in the code at their locations, so that these exceptions can be reviewed and so that tools can automatically handle them in the future. Examples of such tools include ESLint (JavaScript), Rubocop (Ruby), and devtools check (R).
[dependancy]: CI golangci job 运行 hack/verify-staticcheck.sh（golangci-lint），启用 gofmt/goimports/gci 格式化与多类 lint，在 push/PR 强制通过。https://github.com/karmada-io/karmada/blob/master/.golangci.yml ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci.yml

### [Met] [MUST]
Build systems for native binaries MUST honor the relevant compiler and linker (environment) variables passed in to them (e.g., CC, CFLAGS, CXX, CXXFLAGS, and LDFLAGS) and pass them to compiler and linker invocations. A build system MAY extend them with additional flags; it MUST NOT simply replace provided values with its own. If no native binaries are being generated, select "not applicable" (N/A). [build_standard_variables]

It should be easy to enable special build features like Address Sanitizer (ASAN), or to comply with distribution hardening best practices (e.g., by easily turning on compiler flags to do so).
[dependancy]: Makefile 使用 GOOS/GOARCH/VERSION 等标准变量，hack/build.sh 将用户 LDFLAGS 附加到版本 ldflags 后传给 go build，而非覆盖用户值。https://github.com/karmada-io/karmada/blob/master/Makefile ; https://github.com/karmada-io/karmada/blob/master/hack/build.sh

### [Met] [SHOULD]
The build and installation system SHOULD preserve debugging information if they are requested in the relevant flags (e.g., "install -s" is not used). If there is no build or installation system (e.g., typical JavaScript libraries), select "not applicable" (N/A). [build_preserve_debug]

E.G., setting CFLAGS (C) or CXXFLAGS (C++) should create the relevant debugging information if those languages are used, and they should not be stripped during installation. Debugging information is needed for support and analysis, and also useful for measuring the presence of hardening features in the compiled binaries.
[dependancy]: 构建脚本未使用 -s/-w 剥离符号，仅注入 -X 版本变量，默认保留调试信息。https://github.com/karmada-io/karmada/blob/master/hack/build.sh ; https://github.com/karmada-io/karmada/blob/master/hack/util.sh

### [Met] [MUST]
The build system for the software produced by the project MUST NOT recursively build subdirectories if there are cross-dependencies in the subdirectories. If there is no build or installation system (e.g., typical JavaScript libraries), select "not applicable" (N/A). [build_non_recursive]

The project build system's internal dependency information needs to be accurate, otherwise, changes to the project may not build correctly. Incorrect builds can lead to defects (including vulnerabilities). A common mistake in large build systems is to use a "recursive build" or "recursive make", that is, a hierarchy of subdirectories containing source files, where each subdirectory is independently built. Unless each subdirectory is fully independent, this is a mistake, because the dependency information is incorrect.
[dependancy]: 根 Makefile 通过 go build 按 target 构建，无递归子目录 make 交叉依赖问题；Go module 单层构建。https://github.com/karmada-io/karmada/blob/master/Makefile

### [Unmet] [MUST]
The project MUST be able to repeat the process of generating information from source files and get exactly the same bit-for-bit result. If no building occurs (e.g., scripting languages where the source code is used directly instead of being compiled), select "not applicable" (N/A). [build_repeatable]

GCC and clang users may find the -frandom-seed option useful; in some cases, this can be resolved by forcing some sort order. More suggestions can be found at the reproducible build site.
[dependancy]: hack/util.sh 的 version_ldflags 注入 BUILDDATE=$(date -u ...) 时间戳，两次构建产物位级不同；未使用 SOURCE_DATE_EPOCH，也没有可复现构建文档。https://github.com/karmada-io/karmada/blob/master/hack/util.sh
[improvement]: 将构建改为确定性：以 SOURCE_DATE_EPOCH 固定 buildDate（或从版本/commit 派生），记录 go build 参数，发布可复现构建说明，并用同一提交两次构建比对验证 bit-for-bit 一致。

### [Met] [MUST]
The project MUST provide a way to easily install and uninstall the software produced by the project using a commonly-used convention. [installation_common]

Examples include using a package manager (at the system or language level), "make install/uninstall" (supporting DESTDIR), a container in a standard format, or a virtual machine image in a standard format. The installation and uninstallation process (e.g., its packaging) MAY be implemented by a third party as long as it is FLOSS.
[dependancy]: 提供 Helm charts、karmadactl/kubectl-karmada（krew 索引）、Karmada Operator、部署脚本与 OCI 镜像等常见安装/卸载方式。https://github.com/karmada-io/karmada/tree/master/charts ; https://karmada.io/docs/installation/

### [Met] [MUST]
The installation system for end-users MUST honor standard conventions for selecting the location where built artifacts are written to at installation time. For example, if it installs files on a POSIX system it MUST honor the DESTDIR environment variable. If there is no installation system or no standard convention, select "not applicable" (N/A). [installation_standard_variables]
[dependancy]: Helm charts 遵循 values/namespace 等标准约定，karmadactl init 与部署脚本支持标准环境变量（GOOS/GOARCH/REGISTRY/VERSION），安装位置与参数可通过标准约定配置。https://github.com/karmada-io/karmada/blob/master/Makefile ; https://github.com/karmada-io/karmada/tree/master/charts/karmada

### [Met] [MUST]
The project MUST provide a way for potential developers to quickly install all the project results and support environment necessary to make changes, including the tests and test environment. This MUST be performed with a commonly-used convention. [installation_development_quick]

This MAY be implemented using a generated container and/or installation script(s). External dependencies would typically be installed by invoking system and/or language package manager(s), per external_dependencies.
[dependancy]: README 提供本地开发环境一键脚本 hack/local-up-karmada.sh，Makefile 提供 make test/verify/all，开发者可快速搭建开发与测试环境。https://github.com/karmada-io/karmada/blob/master/README.md ; https://github.com/karmada-io/karmada/blob/master/Makefile

### [Met] [MUST]
The project MUST list external dependencies in a computer-processable way. [external_dependencies]

Typically this is done using the conventions of package manager and/or build system. Note that this helps implement installation_development_quick .
[dependancy]: 依赖以 go.mod/go.sum 与 vendor 目录管理，Helm charts 有依赖清单，发布附带 SPDX SBOM，均为计算机可处理格式。https://github.com/karmada-io/karmada/blob/master/go.mod ; https://github.com/karmada-io/karmada/tree/master/vendor

### [Met] [MUST]
Projects MUST monitor or periodically check their external dependencies (including convenience copies) to detect known vulnerabilities, and fix exploitable vulnerabilities or verify them as unexploitable. [dependency_monitoring]

This can be done using an origin analyzer / dependency checking tool / software composition analysis tool such as OWASP's Dependency-Check , Sonatype's Nexus Auditor , Synopsys' Black Duck Software Composition Analysis , and Bundler-audit (for Ruby) . Some package managers include mechanisms to do this. It is acceptable if the components' vulnerability cannot be exploited, but this analysis is difficult and it is sometimes easier to simply update or fix the part.
[dependancy]: CI 用 Trivy 对所有发布镜像扫描 CVE 并上传 SARIF 到 GitHub Security 标签；FOSSA 检查许可证合规；Dependabot 每周检查 GitHub Actions 与 Docker 依赖更新。https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci-image-scanning.yaml ; https://github.com/karmada-io/karmada/blob/master/.github/dependabot.yml

### [Met] [MUST]
The project MUST either: make it easy to identify and update reused externally-maintained components; or use the standard components provided by the system or programming language. Then, if a vulnerability is found in a reused component, it will be easy to update that component. [updateable_reused_components]

A typical way to meet this criterion is to use system and programming language package management systems. Many FLOSS programs are distributed with "convenience libraries" that are local copies of standard libraries (possibly forked). By itself, that's fine. However, if the program *must* use these local (forked) copies, then updating the "standard" libraries as a security update will leave these additional copies still vulnerable. This is especially an issue for cloud-based systems; if the cloud provider updates their "standard" libraries but the program won't use them, then the updates don't actually help. See, e.g., "Chromium: Why it isn't in Fedora yet as a proper package" by Tom Callaway .
[dependancy]: vendor + go.mod 使 Go 依赖可快速升级，Dependabot 自动提更新 PR，Trivy 扫描发现漏洞后可升级修复；镜像按 tag/digest 构建。https://github.com/karmada-io/karmada/blob/master/.github/dependabot.yml ; https://github.com/karmada-io/karmada/blob/master/go.mod

### [Met] [SHOULD]
The project SHOULD avoid using deprecated or obsolete functions and APIs where FLOSS alternatives are available in the set of technology it uses (its "technology stack") and to a supermajority of the users the project supports (so that users have ready access to the alternative). [interfaces_current]
[dependancy]: depguard 禁止 io/ioutil 与已归档的 gopkg.in/yaml.v3，modernize/staticcheck 规则检测过时用法；CI 校验 codegen/CRD/swagger/命令行 flag 文档一致，避免过期接口残留。https://github.com/karmada-io/karmada/blob/master/.golangci.yml ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci.yml

### [Met] [MUST]
An automated test suite MUST be applied on each check-in to a shared repository for at least one branch. This test suite MUST produce a report on test success or failure. [automated_integration_testing]

This requirement can be viewed as a subset of test_continuous_integration, but focused on just testing, without requiring continuous integration.
[dependancy]: ci.yml 在 push 与 PR 上运行 lint/codegen/build/单元测试（含覆盖率报告）与 E2E（Kubernetes v1.34-v1.36 矩阵），失败即阻断合并，并输出测试报告。https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci.yml

### [?] [MUST]
The project MUST add regression tests to an automated test suite for at least 50% of the bugs fixed within the last six months. [regression_tests_added50]

### [Unmet] [MUST]
The project MUST have FLOSS automated test suite(s) that provide at least 80% statement coverage if there is at least one FLOSS tool that can measure this criterion in the selected language. [test_statement_coverage80]

Many FLOSS tools are available to measure test coverage, including gcov/lcov, Blanket.js, Istanbul, JCov, and covr (R). Note that meeting this criterion is not a guarantee that the test suite is thorough, instead, failing to meet this criterion is a strong indicator of a poor test suite.
[dependancy]: Codecov 徽章显示 master 分支语句覆盖率为 42%（2026-08-19 抓取），低于 80% 门槛；Makefile 的 go test -coverprofile 上传 Codecov，未见其他达到 80% 的 FLOSS 覆盖率工具结果。https://codecov.io/gh/karmada-io/karmada ; https://github.com/karmada-io/karmada/blob/master/Makefile
[improvement]: 为 pkg/cmd/operator 等主要包补充单元测试并将语句覆盖率提升至 >=80%，在 CI 中加入覆盖率门禁（如 Codecov threshold），并在 README 公示最新覆盖率数值。

### [Met] [MUST]
The project MUST have a formal written policy that as major new functionality is added, tests for the new functionality MUST be added to an automated test suite. [test_policy_mandated]
[dependancy]: CONTRIBUTING.md 要求“为改动添加新测试用例”，proposal 模板要求说明测试策略，CI 强制单元与 E2E 测试通过，构成正式书面测试政策。https://github.com/karmada-io/karmada/blob/master/CONTRIBUTING.md ; https://github.com/karmada-io/karmada/blob/master/docs/proposals/proposal-template/proposal-template.md

### [Met] [MUST]
The project MUST include, in its documented instructions for change proposals, the policy that tests are to be added for major new functionality. [tests_documented_added]
[dependancy]: CONTRIBUTING.md 在 PR 流程中写明“请开发代码/修复并添加新测试用例”，并要求提交前运行 make test。https://github.com/karmada-io/karmada/blob/master/CONTRIBUTING.md

### [Met] [MUST]
Projects MUST be maximally strict with warnings in the software produced by the project, where practical. [warnings_strict]
[dependancy]: golangci-lint 严格配置（max-issues-per-linter=0）、staticcheck all、gofmt/goimports/gci，并在 CI golangci job 强制通过；Go 编译默认即严格。https://github.com/karmada-io/karmada/blob/master/.golangci.yml

### [Met] [MUST]
The project MUST implement secure design principles (from "know_secure_design"), where applicable. If the project is not producing software, select "not applicable" (N/A). [implement_secure_design]

For example, the project results should have fail-safe defaults (access decisions should deny by default, and projects' installation should be secure by default). They should also have complete mediation (every access that might be limited must be checked for authority and be non-bypassable). Note that in some cases principles will conflict, in which case a choice must be made (e.g., many mechanisms can make things more complex, contravening "economy of mechanism" / keep it simple).
[dependancy]: security self-assessment 描述安全目标、关键/安全相关组件、Push/Pull 工作流与 TLS/mTLS 设计；2025-01 OSTIF 安全审计报告公开；Security Team 与响应流程已建立。https://github.com/karmada-io/community/blob/main/security-team/assessments/self-assessment.md ; https://github.com/karmada-io/community/blob/main/security-team/assessments/OSTIF-Karmada-Report.pdf

### [Met] [MUST]
The default security mechanisms within the software produced by the project MUST NOT depend on cryptographic algorithms or modes with known serious weaknesses (e.g., the SHA-1 cryptographic hash algorithm or the CBC mode in SSH). [crypto_weaknesses]
[dependancy]: 官方安全文档为 karmada-apiserver 等组件配置 --tls-min-version=VersionTLS13，etcd 密码套件取自 Go 安全套件列表，默认机制不依赖 MD5/SHA-1/RC4/3DES 等已知严重弱点算法。https://karmada.io/docs/administrator/security/security-considerations/ ; https://github.com/karmada-io/karmada/blob/master/artifacts/deploy/karmada-apiserver.yaml

### [Met] [SHOULD]
The project SHOULD support multiple cryptographic algorithms, so users can quickly switch if one is broken. Common symmetric key algorithms include AES, Twofish, and Serpent. Common cryptographic hash algorithm alternatives include SHA-2 (including SHA-224, SHA-256, SHA-384 AND SHA-512) and SHA-3. [crypto_algorithm_agility]
[dependancy]: 组件支持 --tls-min-version 与 --cipher-suites 配置多种现代密码套件，Go/Kubernetes TLS 栈支持多算法，证书框架允许更换证书与密钥算法。https://karmada.io/docs/administrator/security/security-considerations/ ; https://github.com/karmada-io/karmada/tree/master/pkg/util

### [Met] [MUST]
The project MUST support storing authentication credentials (such as passwords and dynamic tokens) and private cryptographic keys in files that are separate from other information (such as configuration files, databases, and logs), and permit users to update and replace them without code recompilation. If the project never processes authentication credentials and private cryptographic keys, select "not applicable" (N/A). [crypto_credential_agility]
[dependancy]: 凭据（kubeconfig、CA/证书、私钥）存放在独立文件（如 /etc/karmada/pki）或 Kubernetes Secret 中，证书框架与证书轮换文档支持无需重新编译即可更新凭据。https://karmada.io/docs/administrator/security/cert-framework/ ; https://karmada.io/docs/administrator/security/built-in-cert-rotation/

### [Met] [SHOULD]
The software produced by the project SHOULD support secure protocols for all of its network communications, such as SSHv2 or later, TLS1.2 or later (HTTPS), IPsec, SFTP, and SNMPv3. Insecure protocols such as FTP, HTTP, telnet, SSLv3 or earlier, and SSHv1 SHOULD be disabled by default, and only enabled if the user specifically configures it. If the software produced by the project does not support network communications, select "not applicable" (N/A). [crypto_used_network]
[dependancy]: 控制面 API、聚合 API、webhook、scheduler-estimator gRPC 与 agent 通信均基于 HTTPS/TLS/mTLS；默认部署不启用 FTP/telnet/SSLv3/SSHv1 等不安全协议。https://karmada.io/docs/administrator/security/security-considerations/ ; https://github.com/karmada-io/community/blob/main/security-team/assessments/self-assessment.md

### [Met] [SHOULD]
The software produced by the project SHOULD, if it supports or uses TLS, support at least TLS version 1.2. Note that the predecessor of TLS was called SSL. If the software does not use TLS, select "not applicable" (N/A). [crypto_tls12]
[dependancy]: 官方文档为 karmada-apiserver、aggregated-apiserver、search、metrics-adapter 配置最低 TLS 1.3（高于 1.2），Go 默认支持 TLS 1.2+。https://karmada.io/docs/administrator/security/security-considerations/#tls-configuration

### [Met] [MUST]
The software produced by the project MUST, if it supports TLS, perform TLS certificate verification by default when using TLS, including on subresources. If the software does not use TLS, select "not applicable" (N/A). [crypto_certificate_verification]

Note that incorrect TLS certificate verification is a common mistake. For more information, see "The Most Dangerous Code in the World: Validating SSL Certificates in Non-Browser Software" by Martin Georgiev et al. and "Do you trust this application?" by Michael Catanzaro .
[dependancy]: 证书框架为组件定义 CA/服务端/客户端证书信任链，client-go/kubeconfig 默认校验证书，scheduler-estimator gRPC 亦做证书校验；跳过校验必须显式配置而非默认行为。https://karmada.io/docs/administrator/security/cert-framework/ ; https://github.com/karmada-io/community/blob/main/security-team/assessments/self-assessment.md

### [Met] [MUST]
The software produced by the project MUST, if it supports TLS, perform certificate verification before sending HTTP headers with private information (such as secure cookies). If the software does not use TLS, select "not applicable" (N/A). [crypto_verification_private]
[dependancy]: Karmada 使用标准 Go/Kubernetes client-go transport，TLS 握手与证书校验成功后才发送 HTTP 请求头（含 bearer token/impersonation 等私密信息），无自定义“先发头后验证书”逻辑。https://github.com/karmada-io/karmada/tree/master/pkg/util ; https://karmada.io/docs/administrator/security/cert-framework/

### [Met] [MUST]
The project MUST cryptographically sign releases of the project results intended for widespread use, and there MUST be a documented process explaining to users how they can obtain the public signing keys and verify the signature(s). The private key for these signature(s) MUST NOT be on site(s) used to directly distribute the software to the public. If releases are not intended for widespread use, select "not applicable" (N/A). [signed_releases]

The project results include both source code and any generated deliverables where applicable (e.g., executables, packages, and containers). Generated deliverables MAY be signed separately from source code. These MAY be implemented as signed git tags (using cryptographic digital signatures). Projects MAY provide generated results separately from tools like git, but in those cases, the separate results MUST be separately signed.
[dependancy]: 自 v1.7 起镜像经 Cosign keyless 签名（dockerhub 发布工作流 COSIGN_EXPERIMENTAL=1），CLI/CRD/Chart/SBOM 附带 SLSA provenance（slsa-github-generator v2.1.0）；官网提供 cosign verify 与 slsa-verifier 完整验证命令，私钥不存放在分发站点。https://karmada.io/docs/administrator/security/verify-artifacts/ ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/release.yml ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/dockerhub-released-image.yml

### [Unmet] [SHOULD]
It is SUGGESTED that in the version control system, each important version tag (a tag that is part of a major release, minor release, or fixes publicly noted vulnerabilities) be cryptographically signed and verifiable as described in signed_releases . [version_tags_signed]
[dependancy]: 对最新发布 tag v1.18.2 执行 git cat-file -t 返回 commit，说明其为 lightweight tag 而非签名 annotated tag；仓库未提供 tag 级 GPG/SSH/Sigstore 签名与验证说明。https://github.com/karmada-io/karmada/releases/tag/v1.18.2 ; https://github.com/karmada-io/karmada/tags
[improvement]: 在发布流程中为重要版本创建签名 annotated tag（GPG/SSH/Sigstore），并在发布文档提供 git tag -v 或对应验证方法，确保 tag 对象本身可验证。

### [?] [MUST]
The project results MUST check all inputs from potentially untrusted sources to ensure they are valid (an *allowlist*), and reject invalid inputs, if there are any restrictions on the data at all. [input_validation]

Note that comparing input against a list of "bad formats" (aka a *denylist*) is normally not enough, because attackers can often work around a denylist. In particular, numbers are converted into internal formats and then checked if they are between their minimum and maximum (inclusive), and text strings are checked to ensure that they are valid text patterns (e.g., valid UTF-8, length, syntax, etc.). Some data may need to be "anything at all" (e.g., a file uploader), but these would typically be rare.

### [Met] [SHOULD]
Hardening mechanisms SHOULD be used in the software produced by the project so that software defects are less likely to result in security vulnerabilities. [hardening]

Hardening mechanisms may include HTTP headers like Content Security Policy (CSP), compiler flags to mitigate attacks (such as -fstack-protector), or compiler flags to eliminate undefined behavior. For our purposes least privilege is not considered a hardening mechanism (least privilege is important, but separate).
[dependancy]: 官方部署清单为控制面容器设置 allowPrivilegeEscalation: false 与 seccompProfile: RuntimeDefault；构建显式 CGO_ENABLED=0 减少内存不安全运行时面。https://github.com/karmada-io/karmada/tree/master/artifacts/deploy ; https://github.com/karmada-io/karmada/blob/master/hack/build.sh

### [Unmet] [MUST]
The project MUST provide an assurance case that justifies why its security requirements are met. The assurance case MUST include: a description of the threat model, clear identification of trust boundaries, an argument that secure design principles have been applied, and an argument that common implementation security weaknesses have been countered. [assurance_case]

An assurance case is "a documented body of evidence that provides a convincing and valid argument that a specified set of critical claims regarding a system’s properties are adequately justified for a given application in a given environment" ( "Software Assurance Using Structured Assurance Case Models", Thomas Rhodes et al, NIST Interagency Report 7608 ). Trust boundaries are boundaries where data or execution changes its level of trust, e.g., a server's boundaries in a typical web application. It's common to list secure design principles (such as Saltzer and Schroeer) and common implementation security weaknesses (such as the OWASP top 10 or CWE/SANS top 25), and show how each are countered. The BadgeApp assurance case may be a useful example. This is related to documentation_security, documentation_architecture, and implement_secure_design.
[dependancy]: self-assessment 有 actors/goals/安全功能清单与 OSTIF 审计，但缺少明确的威胁模型、完整信任边界识别、安全设计原则论证以及常见实现弱点（OWASP/CWE）映射；Non-goals 为空，不能视为完整的 assurance case。https://github.com/karmada-io/community/blob/main/security-team/assessments/self-assessment.md
[improvement]: 在 community/security-team/assessments/ 新增 assurance-case.md：威胁模型、逐项信任边界、安全 claim -> 设计原则 -> 常见弱点 -> 控制/测试证据的论证结构，经 Security Team 评审后以公开 URL 作为依据。

### [Met] [MUST]
The project MUST use at least one static analysis tool with rules or approaches to look for common vulnerabilities in the analyzed language or environment, if there is at least one FLOSS tool that can implement this criterion in the selected language. [static_analysis_common_vulnerabilities]
[dependancy]: .golangci.yml 启用 gosec（常见漏洞模式）与 staticcheck all，hack/verify-staticcheck.sh 在 CI golangci job 中执行，发现问题即非零退出阻断。https://github.com/karmada-io/karmada/blob/master/.golangci.yml ; https://github.com/karmada-io/karmada/blob/master/.github/workflows/ci.yml

### [N/A] [MUST]
If the software produced by the project includes software written using a memory-unsafe language (e.g., C or C++), then at least one dynamic tool (e.g., a fuzzer or web application scanner) MUST be routinely used in combination with a mechanism to detect memory safety problems such as buffer overwrites. If the project does not produce software written in a memory-unsafe language, choose "not applicable" (N/A). [dynamic_analysis_unsafe]
[dependancy]: Karmada 交付软件以 Go 编写（其余为 Shell/Makefile/Dockerfile 等非内存不安全语言），构建显式 CGO_ENABLED=0，不含 C/C++ 交付代码，内存不安全语言触发条件不适用。https://github.com/karmada-io/karmada/blob/master/hack/build.sh ; https://github.com/karmada-io/karmada
