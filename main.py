from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils import extract_company_info, get_ticker_symbol
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CompanyRequest(BaseModel):
    company_name: str


@app.post("/company-info")
async def get_company_info(payload: CompanyRequest):
    company_name = payload.company_name
    ticker_symbol = get_ticker_symbol(company_name)

    if not ticker_symbol:
        raise HTTPException(status_code=404, detail="Ticker symbol not found for given company name.")

    try:
        company_data = extract_company_info(f"{ticker_symbol}.NS")
        return company_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))