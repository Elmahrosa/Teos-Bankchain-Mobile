# API_GUIDE.md 🔌
**Integration Guide for TEOS BankChain Mobile APIs**

---

## 📖 Purpose
This guide explains how banks and financial institutions can integrate with the TEOS BankChain Mobile backend APIs.  
It covers authentication, endpoints, request/response formats, and compliance requirements.

---

## 🔑 Authentication
- **OAuth 2.0** → Secure token-based authentication.  
- **API Keys** → Issued per bank client.  
- **Multi-Factor Authentication (MFA)** → Required for admin endpoints.  

Example:
```http
Authorization: Bearer <access_token>
