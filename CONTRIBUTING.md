# Contributing Guidelines

⚠️ **Private Repository — Restricted to Partner Banks Only**  
Access is limited to financial institutions operating under direct agreement with TEOS Egypt.  
Public contributions are not accepted. Redistribution or disclosure is prohibited.

---

## Contribution Workflow

1. **Authorization**
   - Only approved bank developers with signed agreements may contribute.
   - Ensure your access is provisioned through TEOS Egypt.

2. **Branching**
   - Work must be done in feature branches (`feature/<bank>-<module>`).
   - Never commit directly to `main`.

3. **Commits**
   - Use clear, audit‑friendly commit messages:
     ```
     [bank-id] module: short description
     ```
   - Do not include sensitive data, credentials, or regulator information.

4. **Pull Requests**
   - Submit PRs against `develop` branch.
   - PRs must include:
     - Linked issue or task ID
     - Compliance notes (if applicable)
     - Test coverage confirmation

5. **CI/CD**
   - All PRs trigger GitHub Actions workflows:
     - Linting
     - Unit tests (`pytest` for backend, `npm test` for mobile)
     - Security scans
   - PRs failing CI/CD checks will not be merged.

---

## Security & Compliance

- Follow **least privilege** principles when accessing repo modules.
- Ensure **audit logs** are preserved for all development activity.
- Never commit secrets, credentials, or sensitive data.
- All code must pass compliance review before deployment.

---

## Code Style

- **Backend (FastAPI / Python):**
  - PEP8 style guide
  - Type hints required
  - Tests in `backend/tests/`

- **Mobile (Expo / React Native):**
  - ESLint + Prettier enforced
  - Functional components preferred
  - Tests in `mobile/__tests__/`

---

## Reporting Issues

- **Do not open public issues.**
- Report bugs or vulnerabilities privately via TEOS Egypt’s secure channel.
- Include reproduction steps, impact assessment, and suggested mitigation.

---

## License

Private © Elmahrosa & TEOS Egypt  
**Not for public use. Not open source.**
