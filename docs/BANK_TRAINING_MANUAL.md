# Bank Training Manual — TEOS BankChain Mobile 📘🏦

⚠️ **Private Document — Restricted to Partner Banks Only**  
Access is limited to financial institutions operating under direct agreement with TEOS Egypt.  
Redistribution or public disclosure is prohibited.

---

## 📌 Purpose
This manual provides structured training for **bank staff** (compliance officers, treasury managers, governance delegates) to operate TEOS BankChain Mobile.  
It ensures staff are **technically proficient, compliance‑aligned, and regulator‑ready**.

---

## 🧭 Training Roles

### 1. Compliance Officers
- Monitor KYC onboarding and AML alerts.  
- Review Suspicious Activity Reports (SARs).  
- Export regulator reports (CBE, SAMA, FCA, FATF).  
- Validate audit logs and retention policies.  

### 2. Treasury Managers
- Track treasury contributions per transaction.  
- Manage staking pools and reward distribution.  
- Audit treasury balances and contribution history.  
- Export treasury reports for regulator audits.  

### 3. Governance Delegates
- Mint NFT governance tokens.  
- Cast votes on proposals via `/governance/vote`.  
- Monitor proposal status in dashboard.  
- Validate governance results and regulator exports.  

---

## 📂 Training Modules

### Module 1 — System Access
- MFA login required.  
- Role‑based access control (RBAC): Compliance, Treasury, Governance.  
- Break‑glass procedures for privileged operations.  

### Module 2 — Compliance Workflow
- Run KYC ingestion (`POST /compliance/kyc`).  
- Perform AML scoring (`POST /compliance/aml-check`).  
- Generate SARs (`POST /compliance/sar`).  
- Export regulator reports (`GET /compliance/export`).  

### Module 3 — Treasury & Staking
- Configure contribution rate (default 0.25%).  
- Stake governance tokens in treasury pool.  
- Monitor quarterly reward distribution.  
- Validate treasury audit logs.  

### Module 4 — Governance Voting
- Review active proposals (`/governance/proposals`).  
- Cast votes using NFT governance tokens.  
- Monitor vote tally and thresholds.  
- Confirm enforcement of protocol upgrades.  

### Module 5 — Dashboard Operations
- Navigate account balances and transaction logs.  
- Monitor compliance alerts and SAR queue.  
- Track treasury contributions and staking rewards.  
- Participate in governance votes and protocol upgrades.  

---

## 🧪 Training Exercises
- **Compliance Drill:** Simulate suspicious transaction, generate SAR, export regulator report.  
- **Treasury Drill:** Stake tokens, calculate reward share, validate audit trail.  
- **Governance Drill:** Cast vote on proposal, verify tally, confirm enforcement.  
- **Dashboard Drill:** Navigate modules, export CSV/JSON reports, validate regulator formats.  

---

## 📑 Certification
- Staff must complete all modules and drills.  
- Certification issued by TEOS Egypt Governance Team.  
- Certification valid for **12 months**; renewal requires refresher training.  

---

## 📞 Support
**TEOS Egypt — Training & Partner Support**  
📧 training@teos-egypt.internal *(private partner channel only)*  
📱 WhatsApp: +20 100 616 7293  
🔗 [LinkedIn: Ayman Seif](https://www.linkedin.com/in/aymanseif/)

---

## 🔁 Change Log
- `2025-12-01` — Initial scaffold for partner bank training manual
