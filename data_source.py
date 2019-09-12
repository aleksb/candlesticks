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
    stock_data = requests.get(URL + company + "?from=" + start_date + '-01&to=' + end_date + '-31')
    #return stock_data.json()
    dump = stock_data.json()

    count = 0

    lowsum = []
    #lowmin = 0

    highsum = []
    #highmax = 0

    #stock_average = 0
    stock_list = []

    for data in (dump['historical']):
        print(data['low'])
        lowsum.append(data['low'])
        highsum.append(data['high'])
        count += 1
        final_dict = {
            'ticker_symbol': dump['symbol'],
            'price_history': [
                {
                    'open': data['open'],
                    'close': data['close'],
                    'low': data['low'],
                    'high': data['high'],
                    'date': data['label'],
                }
            ]
        }
        stock_list.append(final_dict)
    return stock_list


stock_list = (import_stock_prices('AAPL', '2019-03', '2019-05'))
print(stock_list)
