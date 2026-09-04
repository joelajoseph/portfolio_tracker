import requests
import yfinance as yf
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("FINNHUB_API_KEY")


def get_quote_yfinance(ticker):
    # create ticker object called 'dat'
    dat = yf.Ticker(ticker)

    # grab what we need
    current_price = dat.fast_info.last_price
    last_price = dat.fast_info.last_price
    prev_close = dat.fast_info.previous_close

    # calculate the daily percent change
    percent_change = ((last_price - prev_close) / # type: ignore
                      prev_close) * 100  

    print(f"{ticker[:-3]}: ${current_price:.2f} ({percent_change:.2f}%)")


def get_quote(ticker):
    # make the api call and check response
    url = f"https://finnhub.io/api/v1/quote?symbol={ticker}&token={api_key}"
    r = requests.get(url)

    if r.status_code != 200:
        print(f"Request failed: {r.text}")
        return

    # store the response as a python dictionary
    response_dict = r.json()

    # print what we need
    price = response_dict.get('c')
    percent_change = response_dict.get('dp')
    if price is None or percent_change is None:
        print(f"Missing quote data for {ticker}: {response_dict}")
        return

    print(f"{ticker}: ${price:.2f} ({percent_change:.2f}%)")


my_list = ['AAPL', 'MSFT', 'MU', 'VRT', 'XEQT.TO']

for ticker in my_list:
    if ticker == 'XEQT.TO':
        get_quote_yfinance(ticker)
    else:
        get_quote(ticker)
