

def import_stock_prices(company, start_date, end_date):
    """Imports a range of stock prices from an API.

    
       * company - string company name (must be uppercase)
       * start_date - datetime.date object
       * end_date - datetime.date object
       Returns stock data formatted as described in README.md.
       """
