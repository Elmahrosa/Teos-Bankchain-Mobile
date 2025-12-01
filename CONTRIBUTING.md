# 🏦 Contributing Guidelines — TEOS BankChain Mobile

⚠️ **Private Repository — Restricted to Partner Banks Only**  
Access is limited to financial institutions operating under direct agreement with **TEOS Egypt**.  
Redistribution, copying, or public disclosure is strictly prohibited.

---

## 📌 1. Authorization & Access
- Only approved bank developers with signed **NDA + Partner Access Agreement** may contribute.  
- Access must be provisioned through **TEOS Egypt Security & Governance Team**.  
- All contributors must use:
  - Bank‑approved devices  
  - Secure VPN  
  - Hardened environments  
- Unauthorized or public contributions are not allowed.  

---

## 🌿 2. Branching Rules
**Allowed branch types:**
- `feature/<module-name>`  
- `fix/<issue-id>`  
- `hotfix/<critical-issue>`  

**Requirements:**
- All work MUST occur in a dedicated branch.  
- Direct commits to `main` are strictly prohibited.  
- Every branch must reference:
  - Issue number (if applicable)  
  - Module touched  
  - Compliance or security note (if relevant)  

---

## 🔄 3. Pull Requests (PR Workflow)
**PR targets:**  
- `develop`  
- Integration branches (`integration/mobile`, `integration/backend`)  
- ❌ PRs cannot target `main` directly.  

**Every PR must include:**  
- Clear change summary  
- Compliance notes (KYC/AML/SAR impact if any)  
- Test coverage statement  
- Linked issue or scope reference  
- GPG‑signed commits  
- No screenshots of internal data  

**Review requirements:**  
- Minimum 2 reviewer approvals  
- All CI/CD pipelines must pass  
- Linear history (rebase only, no merge commits)  

---

## 🚦 4. Required CI/CD Status Checks
All must be green before merging:

| Check                 | Purpose                                             |
| --------------------- | --------------------------------------------------- |
| **verify.yml**        | Documentation, formatting, secret validation        |
| **ci.yml**            | Backend + mobile tests                              |
| **codeql.yml**        | Security scanning (bank‑grade CodeQL)               |
| **dependency-review** | Vulnerable dependencies check                       |
| **signed commits**    | Mandatory for audit & regulator compliance          |

---

## 🔐 5. Branch Protection Rules
**`main` branch protection:**
- No direct pushes  
- No force pushes  
- Require PR reviews (2+)  
- Require status checks: `verify`, `ci`, `codeql`, dependency review  
- Require signed commits  
- Require successful code scanning  
- Only compliance‑approved maintainers can bypass restrictions  
- All merges logged in immutable audit logs  

---

## 🛡️ 6. Security & Compliance Standards
- ❌ Never commit secrets, API keys, wallet seeds, or credentials  
- ❌ Never expose bank customer data or compliance reports  
- ✔️ Follow secure coding (validation, sanitization, rate limits)  
- ✔️ KYC/AML logic must remain intact unless approved  
- ✔️ Use vault‑stored environment variables  
- ✔️ Review dependencies for license + vulnerability issues  
- ✔️ Follow TEOS Egypt Security Framework & sanctions lists  

---

## 🧪 7. Testing Requirements
**Backend (FastAPI / Python):**
- Unit tests required for wallet, compliance, transaction flows  
- Integration tests required for KYC, AML, SAR reporting, authentication  
- Directory: `backend/tests/`  

**Mobile (Expo / React Native):**
- Unit tests for UI logic + secure state flows  
- Integration tests for wallet screens, API interactions, biometric auth  
- Directory: `mobile/__tests__/`  

**Coverage minimums:**  
- Backend → 80%  
- Mobile → 80%  

---

## 🧑‍💻 8. Code Style Guidelines
**Backend — Python (FastAPI):**
- Follow PEP8  
- Mandatory type hints  
- Use `black` for formatting  
- Use `pydantic` models for schemas  
- No wildcard imports  

**Mobile — React Native / Expo:**
- ESLint + Prettier required  
- Functional components only  
- Use TypeScript throughout  
- Avoid inline styles (Tailwind or StyleSheet)  

---

## 🐞 9. Issue Reporting
⚠️ Never open public GitHub issues.  
All reports must go through **TEOS private secure channels**.  

Include:  
- Steps to reproduce  
- Expected vs actual results  
- Compliance/security impact  
- Optional fix proposal  

AML/KYC issues → auto‑escalation mandatory.  

---

## 🧭 10. Developer Workflow (Quick Summary)
1. Create branch  
2. Code changes  
3. Add tests  
4. Run local checks (`pytest`, `npm test`)  
5. Run security checks (`bandit -r backend/`, `npm audit`)  
6. Commit with GPG signature  
7. Push branch  
8. Open PR  
9. Pass all CI checks  
10. Review + merge into `develop`  

---

## 🏷️ 11. Commit Standards
**Commit format:**
```
type(scope): message
```

**Types:**
- `feat:` New feature  
- `fix:` Bug fix  
- `sec:` Security fix  
- `docs:` Documentation  
- `test:` Tests  
- `chore:` Maintenance  

**Example:**
```
feat(wallet): add AML screening on wallet creation
```

All commits must be signed & verified.  

---

## 📦 12. Dependencies
- Must use vetted, regulator‑compliant libraries  
- All dependencies must be pinned  
- Dependabot alerts addressed within 48 hours  
- High‑risk vulnerabilities block merge until patched  

---

## 🚀 13. Releases
- Semantic versioning: `vX.Y.Z`  
- Update `CHANGELOG.md`  
- Tag release + generate GitHub Release  
- Include summary, risk assessment, compliance notes  

---

## 🔐 License
**Proprietary © Elmahrosa International & TEOS Egypt**  
Not open source. Redistribution prohibited.  
Unauthorized access will result in immediate legal action.  

---

## 📞 Contact — Authorized Channels Only
**TEOS Egypt — Security & Governance Division**  
📧 Private bank communication channel  
📱 WhatsApp: +20 100 616 7293  
🔗 LinkedIn: [Ayman Seif](https://www.linkedin.com/in/aymanseif/)  

---

**Version:** 1.7  
**Status:** Active  
**Last Updated:** Dec 1, 2025  

---
