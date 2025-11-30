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
```

---

## 🌐 Base URL
- **Sandbox:** `https://sandbox.teos-bankchain.com/api/v1`  
- **Production:** `https://api.teos-bankchain.com/v1`

---

## 📂 Endpoints

### 1. **Bank Accounts**
- `GET /accounts` → List all linked bank accounts.  
- `POST /accounts/link` → Link a new bank account via Open Banking API.  
- `DELETE /accounts/{id}` → Unlink a bank account.  

---

### 2. **Fiat ↔ Crypto Conversion**
- `POST /convert` → Convert fiat to crypto or crypto to fiat.  
  - **Body:**
    ```json
    {
      "from_currency": "USD",
      "to_currency": "BTC",
      "amount": 1000
    }
    ```
  - **Response:**
    ```json
    {
      "transaction_id": "abc123",
      "status": "completed",
      "converted_amount": 0.025,
      "rate": 40000
    }
    ```

---

### 3. **Wallet Management**
- `GET /wallets` → List all wallets (custodial + customer).  
- `POST /wallets/create` → Create a new wallet.  
- `POST /wallets/{id}/transfer` → Transfer crypto between wallets.  

---

### 4. **Compliance & Monitoring**
- `GET /compliance/reports` → Generate compliance reports.  
- `POST /compliance/kyc` → Submit KYC data for a customer.  
- `POST /compliance/aml-check` → Run AML check on a transaction.  

---

### 5. **Settlement Layer**
- `POST /settlement/initiate` → Start fiat ↔ crypto settlement.  
- `GET /settlement/status/{id}` → Check settlement status.  

---

## 📊 Response Codes
- `200 OK` → Successful request.  
- `400 Bad Request` → Invalid parameters.  
- `401 Unauthorized` → Authentication failed.  
- `403 Forbidden` → Insufficient permissions.  
- `500 Internal Server Error` → Unexpected error.  

---

## ⚖️ Compliance Notes
- All API calls are logged for audit purposes.  
- KYC/AML checks are mandatory before settlement.  
- Banks must store API logs for regulator review.  

---

## 🚀 Next Steps
1. Request sandbox API keys from TEOS Egypt.  
2. Test integration with `sandbox.teos-bankchain.com`.  
3. Move to production after compliance approval.  
```

---


