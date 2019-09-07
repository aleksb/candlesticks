
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
    #methodlogy - change stock_info dict in list then take the high and low as a perecentage of the height and width of the candlestick
    rect_color = (255, 255, 255)
    h = 400
    x = 400
    y = 200
    cs_w = 50
    stock_info = {"open":153.6368, "high":157.5648, "low":152.9822, "close":156.6423}
    rect_x = x - (cs_w / 2)
    if stock_info["open"] > stock_info["close"]:
        rect_top = ""
    else:
        rect_y = (y + (((stock_info["high"] - stock_info["close"]) / (stock_info["high"] - stock_info["low"])) * h))
        rect_h = (((stock_info["close"] - stock_info["open"]) / (stock_info["high"] - stock_info["low"])) * h)
    rect_w = cs_w / 2
    print(f"rect_x ={rect_x} rect_y = {rect_y} rect_h = {rect_h} rect_w = {rect_w}")
    pygame.draw.rect(screen, (rect_color), (rect_x, rect_y, cs_w, rect_h), 2)
    pygame.draw.line(screen, (rect_color), (x, y), (x, y + h), 2)

    # list_cords = [stock_info[open], stock_info[close], stock_info[low], stock_info[high]]
    # price_difference = list_cords[3] - list_cords[2] / h
    # if list_cords[0] > list_cords[1]:
    #    pass
    # elif list_cords[0] < list_cords[1]:
    #    pass
    # elif list_cords[0] == list_cords[1]:
    #     pass
