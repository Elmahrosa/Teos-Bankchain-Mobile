# Client Onboarding Playbook — TEOS BankChain Mobile 🧭👥

⚠️ **Private Document — Restricted to Partner Banks Only**  
Access is limited to financial institutions operating under direct agreement with TEOS Egypt.  
Redistribution or public disclosure is prohibited.

---

## 📌 Purpose
This playbook defines the **structured onboarding process** for retail and institutional clients using TEOS BankChain Mobile.  
It ensures onboarding is **secure, compliance‑aligned, and client‑friendly**.

---

## 🧭 Onboarding Phases

### Phase 1 — Pre‑Onboarding
- **Client Identification:** Collect basic client information.  
- **NDA & Disclosure:** Share CLIENT_DISCLOSURE_MANUAL.md with obligations and risks.  
- **Jurisdiction Check:** Confirm eligibility under regulator agreements (CBE, SAMA, FCA, FATF).  

---

### Phase 2 — KYC Verification
- **Document Collection:** Passport, national ID, proof of address.  
- **Verification Workflow:**  
  - Upload documents via secure mobile app.  
  - Automated KYC checks (`POST /compliance/kyc`).  
  - Manual review by compliance officers.  
- **Outcome:** Verified, Pending, or Rejected.  

---

### Phase 3 — AML Screening
- **Transaction Risk Scoring:** Real‑time AML checks (`POST /compliance/aml-check`).  
- **Sanctions/PEP Screening:** Automated flagging of high‑risk clients.  
- **Suspicious Activity Reports (SARs):** Generated if risk threshold exceeded.  

---

### Phase 4 — Account Activation
- **Retail Clients:**  
  - Mobile app access enabled.  
  - Treasury contribution fee disclosed (default 0.25%).  
  - Transaction limits applied based on KYC tier.  

- **Institutional Clients:**  
  - Governance NFT minting enabled.  
  - Treasury staking pool access granted.  
  - Governance voting rights activated.  

---

### Phase 5 — Client Education
- Provide **CLIENT_DISCLOSURE_MANUAL.md** (services, risks, obligations).  
- Share **training materials** for mobile app usage.  
- Conduct webinars for institutional clients on treasury, staking, and governance.  

---

### Phase 6 — Ongoing Monitoring
- Continuous AML scoring and compliance alerts.  
- Quarterly treasury contribution and staking reward reports.  
- Governance voting participation tracking.  
- Regulator reporting exports aligned with jurisdiction.  

---

## 📑 Onboarding Checklist
- [ ] Collect client identification documents.  
- [ ] Share disclosure manual and obtain acknowledgment.  
- [ ] Run KYC verification workflow.  
- [ ] Perform AML screening and sanctions checks.  
- [ ] Activate account (retail or institutional).  
- [ ] Provide client education materials.  
- [ ] Enable ongoing monitoring and compliance alerts.  

---

## 🔒 Compliance Alignment
- **CBE (Egypt):** AML scoring, transaction reporting, treasury audit.  
- **SAMA (Saudi Arabia):** sanctions/PEP screening, beneficial owner reporting.  
- **FCA (UK):** SAR portal uploads, governance transparency.  
- **FATF (International):** AML typologies, suspicious activity aggregation.  

---

## 📞 Contact
**TEOS Egypt — Client Onboarding Team**  
📧 onboarding@teos-egypt.internal *(private partner channel only)*  
📱 WhatsApp: +20 100 616 7293  
🔗 [LinkedIn: Ayman Seif](https://www.linkedin.com/in/aymanseif/)

---

## 🔁 Change Log
- `2025-12-01` — Initial scaffold for client onboarding playbook
