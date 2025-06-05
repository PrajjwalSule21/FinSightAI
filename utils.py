import difflib
import json
import pandas as pd
import yfinance as yf
import pandas as pd


def get_ticker_symbol(company_name: str) -> str:
    with open("symbol_map.json", "r", encoding="utf-8") as f:
        company_ticker_map = json.load(f)

    company_name = company_name.lower()
    lower_map = {name.lower(): symbol for name, symbol in company_ticker_map.items()}
    close_match = difflib.get_close_matches(company_name, lower_map.keys(), n=1)

    if close_match:
        return lower_map[close_match[0]]
    
    return None



def extract_company_info(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    
    company_info = ticker.info
    
    extracted_info = {
        'Symbol': ticker_symbol,
        'Name': company_info.get('longName'),
        'Industry': company_info.get('industry'),
        'Sector': company_info.get('sector'),
        'Address': f"{company_info.get('address1')}, {company_info.get('address2')}, {company_info.get('city')}, {company_info.get('country')}",
        'Phone': company_info.get('phone'),
        'Website': company_info.get('website'),
        'Description': company_info.get('longBusinessSummary'),
        'Full-Time Employees': company_info.get('fullTimeEmployees'),
        'Trailing P/E': company_info.get('trailingPE'),
        'Forward P/E': company_info.get('forwardPE'),
        'Trailing EPS': company_info.get('trailingEps'),
        'Forward EPS': company_info.get('forwardEps'),
        'Dividend Rate': company_info.get('dividendRate'),
        'Dividend Yield': company_info.get('dividendYield'),
        'Beta': company_info.get('beta'),
        'Market Cap': company_info.get('marketCap'),
        '52-Week High': company_info.get('fiftyTwoWeekHigh'),
        '52-Week Low': company_info.get('fiftyTwoWeekLow'),
        'Revenue': company_info.get('totalRevenue'),
        'Gross Margins': company_info.get('grossMargins'),
        'Operating Margins': company_info.get('operatingMargins'),
        'Net Income': company_info.get('netIncomeToCommon'),
        'Debt to Equity': company_info.get('debtToEquity'),
        'Book Value': company_info.get('bookValue'),
        'Price to Book': company_info.get('priceToBook'),
        'Analyst Recommendation Mean': company_info.get('recommendationMean'),
        'Target Mean Price': company_info.get('targetMeanPrice'),
        'Current Price': company_info.get('currentPrice'),
        'Revenue Growth': company_info.get('revenueGrowth'),
        'Earnings Growth': company_info.get('earningsGrowth')
    }
    
    return extracted_info



def comp_symbol_map():
    df = pd.read_csv("equity_data/equity.csv")
    df.columns = [col.strip().upper() for col in df.columns]

    company_names = df["NAME OF COMPANY"].astype(str).str.strip()
    symbol_map = dict(zip(company_names, df["SYMBOL"].astype(str).str.strip()))

    with open("symbol_map.json", "w", encoding="utf-8") as f:
        json.dump(symbol_map, f, ensure_ascii=False, indent=4)

    return symbol_map