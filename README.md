# 📊 FinSightAI

FinSightAI is an AI-powered financial analysis tool that leverages **Alpha Vantage** for real-time US stock market data and **Lyzr Agent** to generate insightful, human-readable financial reports. Whether you're a retail investor, a finance student, or a tech-savvy trader, FinSightAI helps you understand complex company financials in seconds.

---

## 🔐 Prerequisites

Before using this project, make sure you have:

1. **Alpha Vantage API Key**  
   Sign up and get your free API key from:  
   👉 [Alpha Vantage](https://www.alphavantage.co/#page-top)

2. **Lyzr Agent Setup**  
   Create your own Lyzr Agent at:  
   👉 [Lyzr Agent Studio](https://studio.lyzr.ai/)  
   - Create an account or log in  
   - Create a new agent with financial analysis capabilities  
   - Copy your `USER_ID`, `AGENT_ID`, and `LYZR_API_KEY` from the dashboard

---

## 🚀 Features

- 📈 Fetches **real-time financial data** of NASDAQ-listed companies.
- 🧠 Uses **AI agents** to analyze income statements, balance sheets, and cash flows.
- 🧾 Generates **clean, structured markdown reports** including key ratios, risks, and trade recommendations.
- 🔍 Highlights financial health, valuation metrics, and growth potential.
- ⚙️ Built using modern Python frameworks.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI** – Backend framework for API routes
- **Alpha Vantage API** – Real-time financial data provider
- **Lyzr Agent** – AI agent for contextual financial analysis
- **Pydantic** – Data parsing and validation
- **Uvicorn** – ASGI server

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/finsightai.git
cd finsightai
```

2. **nstall dependencies using `uv` (recommended)**

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

Or using `pip`:

```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.env` file:
```bash
API_KEY = your_alpha_vantage_api_key
X_API_KEY = your_lyzr_api_key
USER_ID = your_lyzr_user_id
AGENT_ID = your_lyzr_agent_id
SESSION_ID = yout_lyzr_session_id
```

# How to use
Hit the API endpoint with a company symbol:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/fundamental-analysis' \
  -H 'accept: application/json' \
  -H 'x-api-key: your_lyzr_api_key' \
  -H 'Content-Type: application/json' \
  -d '{
  "symbol": "amzn"
}'

Or 

You can use Swagger UI: 'http://127.0.0.1:8000/docs'
```

# Sample Response:
```bash
{
  "symbol": "AMZN",
  "financial_data": {...},
  "analysis_report": "### COMPANY OVERVIEW\n- <strong>Name:</strong> Amazon.com Inc ...",
}
```


# Sample Output (Report Extract)

### COMPANY OVERVIEW
- **Name:** Amazon.com Inc
- **Symbol:** AMZN
- **Sector:** Trade & Services
- **Industry:** Retail - Catalog & Mail-Order Houses
- **Market Capitalization:** $2.39 trillion

### KEY FINANCIAL INSIGHTS
- **Revenue (TTM):** $637.96B
- **Net Income:** $59.25B
- **Operating Margin:** 10.8%
- **ROE:** 20.72%

### RISKS OR RED FLAGS
- **High Valuation Ratios:** P/E and P/B suggest potential overvaluation
- **Debt-to-Equity:** 1.19 (watch out for leverage)
- **No Dividends Paid**

### FINAL INVESTMENT RECOMMENDATION
- 🔄 **TRADE** – Suitable for short-term trading momentum plays in the tech sector.

