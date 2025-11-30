# Repository Structure — TEOS BankChain Mobile

⚠️ **Private Repository — Restricted to Partner Banks Only**  
Access is limited to financial institutions operating under direct agreement with TEOS Egypt.  
Redistribution or public disclosure is prohibited.

---

## 📂 Root Layout

```
Teos-Bankchain-Mobile/
├── backend/                # FastAPI backend (custodial wallets, conversion, compliance APIs)
│   ├── main.py              # Entry point (Uvicorn app)
│   ├── routers/             # Modular API routers (accounts, convert, compliance)
│   ├── models/              # Pydantic models & DB schemas
│   ├── services/            # Business logic (liquidity, settlement, monitoring)
│   ├── tests/               # Pytest unit/integration tests
│   └── requirements.txt     # Python dependencies
│
├── mobile/                 # Expo / React Native mobile client
│   ├── App.tsx              # Main app entry
│   ├── screens/             # UI screens (Login, Dashboard, Transfers)
│   ├── components/          # Reusable UI components
│   ├── services/            # API calls, auth flows
│   ├── assets/              # Images, icons, fonts
│   └── package.json         # Node dependencies
│
├── docs/                   # Documentation & compliance resources
│   ├── ONBOARDING-PLAYBOOK.md
│   ├── compliance/          # Templates for regulator reporting
│   ├── API_GUIDE.md         # Backend API usage
│   ├── SECURITY.md          # Vulnerability reporting & enforcement
│   ├── CONTRIBUTING.md      # Contribution workflow
│   ├── CODE_OF_CONDUCT.md   # Behavior standards
│   └── ROADMAP.md           # Strategic milestones
│
├── .github/                # GitHub workflows & automation
│   ├── workflows/
│   │   ├── ci.yml           # CI pipeline (lint, test, build)
│   │   ├── verify.yml       # Docs, links, secrets, builds
│   │   ├── codeql.yml       # CodeQL security scanning
│   │   └── dependabot.yml   # Dependency updates
│
├── STRUCTURE.md            # Repo layout (this file)
├── README.md               # Overview, badges, Quickstart
├── LICENSE                 # Proprietary license & NDA
├── CHANGELOG.md            # Release history
└── SECURITY.md             # Security policy
```

---

## 🔑 Design Principles
- **Separation of duties:** Backend, mobile, docs, and workflows isolated.  
- **Compliance‑first:** Dedicated `docs/compliance/` folder for regulator templates.  
- **Audit‑ready:** CI/CD workflows enforce linting, testing, and security scans.  
- **Scalability:** Modular routers and components for rapid iteration.  

---

## 📌 Contributor Notes
- Work only in `feature/*` or `fix/*` branches.  
- Submit PRs against `main` (protected).  
- Ensure CI/CD checks pass before requesting review.  
- Document compliance impact in PR descriptions.  

---

## 📞 Contact
For repo structure or onboarding questions:  
**TEOS Egypt Governance Team**  
📧 [Private bank channel only]  
📱 WhatsApp: +20 100 616 7293  
🔗 [LinkedIn: Ayman Seif](https://www.linkedin.com/in/aymanseif/)
```

