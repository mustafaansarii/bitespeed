

# Bitespeed Backend Task: Identity Reconciliation

This project solves the Identity Reconciliation problem for Bitespeed. It consolidates contact records (email and phone numbers) across multiple purchases to maintain a unique customer identity.

---

## Live API

👉 [https://bitespeed-identity-fz0m.onrender.com/identify](https://bitespeed-identity-fz0m.onrender.com/identify)

---

## 🔧 Tech Stack

- **Framework:** Django (Python)
- **Database:** SQLite (for local dev) / PostgreSQL (for deployment)
- **Deployment:** Render.com
- **API Format:** REST (JSON Body)

---

## Setup Instructions

### Local Development

1. **Clone the repo**
   ```bash
   git clone https://github.com/mustafaansarii/bitespeed.git
   cd bitespeed


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

## Sample Request and Response

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
![screenshot](/postman%20eg.png)
## Edge Case Handling

* ✅ Only email provided
* ✅ Only phoneNumber provided
* ✅ New contact (no match found)
* ✅ Merge scenario (two primaries collide)
* ✅ Proper ordering of primary's data in response

---
