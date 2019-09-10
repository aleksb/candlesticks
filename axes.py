import pygame
from config import BLACK
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
       pass
       


def draw_y_axis(screen, x, y, h, min_price, max_price):
       """Draws the y axis
       
       * screen
       * x - origin x
       * y - origin y
       * h - height
       * min_price - in USD
       * max_price - in USD
       """
       pygame.draw.aaline(screen, BLACK, x, y, 10)
       # text_snippet_min = my_font.render(f"{min_price}", True, BLACK)
       # screen.blit(text_snippet_min, ((x-50), (y+h)))
       # text_snippet_max = my_font.render(f"{max_price}", True, BLACK)
       # screen.blit(text_snippet_max, ((x-50), (y+5)))
       
       spread = max_price - min_price
       
       # text_snippet_mid = my_font.render(f"{max_price-spread/2}", True, BLACK)
       # screen.blit(text_snippet_mid,())


