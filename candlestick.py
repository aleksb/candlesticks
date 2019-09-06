
def draw_candlestick(screen, x, y, h, cs_w, stock_info):
    """Draws a candlestick
       
       * screen
       * x - x co-ordinate of candlestick centre
       * y - origin y
       * h - height of chart
       * cs_w - candlestick_width
       * stock_info - {
           'open': usd,
           'close': usd,
           'low': usd,
           'high': usd,
         }
       """
