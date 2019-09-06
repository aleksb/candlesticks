#!/usr/bin/env python3
import requests

def import_stock_prices(company, start_date, end_date):
    """Imports a range of stock prices from an API.

    
        * company - string company name (must be uppercase)
        * start_date - e.g year-date-month
        * end_date -  e.g year-date-month
        Returns stock data formatted as described in README.md.
        """

    URL = 'https://financialmodelingprep.com/api/v3/historical-price-full/'
    stock_data = requests.get(URL + company + "?from=" + start_date + '-01' + "&to=" + end_date + '-31')
    return stock_data.json()

dump = import_stock_prices('AAPL', '2018-03', '2018-04')
count = 0
lowsum = []

#testing averaging lows
for data in dump:
    for key in data:
        try:
            lowsum.append(dump['historical'][count]['low'])
            count += 1
            print(sum(lowsum) / count)
        except:
            break

