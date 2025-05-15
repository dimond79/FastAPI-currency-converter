# Currency Converter API 🌍💱

## 📌 Project Overview

This **Currency Converter API** is a FastAPI-based microservice designed for real-time currency conversion. It leverages the **ExchangeRate-API** to fetch live exchange rates and provides a seamless way to convert amounts between different currencies.

---

## 📂 Repository

Clone the repository to get started:

```bash
git clone https://github.com/dimond79/FastAPI-currency-converter.git  
cd Currency-converter  
```

---

## 🧑‍💻 Setup Instructions

### 🔧 1. Environment Configuration

1. Create a `.env` file in the root directory:

   ```plaintext
   EXCHANGE_API_KEY=your_real_key  
   EXCHANGE_API_URL=https://v6.exchangerate-api.com/v6  
   ```

2. Replace `your_real_key` with your API key from [ExchangeRate-API](https://www.exchangerate-api.com).

---

### 🛠️ 2. Install Dependencies

Ensure you have Python installed (preferably Python 3.9+). Then run:

```bash
pip install -r requirements.txt  
```

---

### 🖥️ 3. Run the Development Server

Start the FastAPI server:

```bash
uvicorn app.main:app --reload  
```

You can access the interactive API documentation at:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🛠️ Configuration Notes

* **API Key**: Obtain your free API key from [ExchangeRate-API](https://www.exchangerate-api.com).
* **Base URL**: The API URL in `.env` should follow this format:

  ```plaintext
  https://v6.exchangerate-api.com/v6  
  ```
* **API Endpoint**: The full endpoint appends your key and base currency like this:

  ```plaintext
  https://v6.exchangerate-api.com/v6/YOUR_KEY/latest/USD  
  ```

---

## 📜 License

This project is licensed under the MIT License.
