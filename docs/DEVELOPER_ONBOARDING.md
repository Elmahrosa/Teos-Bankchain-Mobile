# Developer Onboarding — TEOS BankChain Mobile 🚀

⚠️ **Private Repository — Restricted to Partner Banks Only**  
Access is limited to financial institutions operating under direct agreement with TEOS Egypt.  
Redistribution or public disclosure is prohibited.

---

## 📌 Purpose
This guide provides new engineers at partner banks with a step‑by‑step onboarding process:  
- Clone the repo  
- Set up backend (FastAPI)  
- Run mobile client (Expo / React Native)  
- Validate CI/CD checks  
- Confirm compliance modules  

---

## 🛠 Prerequisites
- **GitHub access** (NDA signed, repo invite approved)  
- **Python 3.11+** (backend)  
- **Node.js 18+ & npm/yarn** (mobile client)  
- **Expo CLI** (`npm install -g expo-cli`)  
- **Docker** (optional for containerized backend)  
- **Postman** (for API testing)  
- **GPG keys** (for signed commits)  

---

## 📂 Step 1 — Clone Repo
```bash
git clone git@github.com:Elmahrosa/Teos-Bankchain-Mobile.git
cd Teos-Bankchain-Mobile
```

---

## ⚙️ Step 2 — Backend Setup (FastAPI)
```bash
cd backend
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
uvicorn main:app --reload
```

**Verify:**  
- API docs available at `http://localhost:8000/docs`  
- Health check endpoint: `GET /health` → `200 OK`  

---

## 📱 Step 3 — Mobile Client Setup (Expo / React Native)
```bash
cd mobile
npm install
expo start
```

**Verify:**  
- Scan QR code with Expo Go app (iOS/Android)  
- Login screen loads with OTP + biometric prompt  

---

## 🔒 Step 4 — Compliance Modules
- Run KYC endpoint: `POST /compliance/kyc`  
- Trigger AML check: `POST /compliance/aml-check`  
- Export audit logs: `GET /compliance/export?format=json`  
- Confirm immutable audit trail in logs  

---

## 🧪 Step 5 — CI/CD Validation
Run local checks before PR submission:
```bash
pytest              # backend tests
npm test            # mobile tests
```

CI/CD pipelines enforced:
- ✅ `verify.yml` — docs, links, secrets, builds  
- ✅ `ci.yml` — backend + mobile tests  
- ✅ `codeql.yml` — security scanning  

---

## 🔑 Step 6 — Contribution Rules
- Work only in `feature/*` or `fix/*` branches  
- Submit PRs against `main` (protected)  
- Ensure commits are **signed** (`git commit -S`)  
- Document compliance impact in PR descriptions  

---

## 📦 Optional — Docker Backend
```bash
docker build -t teos-bankchain-backend .
docker run -p 8000:8000 teos-bankchain-backend
```

---

## 📞 Support
**TEOS Egypt Technical Team**  
📧 Private partner channel  
📱 WhatsApp: +20 100 616 7293  
🔗 [LinkedIn: Ayman Seif](https://www.linkedin.com/in/aymanseif/)

---

## 🔁 Change Log
- `2025-11-30` — Initial scaffold for partner bank onboarding
