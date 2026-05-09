# Fraud Detection API 🔍

A fraud detection system built using **MapReduce (mrjob)** for processing transaction data and **Flask** for exposing the results via a REST API.

---

##  Project Overview

This project processes transaction data to identify fraudulent transactions using a MapReduce job and exposes the results through a Flask API endpoint. It was built as part of a Cloud Computing lab to demonstrate big data processing and API development.

---

##  Technologies Used

- **Python 3.11**
- **mrjob** — MapReduce framework for processing transaction data
- **Flask** — Web framework for building the REST API
- **Thunder Client / Postman** — For API testing

---

##  Project Structure

```
CloudComputing Lab/
│
├── transaction_count.py   # MapReduce job for counting fraudulent transactions
├── app.py                 # Flask API to expose fraud detection results
├── transactions.csv       # Sample transaction data
└── README.md              # Project documentation
```

---

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/chesergon/Fraud-detection-API.git
cd Fraud-detection-API
```

**2. Install dependencies**
```bash
pip install mrjob flask
```

---

## 📊 Transaction Data Format

The `transactions.csv` file should follow this format:

```
transaction_id,amount,is_fraud
1,500,1
2,200,0
3,1500,1
4,300,0
```

- `is_fraud = 1` → Fraudulent transaction
- `is_fraud = 0` → Legitimate transaction

---

##  Running the MapReduce Job

To run the fraud detection MapReduce job directly:

```bash
python transaction_count.py transactions.csv
```

**Expected output:**
```
"fraud"    3
```

This tells you how many fraudulent transactions were found.

---

## Running the Flask API

Start the Flask server:

```bash
python app.py
```

The server will start at `http://127.0.0.1:5000`

---

##  API Endpoint

### POST `/process`

Accepts a list of transactions and returns the fraud count.

**Request Body:**
```json
{
  "transactions": [
    "1,1000,1",
    "2,500,0",
    "3,1500,1",
    "4,700,0",
    "5,300,1"
  ]
}
```

**Response:**
```json
{
  "fraudulent_transactions": 3
}
```

---

##  Testing the API

You can test the API using **Thunder Client** (VS Code extension) or **Postman**:

1. Set request type to **POST**
2. Enter URL: `http://127.0.0.1:5000/process`
3. Set body to **JSON** and paste the transaction data
4. Click **Send**

---

##  How It Works

1. **Mapper** — reads each transaction line, checks if `is_fraud == 1` and flags it by yielding `("fraud", 1)`
2. **Reducer** — counts all flagged transactions and returns the total fraud count
3. **Flask API** — receives transaction data via POST request, triggers the MapReduce job and returns the fraud count as a JSON response

---

##  Known Limitations

- Currently processes data synchronously — large datasets may cause timeouts
- Designed for development use only — not suitable for production deployment
- Uses a development Flask server — a production WSGI server is recommended for deployment

---

##  Future Improvements

- Implement asynchronous processing with job IDs
- Add more API endpoints for different teams
- Deploy to cloud (AWS EMR) for large scale processing
- Add a frontend dashboard for non-technical users

---

## 👩‍💻 Author

**Lyne Chesergon**  
[GitHub](https://github.com/chesergon)

---
