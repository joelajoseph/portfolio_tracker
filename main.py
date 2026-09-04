import requests
import yfinance as yf
from dotenv import load_dotenv
import os
import colorama
from colorama import Fore, Style, init

load_dotenv()
api_key = os.getenv("FINNHUB_API_KEY")

colorama.init()
init(autoreset=True)

# FOR CANADIAN STOCKS
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

    color = Fore.GREEN if percent_change >= 0 else Fore.RED

    print(
    f"{ticker[:-3]}: ${current_price:.2f} ({color}{percent_change:.2f}%{Style.RESET_ALL})"
    )

# FOR U.S. STOCKS
# def get_quote(ticker):
#     # make the api call and check response
#     url = f"https://finnhub.io/api/v1/quote?symbol={ticker}&token={api_key}"
#     r = requests.get(url)

#     if r.status_code != 200:
#         print(f"Request failed: {r.text}")
#         return

#     # store the response as a python dictionary
#     response_dict = r.json()

#     # print what we need
#     price = response_dict.get('c')
#     percent_change = response_dict.get('dp')
#     if price is None or percent_change is None:
#         print(f"Missing quote data for {ticker}: {response_dict}")
#         return

#     color = Fore.GREEN if percent_change >= 0 else Fore.RED

#     print(
#     f"{ticker}: ${price:.2f} ({color}{percent_change:.2f}%{Style.RESET_ALL})"
#     )


my_list = ['AAPL.TO', 'MSFT.TO', 'MU.TO', 'VRT.TO', 'XEQT.TO']

for ticker in my_list:
    get_quote_yfinance(ticker)
