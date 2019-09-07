

def draw_x_axis(screen, x, y, w, start_date, end_date):
       """Draws the x axis
       
       * screen
       * x - origin x
       * y - origin y
       * w - width
       * start_date - datetime.date (first day of data)
       * end_date - datetime.date (last day of data + 1)

       note that (end_date - start_date) is the number of days
       in that period
       """
       pygame.draw.line(screen, BLACK, True, (x,y), (w,y), 2)
       text_start_date = my_font.render(f"{start_date}", True, BLACK)
       text_end_date = my_font.render(f"{end_date}", True, BLACK)
       text_start_date = pygame.transform.rotate(text_start_date, 90)
       text_end_date = pygame.transform.rotate(text_end_date, 90)
       screen.blit(text_start_date, (x,y))
       screen.blit(text_end_date, (w,y))
       num_candlesticks = (end_date - start_date).days
       


def draw_y_axis(screen, x, y, h, min_price, max_price):
       """Draws the y axis
       
       * screen
       * x - origin x
       * y - origin y
       * h - height
       * min_price - in USD
       * max_price - in USD
       """
       pygame.draw.lines(screen, BLACK , False, [(x,y),(x,h)], 2)
       text_snippet_min = my_font.render(f"{min_price}", True, BLACK)
       screen.blit(text_snippet_min, ((x-50), (y+h)))
       text_snippet_max = my_font.render(f"{max_price}", True, BLACK)
       screen.blit(text_snippet_max, ((x-50), (y+5)))
       
       spread = max_price - min_price
       
       text_snippet_mid = my_font.render(f"{max_price-spread/2}", True, BLACK)
       # screen.blit(text_snippet_mid,())
       
              

