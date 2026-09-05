import yfinance as yf
from colorama import Fore, Style, init

init(autoreset=True)


def get_quote_yfinance(ticker):
    dat = yf.Ticker(ticker)

    current_price = dat.fast_info.last_price
    prev_close = dat.fast_info.previous_close

    if prev_close is None or prev_close == 0:
        print(f"{ticker}: ${current_price:.2f} (no previous close)")
        return

    percent_change = ((current_price - prev_close) / prev_close) * 100

    color = Fore.GREEN if percent_change >= 0 else Fore.RED

    # For Canadian-listed tickers ending in .TO, strip the suffix for display
    label = ticker[:-3] if ticker.endswith(".TO") else ticker
    print(
        f"{label}: ${current_price:.2f} ({color}{percent_change:.2f}%{Style.RESET_ALL})"
    )


def main():
    my_list = ['AAPL.TO', 'MSFT.TO', 'MU.TO', 'VRT.TO', 'XEQT.TO']

    for ticker in my_list:
        get_quote_yfinance(ticker)


if __name__ == '__main__':
    main()
