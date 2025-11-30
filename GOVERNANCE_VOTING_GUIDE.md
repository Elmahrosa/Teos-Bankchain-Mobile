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
