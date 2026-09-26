<p align="center">
  <img src="assets/profile-hero.svg" alt="王治凯 个人介绍横幅" width="100%" />
</p>

<p align="center">
  <b><a href="README.md">English</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.zh-CN.md">简体中文</a></b>
</p>

# 王治凯 (Chih-Kai Wang)

> **致力于构建可验证的自主 Agent 架构、内核沙箱运行环境与形式化数学证明系统。**  
> *Building verifiable agent systems, sandboxed execution runtimes, and formal mathematics tools.*

国立台北教育大学（NTUE）数学暨信息教育学系 数学组，预计 2028 年毕业。现居台湾台北。  
专注于自主 AI 智能体系统工程、形式化定理证明（Lean 4）、进程沙箱隔离与确定性软件工程。

[📑 简历下载 (CV)](cv/Chih-Kai-Wang-CV.pdf) · [🐙 GitHub](https://github.com/f0909172434) · [✉️ 电子邮箱](mailto:f0909172434@gmail.com)

---

## 🌟 精选核心研究与工程项目

### 🤖 自主 Agent 架构与沙箱运行环境
- **[DSH Architecture Lab](https://github.com/f0909172434/dsh-architecture-lab)**  
  *面向 DeepSeek Harness 的生产级自主 Agent 架构研究实验室。*  
  具备 Lima Linux 虚拟机内核隔离、微美分级 Token 费用扣款拦截审计、不可变加密研究协议（`review-protocol.json`），以及覆盖记忆与规划四大配方（A/B/C/D）的阶乘实证研究。已验证 DeepSeek-V4.1-Flash 达到 100% 外部测试通过率。
- **[RuleShift](https://github.com/f0909172434/ruleshift)**  
  *评估 Agent 记忆在动态规则变更下适应能力的确定性本地测试床。*  
  涵盖 800 次配对任务、自动化世界状态验证与可重放证据。实证发现基础按需检索（Retrieval）以更低调用成本达到与选择性更新相同的高成功率（95.6%），提供极具性价比的架构选型。
- **[DSH Second Agent Kit](https://github.com/f0909172434/dsh-second-agent-kit)**  
  *DeepSeek Harness 的 macOS 纵深防御安全与记忆隔离套件。*  
  结合 macOS Seatbelt 内核沙箱配置文件（限制 IP 网络、开放本地 Socket 通信）、交互操作熔断保护（防死锁安全机制），以及基于 `AsyncLocalStorage` 的项目记忆动态隔离。
- **[MiniHarness](https://github.com/f0909172434/miniharness)**  
  *8 步骤深入学习 AI Agent Harness 系统架构的 Python 实战工作坊。*  
  提供零外部依赖的本地学习路径，从工具分发、Agent 循环到记忆宫殿与生产级架构，附带完整的中文前置教材与体系图。
- **[Verified Search Plugin](https://github.com/f0909172434/dsh-plugin-verified-search)**  
  *DeepSeek Harness 的可审计现况来源检索与抗幻觉验证插件。*  
  由 250+ 项确定性测试与 42 组冻结语料库验证，支持结构化 JSON 提取与显式证据缺口标记（`unresolved`），从根源防止模型产生无根据的推论。

---

### 📐 形式化数学与自动定理证明
- **[ProofWeave Core](https://github.com/f0909172434/proofweave-math-lab)**  
  *由 Lean 4 内核驱动的结构化数学主张验证平台。*  
  将结构化数学证明转化为透明可审计的认证流程，严谨分离“形式证明有效性”（由 Lean 4 内核验证）与“语义陈述对齐范围”，具备确定性计算预算。
- **[SAIR Proof Press](https://github.com/f0909172434/sair-stage2-proof-press)**  
  *等式推论求解器与 Lean 4 形式化证书产出伴随项目。*  
  提供公开伴随数据集、不可变基准产物、发布输入评估套件，以及完整的英文学术研究论文。
- **[Finite Witness](https://github.com/f0909172434/finite-witness-webmcp)**  
  *集成 WebMCP 的有限图有界反例搜索工具。*  
  具备有界穷举搜索、纯前端浏览器数据主权、可检视证书，以及完全独立的 Python 重播验证器。

---

### 🛡️ 软件工程质量、CI 凭据与可重现性
- **[HonestCI](https://github.com/f0909172434/honest-ci)**  
  *让绿灯 CI 真正代表测试如实执行的开发者 GitHub Action 与 CLI。*  
  封装测试命令、验证新鲜且未损坏的 JUnit XML 凭据、防范测试数量相对默认分支异常下降，并能警告 GitHub Actions 中可疑的假绿灯写法（已发布于 npm 与 GitHub Marketplace，版本 `v1.0.4`）。
- **[RigorGraph](https://github.com/f0909172434/rigorgraph)**  
  *本地优先的主张-证据 DAG 图谱与确定性审计报告系统。*  
  实现四眼审核原则（作者与独立审查者职责分离）、DAG 环状依赖检测、SHA-256 字节数字指纹，并能导出离线独立 HTML 审查文件。

---

### 🔬 交互式 AI 探索与特色工具
- **[TokenScope](https://github.com/f0909172434/tokenscope)**  
  *因果注意力矩阵、Token 采样与 BPE 的双语交互浏览器实验室。*  
  具备可检查的 $5 \times 5$ 自注意力矩阵、温度／top-k／top-p 概率分布控制，以及完全可反转的 Unicode BPE 分词器。
- **[Charlie Alpha 4B](https://github.com/f0909172434/Charlie-Alpha-4B)**  
  *专为 Apple Silicon MLX 优化的三语统计程序选择辅助模型。*  
  提供可重现的统计决策建议，内置审慎澄清机制（`needs_clarification`），避免在信息不足时做出武断推断。
- **[DeepSeek Girl Pets](https://github.com/f0909172434/deepseek-girl-codex-pet)**  
  *DeepSeek Harness 与 Codex Desktop 的 16 方向动态视线追踪桌面宠物扩展。*  
  纯净无痕设计、零 DOM 污染、官方生命周期钩子同步，且 100% 本地离线运行保障隐私。

---

## 🛠️ 技术专业与技术栈

| 领域分类 | 核心技术、语言与框架 |
| :--- | :--- |
| **编程语言** | Python, TypeScript, JavaScript (Node.js 20+), Lean 4, SQL, Bash/Zsh |
| **Agent 与系统工程** | DeepSeek Harness, Model Context Protocol (MCP), WebMCP, Tool Calling Loops, 记忆宫殿 |
| **沙箱与进程隔离** | Lima Linux VM, Docker, macOS Seatbelt (`sandbox-exec`), 进程组隔离, 熔断控制器 |
| **形式化方法与数学** | Lean 4 & Mathlib, 形式证明辅助器, 等式逻辑, 有限图搜索, 近世代数 |
| **AI 与机器学习** | Apple Silicon MLX, PyTorch, 因果自注意力机制, BPE 分词技术, 本地 LLM 量化推理 |
| **软件质量与基础设施** | GitHub Actions CI/CD, HonestCI, JUnit XML 标准, Vitest / Pytest, Prettier / ESLint / Ruff |

---

## 💡 核心工程哲学

1. **证据紧随主张（Keep Evidence Attached to Claims）**：没有可计算凭据的推论仅为猜想。每一项技术结论都必须由可重放的实证或形式化凭证支撑。
2. **纵深防御与失效闭锁（Defense-in-Depth & Fail-Closed Design）**：安全沙箱边界、Token 费用上限与执行超时保护皆必须具备失效闭锁机制，在异常发生时第一时间内守护系统安全与资源。
3. **确定性与离线可重现（Determinism & Reproducibility）**：研究工具与评测基准坚持支持 100% 离线执行与固定种子，摆脱对外部网络环境不可控波动的依赖。
4. **积极正向的开源工艺（Constructive Open-Source Craftsmanship）**：以清晰的人话沟通架构思维，通过透明可审计的工程实践赋能开发者与社区。

---

<p align="center">
  <sub>在台北精心打造 · 热忱欢迎软件工程与 AI 研究实习合作机会。</sub>
</p>
