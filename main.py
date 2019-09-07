#!/usr/bin/env python3
"""Creates a PyGame window and co-ordinates the fetching of data and
   drawing a chart"""
import pygame
import sys
import config as config
from chart import draw_candlestick_chart
from data_source import import_stock_prices

## application config
FPS = 5 # frames per second limit

## initialise pygame
pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Financial Modelling App")
clock = pygame.time.Clock()

font_name = 'serif' # or None for the default font
font_px = 32
my_font = pygame.font.SysFont(font_name, font_px)

## do we need this __main__ thing???
'''
if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument('s', help='The start date in format: YYYY-MM')
   parser.add_argument('e', help='The end date in format: YYYY-MM')
   args = parser.parse_args()

   start_date = args.s
   end_date = args.e
'''
#### Game loop ####


## what is this event?
company = "AAPL"
start_date = "2014-06"
end_date = "2014-06"
chart_data = import_stock_prices(company, start_date, end_date)
running = True
while running:

   clock.tick(FPS)

   #### Game loop part 1: Event handling #####

   for event in pygame.event.get():

      if event.type == pygame.QUIT:
            running = False
            break



   #### Game loop part 2: Updates #####

   #### Game loop part 3: Draw #####
   screen.fill(config.WHITE)

   # call chart:
   drawing_rect = (0,0,config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
   draw_candlestick_chart(screen, chart_data, drawing_rect)

   # after drawing, make the drawing visible
   pygame.display.flip()

#### Clean up and close program ####

# close the window
pygame.quit()
