from fastapi import FastAPI, HTTPException, Security, status
from fastapi.params import Depends
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from Services.finance_data import fundamental_analysis
from LyzrAgent.agent import chat_with_agent

app = FastAPI(
    title="Stock Data Tool API",
    description="API for performing fundamental analysis on stock data using Lyzr Agent.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY_NAME = "x-api-key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


def get_api_key(api_key: str = Security(api_key_header)):
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="API key is missing"
        )
    
    return api_key


                

@app.get("/")
async def root():
    return {"message": "Welcome to the Stock Data Tool API"}


class TickerRequest(BaseModel):
    symbol: str

@app.post("/fundamental-analysis")
async def fundamental_analysis_report(request: TickerRequest, api_key: str = Depends(get_api_key)):
    symbol = request.symbol.upper()

    try:
        financial_data = fundamental_analysis(symbol)
        if not financial_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No financial data found for ticker: {symbol}"
            )
        analysis_report = chat_with_agent(
            message=f"Financial Data:\n{financial_data}",
            user_api_key=api_key)
        
        if not analysis_report:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to get analysis report from Lyzr Agent"
            )
        
        return {
            "symbol": symbol,
            "financial_data": financial_data,
            "analysis_report": analysis_report
        }
            
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )