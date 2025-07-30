# 🎉 Holiday API

Ever wanted to know what weird, fun, or downright bizarre holidays are celebrated today? Look no further! The ** Holiday API** gives you quick access to oddball celebrations based on date. 🗓️✨

---

## 🚀 Features

- 🔍 `GET /holiday?date=DD-MM` — Fetch  holidays for any date
- 📅 `GET /today` — Instantly get today's quirky holidays
- 🌐 JSON responses, easy to integrate in apps or projects
- 💡 Ideal for content creators, indie hackers, bots, and newsletters

---

## 🛠️ How to Use

### 🔗 Base URL (local)
```
http://localhost:8000
```

### 📬 Endpoints

#### `GET /holiday?date=DD-MM`
Returns holidays for a specific date.

**Example:**
```
/holiday?date=30-07
```

**Response:**
```json
{
  "date": "30-07",
  "holidays": ["International Friendship Day", "National Cheesecake Day"]
}
```

---

#### `GET /today`
Returns holidays for the current system date.

**Response (example):**
```json
{
  "date": "25-12",
  "holidays": ["Christmas", "Pumpkin Pie Day"]
}
```

---

## 📦 Running the API Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/SnipeAB/-holiday-api.git
   cd -holiday-api
   ```

2. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

3. Run the API:
   ```bash
   python -m uvicorn holidayAPI:app --reload
   ```

4. Visit Swagger UI:
   ```
   http://127.0.0.1:8000/docs
   ```

---

## 🧠 Powered By

- [FastAPI](https://fastapi.tiangolo.com/) 🚀
- JSON-powered holiday data 📂

---

## 📅 Sample Data

Holiday data is stored in [`data/holidays.json`](./data/holidays.json). You can easily extend it by adding new entries in `DD-MM` format.

---

## ❤️ Contribute

Want to add holidays? Found a bug? PRs welcome!

---

## 📃 License

MIT — use this freely, even commercially!

---

> Built with caffeine ☕, emojis 😎, and love 💖
