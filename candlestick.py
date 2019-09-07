
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
    list_cords = [stock_info[open], stock_info[close], stock_info[low], stock_info[high]]
    price_difference = list_cords[3] - list_cords[2] / h
    if list_cords[0] > list_cords[1]:
       pass
    elif list_cords[0] < list_cords[1]:
       pass
    elif list_cords[0] == list_cords[1]:
        pass
    pygame.draw.line(screen, (BLACK), (start_pos), (end_pos), 2)
    pygame.draw.rect(screen, (rect_color), (rect_x, rect_y, rect_w, rect_h), 2)
