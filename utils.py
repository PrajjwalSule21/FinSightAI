import requests
import os
from dotenv import load_dotenv; load_dotenv()

API_KEY = os.getenv("API_KEY")  # Replace with your real API key

# Fetch income statement
def fetch_income_statement(symbol: str):
    url = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data["annualReports"][0] if "annualReports" in data else None

# Fetch balance sheet
def fetch_balance_sheet(symbol: str):
    url = f"https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data["annualReports"][0] if "annualReports" in data else None

# Fetch cash flow statement
def fetch_cash_flow(symbol: str):
    url = f"https://www.alphavantage.co/query?function=CASH_FLOW&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data["annualReports"][0] if "annualReports" in data else None

# Fetch company overview
def fetch_overview(symbol: str):
    url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url)
    return response.json()

# Calculate financial ratios and metrics
def calculate_ratios(income, balance, cash_flow, overview):
    def safe_div(numerator, denominator):
        try:
            return float(numerator) / float(denominator)
        except:
            return None

    return {
        "EPS": overview.get("EPS"),
        "Revenue": income.get("totalRevenue"),
        "Gross Profit": income.get("grossProfit"),
        "Operating Income": income.get("operatingIncome"),
        "Net Income": income.get("netIncome"),

        "Total Assets": balance.get("totalAssets"),
        "Total Liabilities": balance.get("totalLiabilities"),
        "Shareholder Equity": balance.get("totalShareholderEquity"),
        "Book Value per Share": overview.get("BookValue"),

        "Operating Cash Flow": cash_flow.get("operatingCashflow"),
        "Investing Cash Flow": cash_flow.get("cashflowFromInvestment"),
        "Financing Cash Flow": cash_flow.get("cashflowFromFinancing"),
        "Free Cash Flow": cash_flow.get("freeCashFlow"),

        # Valuation
        "P/E Ratio": overview.get("PERatio"),
        "P/B Ratio": overview.get("PriceToBookRatio"),
        "P/S Ratio": overview.get("PriceToSalesRatioTTM"),
        "Market Capitalization": overview.get("MarketCapitalization"),
        "Dividend Yield": overview.get("DividendYield"),

        # Profitability
        "ROE": safe_div(income.get("netIncome"), balance.get("totalShareholderEquity")),
        "ROA": safe_div(income.get("netIncome"), balance.get("totalAssets")),
        "Gross Margin": safe_div(income.get("grossProfit"), income.get("totalRevenue")),
        "Operating Margin": safe_div(income.get("operatingIncome"), income.get("totalRevenue")),
        "Net Profit Margin": safe_div(income.get("netIncome"), income.get("totalRevenue")),

        # Leverage & Liquidity
        "Debt-to-Equity Ratio": safe_div(balance.get("totalLiabilities"), balance.get("totalShareholderEquity")),
        "Current Ratio": overview.get("CurrentRatio"),
        "Quick Ratio": overview.get("QuickRatio"),
        "Interest Coverage Ratio": overview.get("InterestCoverage")
    }