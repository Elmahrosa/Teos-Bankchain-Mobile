## Current Governance Status

- Founder-led development
- No external contributors
- No DAO active at this stage

The project is in **pre-institutional phase** and preparing for international exposure, including **Consensus Hong Kong (HK)**.

# Governance Charter — TEOS BankChain Mobile 🏛️🌍

⚠️ **Private Repository — Restricted to Partner Banks Only**  
Access is limited to financial institutions operating under direct agreement with TEOS Egypt.  
Redistribution or public disclosure is prohibited.

---

## 📌 Purpose
This charter consolidates all governance policies for TEOS BankChain Mobile.  
It unifies **contribution rules, conduct standards, security protocols, and compliance frameworks** into a single reference for partner banks, regulators, and institutions.

---

## 🤝 Contribution Governance
- All contributions must follow **CONTRIBUTING.md** rules:
  - Work only in `feature/*` or `fix/*` branches.  
  - Submit PRs against `main` (protected).  
  - Ensure commits are **signed** (`git commit -S`).  
  - Document compliance impact in PR descriptions.  
- CI/CD pipelines (`verify.yml`, `ci.yml`, `codeql.yml`) must pass before merge.  
- Direct commits to `main` are prohibited.  

---

## 🧭 Code of Conduct
- Contributors must act with **integrity, professionalism, and respect**.  
- Confidentiality of repo contents is mandatory.  
- Harassment, discrimination, or disrespectful communication is prohibited.  
- Unauthorized redistribution or resale of TEOS Egypt IP is forbidden.  
- Violations may result in access revocation and legal enforcement.  

---

## 🛡️ Security Policy
- Vulnerabilities must be reported privately (see `SECURITY.md`).  
- No public issues or disclosures of security flaws.  
- Reports acknowledged within **48–72 hours**; critical issues patched immediately.  
- Scope includes backend (FastAPI), mobile (Expo/React Native), and CI/CD.  
- Audit logs preserved for all development activity.  
- Secrets, credentials, or sensitive data must never be committed.  

---

## ⚖️ Compliance Framework
- **KYC (Know Your Customer):** mandatory identity verification for all customers.  
- **AML (Anti‑Money Laundering):** continuous monitoring, sanctions/PEP screening, SAR reporting.  
- **Audit Logging:** immutable, cryptographically hashed records for every API call.  
- **Regulatory Reporting:** automated exports for CBE, SAMA, FCA, FATF.  
- **Retention:** 7‑year regulator storage, 10‑year SAR artefacts, AES‑256 encryption at rest.  
- **Access Control:** RBAC + MFA; privileged ops require break‑glass justification.  

---

## 📑 Institutional Checklist
- Signed NDA & License Agreement.  
- Compliance checklist validated (KYC/AML, audit, reporting).  
- Technical integration report (sandbox → production).  
- Regulator acceptance letter (where applicable).  
- Bank onboarding confirmation memo.  

---

## 🧪 Governance Enforcement
- All governance rules are binding under TEOS Egypt’s compliance framework.  
- Violations may result in:
  - Immediate revocation of repository access.  
  - Termination of partnership agreements.  
  - Legal action under Egyptian jurisdiction (Alexandria courts).  

---

## 📞 Contact
**TEOS Egypt — Governance & Compliance Team**  
📧 compliance@teos-egypt.internal *(private partner channel only)*  
📱 WhatsApp: +20 100 616 7293  
🔗 [LinkedIn: Ayman Seif](https://www.linkedin.com/in/aymanseif/)

---

## 🔁 Change Log
- `2025-11-30` — Initial unified governance charter (CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, COMPLIANCE).
