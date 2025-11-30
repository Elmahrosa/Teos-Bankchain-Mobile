# **API Guide — TEOS BankChain Mobile**

⚠️ **Private Repository — Restricted to Partner Banks Only**
Access only for financial institutions under agreement with **TEOS Egypt**.
Redistribution or public disclosure is strictly prohibited.

---

## 📌 **Overview**

This guide documents the **FastAPI backend endpoints** and **mobile client flows** for TEOS BankChain Mobile.
All requests must be authenticated and comply with TEOS Egypt’s compliance framework (KYC/AML, audit trail, regulator reporting).

---

## 🔑 **Authentication**

### **Endpoint**

`POST /auth/login`

### **Request**

```json
{
  "username": "bankuser1",
  "password": "securePassword123",
  "otp": "123456"
}
```

---

## 🔒 **Security Model**

* **OAuth 2.0** — secure token-based authentication
* **API Keys** — issued per bank
* **MFA required** — for all admin endpoints

### **Header Example**

```http
Authorization: Bearer <access_token>
```

---

## 🌐 **Base URLs**

| Environment    | URL                                         |
| -------------- | ------------------------------------------- |
| **Sandbox**    | `https://sandbox.teos-bankchain.com/api/v1` |
| **Production** | `https://api.teos-bankchain.com/v1`         |

---

# 📂 **API Endpoints**

---

## **1. Bank Accounts**

### `GET /accounts`

List customer’s linked bank accounts.

### `POST /accounts/link`

Link a new bank account via Open Banking API.
**Body Example:**

```json
{
  "account_number": "123456789",
  "bank_code": "CIBEG",
  "owner_name": "Ayman Seif"
}
```

### `DELETE /accounts/{id}`

Remove a linked bank account.

---

## **2. Fiat ↔ Crypto Conversion**

### `POST /convert`

Convert between fiat and crypto.

**Request Example:**

```json
{
  "from_currency": "USD",
  "to_currency": "BTC",
  "amount": 1000
}
```

**Response Example:**

```json
{
  "transaction_id": "abc123",
  "status": "completed",
  "converted_amount": 0.025,
  "rate": 40000
}
```

---

## **3. Wallet Management**

### `GET /wallets`

List all wallets (custodial + customer).

### `POST /wallets/create`

Create a new wallet.

### `POST /wallets/{id}/transfer`

Transfer between wallets.
**Body:**

```json
{
  "to_wallet_id": "wallet_002",
  "amount": 25,
  "asset": "USDT"
}
```

---

## **4. Compliance & Monitoring**

### `GET /compliance/reports`

Generate compliance reports.

### `POST /compliance/kyc`

Submit KYC data.

### `POST /compliance/aml-check`

Run AML screening on a transaction.

---

## **5. Settlement Layer**

### `POST /settlement/initiate`

Start a settlement request.

### `GET /settlement/status/{id}`

Check settlement status by transaction ID.

---

# 📊 **Response Codes**

| Code                          | Meaning                  |
| ----------------------------- | ------------------------ |
| **200 OK**                    | Successful               |
| **400 Bad Request**           | Invalid input            |
| **401 Unauthorized**          | Missing/invalid auth     |
| **403 Forbidden**             | Insufficient permissions |
| **500 Internal Server Error** | Unexpected failure       |

---

# ⚖️ **Compliance Requirements**

* All API calls generate **immutable audit logs**
* **KYC/AML checks mandatory** before transfers or settlements
* Partner banks must retain logs per regulator rules

---

# 🚀 **Next Steps for Integration**

1. Request **sandbox API keys** from TEOS Egypt.
2. Test calls against:
   `https://sandbox.teos-bankchain.com/api/v1`
3. After compliance approval → switch to production.

---
