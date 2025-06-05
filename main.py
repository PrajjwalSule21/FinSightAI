from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils import calculate_ratios, fetch_balance_sheet, fetch_cash_flow
from utils import fetch_income_statement, fetch_overview
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TickerRequest(BaseModel):
    symbol: str

@app.post("/fundamental-analysis")
async def fundamental_analysis(request: TickerRequest):
    symbol = request.symbol.upper()

    try:
        income = fetch_income_statement(symbol)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch income statement: {e}")

    try:
        balance = fetch_balance_sheet(symbol)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch balance sheet: {e}")

    try:
        cash_flow = fetch_cash_flow(symbol)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch cash flow statement: {e}")

    try:
        overview = fetch_overview(symbol)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch overview: {e}")

    if not all([income, balance, cash_flow, overview]):
        raise HTTPException(status_code=404, detail=f"Incomplete financial data for symbol: {symbol}")

    try:
        report = calculate_ratios(income, balance, cash_flow, overview)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to calculate ratios: {e}")

    return {
        "name": overview.get("Name"),
        "symbol": symbol,
        "income_statement": income,
        "balance_sheet": balance,
        "cash_flow": cash_flow,
        "overview": overview,
        "ratios": report
    }
