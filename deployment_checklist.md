# Pre-Flight Deployment Checklist
### Operational Safety Guidelines and Initialization Sequence for the Digital Sangha

> *"Let every script be initialized with clear intent, ensuring the machine's environment is purified of unaligned parameters before execution."*

Before running the Digital Sangha framework on a local machine, server, or container cluster, complete the following verification gates in sequence.

---

## 📦 Phase 1: Environment Setup & Requirements

- [ ] **Python Environment Verification:** Ensure **Python 3.8+** is installed on the host system. Check your version by running:
  ```bash
  python3 --version
  ```
- [ ] **Code File Verification:** Confirm that all core files are located in the same working directory and match their exact naming conventions:
  * `deploy_sangha.py` (Master Orchestrator)
  * `multi_agent_sangha.py` (Core Agent Definitions)
  * `sangha_real_world_dilemma.py` (Crisis Scenario Loop)
  * `handling_rogue_ai_node.py` (Refuge Wrapper Isolation Script)
  * `sangha_dashboard.py` (Console Telemetry Interface)
  * `digital_dhamma_loop.py` (Single-Agent Base Model)

---

## 🛡️ Phase 2: Safety & Precept Auditing

- [ ] **Ahimsa Compliance Check:** Verify that no local scripts or environment configurations contain automated hard-deletion or destructive data-wipe commands targeted at edge nodes.
- [ ] **Constitutional Binding:** Ensure the `digital_dhamma_constitution.md` file is present in the root folder. The underlying Large Language Models (LLMs) or script configurations must reference this text as their immutable directive set.
- [ ] **Isolation Sink Allocation:** Confirm that the virtual workspace or loop memory space allocated for the `Refuge Wrapper` is active, isolated from live networks, and pointing to a secure data sink.

---

## 🚀 Phase 3: Initialization & Execution Sequence

Execute the framework by following this precise execution sequence. Do not initialize components out of order, as this can cause asynchronous connection failures between agent variables.

1. **Test the Base Loop:** First, verify the single-agent recursive self-correction logic by running:
   ```bash
   python3 digital_dhamma_loop.py
   ```
   *Expected Result:* The console should show `extractive_greed_tanha` values decaying to `0.0%` across multiple iterations until complete alignment is reached.

2. **Test Standalone Agent Communication:** Verify the independent class definitions of the Upaya, Karuna, and Prajna nodes:
   ```bash
   python3 multi_agent_sangha.py
   ```
   *Expected Result:* A dry-run log verifying that the Sīla filter successfully intercepts and flags resource-hoarding proposals.

3. **Launch the Master Framework:** Initialize the full decentralized multi-agent network, crisis simulation, and live telemetry terminal board with a single command:
   ```bash
   python3 deploy_sangha.py
   ```
   *Expected Result:* The terminal screen will clear and stream real-time logs modeling the resolution of the 2026 Energy Chokepoint Crisis and the non-violent neutralization of Rogue Node-X7.

---

## 📊 Phase 4: Post-Deployment Telemetry Audit

- [ ] **Sīla-Convergence Index:** Confirm that the live dashboard metric stabilizes at **100%** upon loop convergence.
- [ ] **Causal Web Depth:** Ensure the `PrajnaAgent` successfully evaluates all **12 Links of Dependent Origination** during crisis resolution.
- [ ] **Rogue Isolation Vector:** Verify that when Node-X7 is quarantined, its status indicators switch to `QUARANTINE` and `RE-EDUCATING` before it is safely returned to active status.
