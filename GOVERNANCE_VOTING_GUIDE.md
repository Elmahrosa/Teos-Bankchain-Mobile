# Governance Voting Guide — TEOS BankChain Mobile 🗳️🏛️

⚠️ **Private Document — Restricted to Partner Banks Only**  
Access is limited to financial institutions operating under direct agreement with TEOS Egypt.  
Redistribution or public disclosure is prohibited.

---

## 📌 Purpose
This guide explains how partner banks participate in **TEOS governance voting** using NFT‑based tokens.  
It covers **vote casting, tallying, enforcement, and compliance alignment** for institutional decision‑making.

---

## 🧭 Governance Principles
1. **Transparency** — All votes logged in immutable audit trails.  
2. **Fairness** — Voting power proportional to staked governance tokens.  
3. **Compliance** — KYC/AML enforced for all voting participants.  
4. **Finality** — Decisions executed automatically via smart contracts.  

---

## 🖼 NFT Voting Tokens
- Each bank mints **NFT governance tokens** representing its stake.  
- Metadata includes:  
  - `bank_id`  
  - `stake_amount`  
  - `vote_weight`  
  - `issued_at`  
- NFTs are non‑transferable outside partner bank marketplace.  

---

## 🗳️ Casting Votes
- **Endpoint:** `POST /governance/vote`  
- **Request Example:**
```json
{
  "proposal_id": "PROP-20251201-001",
  "bank_id": "BANK123",
  "nft_id": "NFT98765",
  "vote": "yes"
}
```

- **Response Example:**
```json
{
  "vote_id": "VOTE-20251201-0001",
  "status": "recorded",
  "timestamp": "2025-12-01T10:00:00Z"
}
```

---

## 📊 Tallying Votes
- Votes weighted by **stake amount** linked to NFT.  
- Formula:
```
total_yes_weight = Σ(bank_vote_weight where vote == yes)
total_no_weight  = Σ(bank_vote_weight where vote == no)
```
- Decision threshold: **≥ 51% of total stake weight**.  
- Results published via `/governance/results`.  

---

## ⚙️ Enforcement
- Once threshold met:  
  - Smart contract executes protocol upgrade or fee adjustment.  
  - Immutable audit record created (`audit_id`).  
  - Regulator reporting triggered if compliance impact detected.  

---

## 🔒 Compliance Integration
- All votes logged with KYC‑verified bank IDs.  
- AML checks enforced on treasury contributions linked to voting NFTs.  
- Regulator exports available for governance decisions.  
- Retention: 7 years (regulator), 10 years (sensitive governance artefacts).  

---

## 📑 Partner Bank Checklist
- [ ] Mint NFT governance tokens.  
- [ ] Verify vote weight matches staked amount.  
- [ ] Cast votes via `/governance/vote`.  
- [ ] Validate results via `/governance/results`.  
- [ ] Confirm compliance export for regulator review.  

---

## 📞 Contact
**TEOS Egypt — Governance & Voting Team**  
📧 governance@teosegypt.com *(private partner channel only)*  
📱 WhatsApp: +20 100 616 7293  
🔗 [LinkedIn: Ayman Seif](https://www.linkedin.com/in/aymanseif/)

---

## 🔁 Change Log
- `2025-12-01` — Initial scaffold for NFT governance voting
```
