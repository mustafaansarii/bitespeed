Here’s a **complete `README.md`** for your Bitespeed Identity Reconciliation backend task, ready for GitHub.

You can copy-paste this into your `README.md` file and replace placeholders like your Render URL, GitHub repo name, and screenshot image path.

---


# Bitespeed Backend Task: Identity Reconciliation

![screenshot](/postman%20eg.png)

This project solves the Identity Reconciliation problem for Bitespeed. It consolidates contact records (email and phone numbers) across multiple purchases to maintain a unique customer identity.

---

## 🚀 Live API

👉 [https://your-render-app-url.onrender.com/identify](https://your-render-app-url.onrender.com/identify)

---

## 🔧 Tech Stack

- **Framework:** Django (Python)
- **Database:** SQLite (for local dev) / PostgreSQL (for deployment)
- **Deployment:** Render.com
- **API Format:** REST (JSON Body)

---

## 📦 Setup Instructions

### 🖥️ Local Development

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/bitespeed-identity-reconciliation.git
   cd bitespeed-identity-reconciliation


2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # or `venv\Scripts\activate` on Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the server**

   ```bash
   python manage.py runserver
   ```

6. **Test in Postman**

   * URL: `http://localhost:8000/identify`
   * Method: `POST`
   * Header: `Content-Type: application/json`
   * Body (example):

     ```json
     {
       "email": "mcfly@hillvalley.edu",
       "phoneNumber": "123456"
     }
     ```

---

## 🔍 Sample Request and Response

### Request

```http
POST /identify
Content-Type: application/json

{
  "email": "mcfly@hillvalley.edu",
  "phoneNumber": "123456"
}
```

### Response

```json
{
  "contact": {
    "primaryContatctId": 1,
    "emails": [
      "lorraine@hillvalley.edu",
      "mcfly@hillvalley.edu"
    ],
    "phoneNumbers": [
      "123456"
    ],
    "secondaryContactIds": [23]
  }
}
```

---

## 🔁 Edge Case Handling

* ✅ Only email provided
* ✅ Only phoneNumber provided
* ✅ New contact (no match found)
* ✅ Merge scenario (two primaries collide)
* ✅ Proper ordering of primary's data in response

---
