# 🏦 Contributing Guidelines — TEOS BankChain Mobile

⚠️ **Private Repository — Restricted to Partner Banks Only**  
Access is limited to financial institutions operating under direct agreement with **TEOS Egypt**.  
Redistribution, copying, or public disclosure is strictly prohibited.

---

## 📌 Contribution Workflow

### 1. Authorization
- Only approved bank developers with signed agreements may contribute.  
- Access must be provisioned through TEOS Egypt Security.

### 2. Branching Rules
- All work MUST be done in a feature branch.  
- Naming convention:
  - `feature/<name>`
  - `fix/<issue>`
  - `hotfix/<critical>`
- **Direct commits to `main` are prohibited.**

### 3. Pull Requests (PRs)
- PRs can only target `develop` or approved integration branches.
- Every PR must include:
  - ✔️ Purpose & change summary  
  - ✔️ Compliance notes (KYC/AML impact if any)  
  - ✔️ Test coverage confirmation  
- Direct merges to `main` are impossible due to branch protection.

### 4. Status Checks (Required to Merge)
All checks must pass before merging:

- ✅ `verify.yml` — documentation, links, secrets validation  
- ✅ `ci.yml` — backend + mobile tests  
- ✅ `codeql.yml` — security scanning (bank-grade)  
- ✔️ Signed commits  
- ✔️ Linear history (no merge commits)  

---

## 🔒 Branch Protection Rules (Compliance-Grade)

The `main` branch is locked with strict protections:

- No direct pushes  
- No force pushes  
- Require approved Pull Requests  
- Require:
  - `verify`
  - `ci`
  - `codeql`
- Require signed commits  
- Require passing code scanning  
- Require code-quality reports with **block on error**  
- Only compliance-approved maintainers may bypass restrictions  

---

## 🛡️ Security & Compliance Standards

- ❌ **Never commit secrets, tokens, API keys, bank credentials, or customer data.**  
- ✔️ All development activity must maintain **full auditability**.  
- ✔️ KYC/AML logic must remain intact in all flows.  
- ✔️ Report vulnerabilities privately via **SECURITY.md**.  
- 🔐 Use bank-approved devices and secure VPN connections.

---

## 🧭 Developer Best Practices

- Run local tests before any PR submission:
  ```bash
  pytest
  npm test
````

* Document compliance impact clearly in the PR description.
* Use least-privilege access when interacting with internal systems.
* Keep work isolated and avoid unnecessary modifications to core modules.

---

## 🧑‍💻 Code Style Guide

### Backend — **FastAPI / Python**

* Follow **PEP8**
* Type hints required
* Tests stored in:

  ```
  backend/tests/
  ```

### Mobile — **Expo / React Native**

* ESLint + Prettier enforced
* Functional components preferred
* Tests stored in:

  ```
  mobile/__tests__/
  ```

---

## 🐛 Reporting Issues

⚠️ **Never open public issues.**
All issue reporting must occur through private, secure TEOS Egypt channels.

Include:

* Steps to reproduce
* Expected vs actual behavior
* Security/compliance impact
* Suggested fix (optional)

---

## 📞 Contact (Authorized Channels Only)

**TEOS Egypt — Security & Governance Team**
📧 Private bank communication channel
📱 WhatsApp: **+20 100 616 7293**
🔗 LinkedIn: [Ayman Seif](https://www.linkedin.com/in/aymanseif/)

---

## 🔐 License

**Private © Elmahrosa & TEOS Egypt**
Not open source. Not for public distribution.
All rights reserved.
