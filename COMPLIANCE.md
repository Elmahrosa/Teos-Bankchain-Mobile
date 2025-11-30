# COMPLIANCE — TEOS BankChain Mobile 🛡️

> This document explains how TEOS BankChain Mobile satisfies regulator reporting, audit logging, KYC/AML, and data retention requirements for partner banks.  
> Target regulators covered: **CBE (Central Bank of Egypt), SAMA (Saudi Arabia), FCA (UK), FATF (international)**.

---

## 📖 Purpose
Provide a clear, auditable mapping from application events to regulator reporting artefacts and formats.  
Enable partner banks to rapidly comply with local regulator demands and automated audits.

---

## 🧭 Scope
- Transaction and settlement reporting  
- KYC / Customer onboarding artefacts  
- AML alerts and suspicious activity reporting (SAR)  
- Immutable audit trails and change history  
- Data export formats for regulator ingestion (JSON / CSV / encrypted XML)

---

## 🔐 Audit Log — Canonical Schema
All API calls produce an immutable audit record. Records are append‑only and cryptographically hashed (SHA‑256).

**Audit record (canonical JSON):**
```json
{
  "audit_id": "AUD-20251130-0001",
  "timestamp_utc": "2025-11-30T21:40:00Z",
  "service": "transactions",
  "operation": "create",
  "initiator": {
    "type": "user|system|bank",
    "id": "CUST12345",
    "wallet_id": "WALLET_ABC"
  },
  "request": {
    "path": "/transactions",
    "method": "POST",
    "body_hash": "sha256:abcd...",
    "ip": "41.32.10.5",
    "user_agent": "TeosMobile/1.2.3 (Android)"
  },
  "response": {
    "status_code": 202,
    "response_hash": "sha256:ef01..."
  },
  "compliance_flags": {
    "kyc_checked": true,
    "aml_score": 78,
    "sanctions_screened": true,
    "requires_sar": false
  },
  "retention_class": "regulatory_7y",
  "signature": "ed25519:base58sig..."
}
```

---

## 🧾 Regulator Field Mapping

### CBE (Central Bank of Egypt)
- **Required:** `audit_id`, `timestamp_utc`, `initiator.id`, `operation`, `amount`, `currency`, `counterparty_id`, `transaction_id`, `kyc_checked`, `aml_score`  
- **Format:** CSV or encrypted JSON (AES‑256) with bank signature header

### SAMA (Saudi Arabian Monetary Authority)
- **Required:** full transaction trace, `sanctions_screened`, `aml_score`, `customer_risk_rating`, `customer_address`, `beneficial_owner` (>25%)  
- **Format:** JSON (UTF‑8) or XML (ISO 20022 settlement mapping)

### FCA (United Kingdom)
- **Required:** SARs when `requires_sar == true`, KYC proof (hashed IDs), timestamps, audit trail with IP + geolocation  
- **Format:** Secure portal upload (CSV/JSON) or SFTP drop with manifest

### FATF / International
- **Required:** Aggregated AML statistics, SAR counts, typologies, cross‑border flows, suspicious patterns  
- **Format:** Aggregate JSON or Excel; SARs via secure channels

---

## 🔎 KYC / AML Workflow

1. **Onboarding (`POST /compliance/kyc`)**  
   - Capture name, DOB, IDs, address, PoA  
   - Store docs encrypted (AES‑256); metadata in DB  
   - Output: `kyc_id`, `kyc_status` (`pending|verified|rejected`)

2. **Sanctions & PEP Screening**  
   - Automated at onboarding + periodic intervals (30/90/365 days)  
   - Flags: `sanctions_screened`, `pep_hit`

3. **Transaction Monitoring**  
   - Real‑time scoring (`aml_score` 0–100)  
   - Thresholds:  
     - `>=90` → auto‑block + escalate  
     - `70–89` → manual review queue  
   - SAR endpoint: `POST /compliance/sar`

4. **SAR Payload Example**
```json
{
  "sar_id": "SAR-20251130-0001",
  "reported_at": "2025-11-30T21:45:00Z",
  "subject": {
    "customer_id": "CUST12345",
    "name_hash": "sha256:..."
  },
  "transactions": [
    {
      "transaction_id": "TX123456",
      "timestamp": "2025-11-30T21:36:00Z",
      "amount": 10000,
      "currency": "USD"
    }
  ],
  "reason": "Structuring to avoid thresholds",
  "analyst_notes": "Pattern of rapid deposits followed by off-chain withdrawal",
  "attachments": ["s3://secure-bucket/sar/SAR-20251130-0001/pack.enc"]
}
```

---

## 🗂️ Data Retention & Access Control
- **Retention classes:**  
  - `operational_1y` — ops logs (1 year)  
  - `regulatory_7y` — regulator storage (7 years)  
  - `sensitive_10y` — AML SAR artefacts (10 years)  
- **Encryption:** AES‑256 at rest, DB field encryption for PII  
- **Key management:** AWS KMS / HSM  
- **Access control:** RBAC + MFA; privileged ops require break‑glass justification

---

## 🔁 Export Endpoints

- `GET /compliance/export/audit?from=2025-11-01&to=2025-11-30&format=json|csv|xml`  
- `POST /compliance/export/push`  
```json
{
  "regulator": "CBE|SAMA|FCA",
  "format": "json|csv|xml",
  "delivery": "sftp|https|portal",
  "manifest": {
    "records": 1523,
    "file_hash": "sha256:..."
  }
}
```

**CSV Export Header (CBE):**
```
audit_id,timestamp_utc,operation,transaction_id,initiator_id,amount,currency,counterparty_id,kyc_checked,aml_score,sanctions_screened,retention_class
```

---

## 🧪 Compliance Testing
- **Sandbox endpoints:**  
  - `POST /sandbox/compliance/seed` → seed fake KYC & transactions  
  - `GET /sandbox/compliance/report/selftest` → self‑audit verification  
- **Audit snapshots:** immutable tarball with manifest + hash chain

---

## 🔗 Partner Bank Checklist
- [ ] Acquire sandbox API keys  
- [ ] Verify KYC ingestion (`POST /compliance/kyc`)  
- [ ] Run sanctions/PEP scans  
- [ ] Validate transaction monitoring thresholds + SAR generation  
- [ ] Export regulator format + validate manifest signatures  
- [ ] Confirm retention classification + access control  

---

## 📞 Escalation & Contact
**TEOS Egypt — Compliance & Security**  
📧 compliance@teos-egypt.internal *(private partner channel only)*  
📱 WhatsApp: +20 100 616 7293  
🔗 [LinkedIn: Ayman Seif](https://www.linkedin.com/in/aymanseif/)

---

## ⚠️ Legal Notes
- This document is **guidance** — partner banks must confirm formats with local counsel/regulators.  
- TEOS provides technical exports + secure delivery; acceptance requires regulator agreement.

---

## 🧾 Change Log
- `2025-11-30` — Initial scaffold (CBE, SAMA, FCA, FATF)  
- Future: add ISO 20022 XML schemas, sample SFTP manifests, SAR transmission API bindings
```
