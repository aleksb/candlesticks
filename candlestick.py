
def calc_rect(screen, x, y, width, height, stock_info, close_high):
    '''
    calculates the values for the rect of the candlestick using screen, x, y, width, height and stock_info\n
    uses the close_high bool to determine if the top the rect is close or the open and the color the rect should be.
    '''
    rect_x = x - (width / 2)
    if close_high is True:
        rect_y = (y + (((stock_info["high"] - stock_info["close"]) / (stock_info["high"] - stock_info["low"])) * h))
        rect_h = (((stock_info["close"] - stock_info["open"]) / (stock_info["high"] - stock_info["low"])) * h)
        rect_values = (screen, (0, 0, 0), (rect_x, rect_y, width, rect_h), 2)
        return rect_values
    elif close_high is False:
        rect_y = (y + (((stock_info["high"] - stock_info["open"]) / (stock_info["high"] - stock_info["low"])) * h))
        rect_h = (((stock_info["close"] - stock_info["open"]) / (stock_info["high"] - stock_info["low"])) * h)
        rect_values = (screen, (0, 0, 0), (rect_x, rect_y, width, rect_h))
        return rect_values

def draw_candlestick(screen, x, y, h, cs_w, stock_info):
    """Draws a candlestick
    * screen
       * x - x co-ordinate of candlestick centre
       * y - origin y
       * h - height of candlestick - changed to the height of the candlestick
       * cs_w - candlestick_width
       * stock_info - {
            'open': usd,
            'close': usd,
            'low': usd,
            'high': usd,
        }
    """
    pygame.draw.line(screen, (0, 0, 0), (x, y), (x, y + h), 2)
    if stock_info["close"] > stock_info["open"]:
        rect_values = calc_rect(screen, x, y, cs_w, h, stock_info, True)
        pygame.draw.rect(rect_values[0], rect_values[1], rect_values[2], rect_values[3])
        #Draws a white rect to cover the line inside the first rect
        pygame.draw.rect(rect_values[0], (255, 255, 255), (rect_values[2][0] + 2, rect_values[2][1] + 2, rect_values[2][2] - 4, rect_values[2][3] - 2))
    else:
        rect_values = calc_rect(screen, x, y, cs_w, h, stock_info, False)
        pygame.draw.rect(rect_values[0], rect_values[1], rect_values[2])