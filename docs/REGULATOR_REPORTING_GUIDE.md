# Regulator Reporting Guide — TEOS BankChain Mobile 🏛️📊

⚠️ **Private Document — Restricted to Partner Banks Only**  
Access is limited to financial institutions operating under direct agreement with TEOS Egypt.  
Redistribution or public disclosure is prohibited.

---

## 📌 Purpose
This guide explains how TEOS BankChain Mobile enables partner banks to deliver **regulator‑ready exports**.  
It covers reporting formats, delivery channels, and compliance mappings for **CBE (Central Bank of Egypt)**, **SAMA (Saudi Arabia)**, **FCA (UK)**, and **FATF (international)**.

---

## 🧭 Scope
- Transaction and settlement reporting  
- KYC/AML compliance exports  
- Suspicious Activity Reports (SARs)  
- Immutable audit trails  
- Data retention and regulator ingestion formats  

---

## 🏦 Central Bank of Egypt (CBE)

### Required Fields
- `audit_id`  
- `timestamp_utc`  
- `initiator.id`  
- `operation`  
- `amount`  
- `currency`  
- `counterparty_id`  
- `transaction_id`  
- `kyc_checked`  
- `aml_score`  

### Preferred Format
- **CSV or encrypted JSON (AES‑256)**  
- Must include **bank signature header** for authenticity  

### Delivery Channels
- Secure **SFTP drop** to CBE compliance servers  
- HTTPS upload via regulator portal (TLS 1.3 enforced)  
- Signed manifest required: `{file_hash, record_count, generated_by, signature}`  

### Example CSV Header
```
audit_id,timestamp_utc,operation,transaction_id,initiator_id,amount,currency,counterparty_id,kyc_checked,aml_score,sanctions_screened,retention_class
```

---

## 🇸🇦 Saudi Arabian Monetary Authority (SAMA)
- **Required:** full transaction trace, sanctions screening, AML score, beneficial owner (>25%)  
- **Format:** JSON (UTF‑8) or XML (ISO 20022 settlement mapping)  
- **Delivery:** Secure HTTPS or regulator portal  

---

## 🇬🇧 Financial Conduct Authority (FCA)
- **Required:** SARs when `requires_sar == true`, hashed KYC proofs, IP + geolocation logs  
- **Format:** CSV/JSON via secure portal or SFTP  
- **Delivery:** FCA secure upload portal  

---

## 🌍 FATF / International
- **Required:** aggregated AML statistics, SAR counts, typologies, cross‑border flows  
- **Format:** Aggregate JSON or Excel  
- **Delivery:** Secure FATF channels (encrypted email/SFTP)  

---

## 🔒 Compliance Workflow
1. **Generate audit logs** → Immutable, hashed records  
2. **Run AML scoring** → Flag suspicious activity  
3. **Create SARs** → `POST /compliance/sar`  
4. **Export regulator data** → `GET /compliance/export?format=json|csv|xml`  
5. **Deliver securely** → SFTP/HTTPS/portal upload with signed manifest  

---

## 📑 Partner Bank Checklist
- [ ] Acquire sandbox API keys  
- [ ] Validate regulator export formats (CBE, SAMA, FCA, FATF)  
- [ ] Confirm signed manifest generation  
- [ ] Test secure delivery channels (SFTP/HTTPS)  
- [ ] Run compliance dry‑run with regulator observers  

---

## 📞 Escalation & Contact
**TEOS Egypt — Compliance & Reporting Team**  
📧 compliance@teos-egypt.internal *(private partner channel only)*  
📱 WhatsApp: +20 100 616 7293  
🔗 [LinkedIn: Ayman Seif](https://www.linkedin.com/in/aymanseif/)

---

## 🔁 Change Log
- `2025-11-30` — Initial scaffold with CBE, SAMA, FCA, FATF reporting
```
