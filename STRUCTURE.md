# Repo Structure: TEOS BankChain Mobile 📂

This document explains the folder layout, purpose of each module, and onboarding flow for contributors.

---

## 📂 Root Layout
```
teos-bankchain-mobile/
│
├── android/        # Native Android app (Kotlin/Java)
├── ios/            # Native iOS app (Swift)
├── backend/        # API + Conversion Engine (FastAPI/Spring Boot)
├── blockchain/     # Ethereum, Pi Network, Bitcoin connectors
├── compliance/     # KYC/AML modules + monitoring
├── docs/           # Documentation (STRUCTURE.md, COMPLIANCE.md, API_GUIDE.md)
├── .github/        # CI/CD workflows
├── docker/         # Dockerfiles for backend + blockchain
├── SECURITY.md     # Encryption, wallet safety, audit logs
├── CONTRIBUTING.md # Dev onboarding and standards
├── ROADMAP.md      # Feature rollout plan
└── LICENSE         # Private license
```

---

## 📱 Mobile Apps
- **android/** → Kotlin/Java codebase using Jetpack Compose.  
  - `ui/` → Screens and components.  
  - `wallet/` → Crypto wallet integration.  
  - `build.gradle` → Build configuration.  

- **ios/** → Swift/SwiftUI codebase.  
  - `UI/` → Screens and components.  
  - `Wallet/` → Crypto wallet integration.  
  - `Info.plist` → App configuration.  

---

## ⚙️ Backend
- **backend/** → FastAPI (Python) or Spring Boot (Java).  
  - `src/` → API endpoints for fiat ↔ crypto conversion.  
  - `tests/` → Unit and integration tests.  
  - `requirements.txt` → Dependencies.  

---

## 🌐 Blockchain Gateway
- **blockchain/** → Connectors for Ethereum, Pi Network, Bitcoin.  
  - `ethereum/` → Web3.js / ethers.js integration.  
  - `pi-network/` → Pi SDK integration.  
  - `bitcoin/` → Bitcoin RPC integration.  
  - `README.md` → Notes on blockchain setup.  

---

## 🛡️ Compliance
- **compliance/** → KYC/AML modules and monitoring scripts.  
  - `modules/` → Verification logic.  
  - `reports/` → Regulatory reporting templates.  
  - `README.md` → Compliance overview.  

---

## 📑 Documentation
- **docs/** → Living documentation for contributors and banks.  
  - `STRUCTURE.md` → Repo layout (this file).  
  - `COMPLIANCE.md` → Regulatory notes.  
  - `API_GUIDE.md` → How banks integrate via APIs.  

---

## 🔄 CI/CD
- **.github/workflows/** → GitHub Actions pipelines.  
  - Automated builds for Android/iOS.  
  - Docker builds for backend + blockchain.  
  - Security scans and compliance checks.  

---

## 🐳 Deployment
- **docker/** → Dockerfiles for backend and blockchain services.  
  - `backend.Dockerfile` → API container.  
  - `blockchain.Dockerfile` → Blockchain gateway container.  

---

## 🚀 Contributor Flow
1. Clone repo → `git clone ...`  
2. Install dependencies (Android Studio, Xcode, Python/Java).  
3. Run backend locally → `uvicorn main:app --reload` or `mvn spring-boot:run`.  
4. Launch mobile apps in emulator (Android/iOS).  
5. Connect blockchain gateways via testnet.  
6. Submit PRs → reviewed before merging into `main`.  

---

## ⚖️ Notes
- Repo is **private** and proprietary.  
- All contributions must follow **SECURITY.md** and **CONTRIBUTING.md**.  
- Compliance modules are mandatory for production builds.  
