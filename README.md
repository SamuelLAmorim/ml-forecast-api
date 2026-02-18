# 💰 ML Forecast API

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)

API for financial management with monthly expense forecasting using Machine Learning.

Built with **FastAPI**, **SQLAlchemy**, and **Scikit-Learn**.

---

## 🚀 Features

- User authentication with session middleware
- Expense registration (date, category, value, payment type)
- Financial dashboard with charts (Chart.js)
- Monthly aggregation (ISO 8601 - `YYYY-MM`)
- Automatic spending insights
- Monthly expense forecasting using ML model
- Modular architecture ready for MLOps

---

## 🧠 Machine Learning

Model trained using:

- `scikit-learn`
- Dataset: Personal Finance Dataset (Kaggle)
- Features:
  - `ano`
  - `mes`
- Target:
  - `gasto_mensal`

Model file:

```
models/model_gastos.pkl
```

Prediction endpoint:

```
GET /previsao/previsao?ano=2026&mes=3
```

Example response:

```json
{
  "ano": 2026,
  "mes": 3,
  "previsao_gasto": 2430.75
}
```

---

## 🏗️ Project Structure

```
app/
│
├── main.py
├── database.py
├── models.py
│
├── routes/
│   ├── auth.py
│   ├── gastos.py
│   ├── dashboard.py
│   ├── previsao.py
│   └── mlops.py
│
└── models/
    └── model_gastos.pkl
```

---

## 📊 Dashboard

Provides:

- Total spending
- Category distribution (Pie Chart)
- Monthly spending trend (Line Chart)
- Smart recommendations
- Forecast for next month

Frontend stack:

- HTML
- CSS
- JavaScript
- Chart.js

---

## 🔐 Authentication

Session-based authentication using:

- `SessionMiddleware`
- Cookies

Main routes:

```
POST   /login
POST   /gastos/novo
GET    /dashboard/me
GET    /previsao/previsao
```

---

## 🛠️ Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Scikit-Learn
- Pandas
- Joblib
- Chart.js
- Uvicorn

---

## ▶️ Running the Project

### Clone repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### Create virtual environment

```bash
python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start server

```bash
uvicorn app.main:app --reload
```

Access:

```
http://127.0.0.1:8000/docs
```

---

## 📌 Roadmap

- [ ] User-personalized forecasting
- [ ] Forecast vs real comparison
- [ ] JWT authentication
- [ ] Cloud deployment
- [ ] Automated ML retraining pipeline

---

## 👨‍💻 Author

Amorim

---

## 📄 License

MIT License

