import urllib.request
import re
import sys
import pandas_datareader.data as web
from datetime import datetime
from datetime import timedelta


def get_quote(ticker):
    start = datetime.today()-timedelta(days=1)
    end = datetime.today()
    prices = web.DataReader(ticker, 'yahoo', start, end)
    close = prices['Close']
    return str(float(close[0]))


def get_estimate(symbol):
    base_url = 'https://tw.stock.yahoo.com/d/s/dividend_'
    content = urllib.request.urlopen(
        base_url + symbol + '.html').read().decode("big5")
    match = re.findall('<td align="center">(.*?)</td>', content)
    dif = 0
    if match:
        avg = 0
        print('\nLast 5 years dividend are')
        for i in range(5):
            avg += float(match[4+i*5])
            print(match[4+i*5])

        avg = avg/5
        print('\nAverage dividen of the past 5 year is', avg)
        r = float(avg)*20
        print('current reasonable price for 5% dividend price ratio might be ', r)
        r = float(avg)*25
        print('current reasonable price for 4% dividend price ratio might be ', r)
        r = float(avg)*50
        print('current reasonable price for 2% dividend price ratio might be ', r)
    else:
        print('Get dividen failure ' + symbol)


def target_dividend_yield(symbol):
    print(' === ' + symbol + ' === ' +
          ' current price is ' + get_quote(symbol+'.TW'))
    get_estimate(symbol)


if __name__ == "__main__":
    try:
        stocklist = open(sys.argv[1]).read().splitlines()
        print('\n')
        for line in stocklist:
            target_dividend_yield(line)
            print('\n')
    except KeyboardInterrupt:
        print("\n\nUser Press Ctrl+C,Exit")
