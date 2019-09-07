#!/usr/bin/env python3
"""Creates a PyGame window and co-ordinates the fetching of data and
   drawing a chart"""
import argparse
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

##
## Main Program
##
if __name__ == "__main__":
   ## Take Company Name, Start Date and End Date from the command line at runtime
   parser = argparse.ArgumentParser()
   parser.add_argument('-n', help='The company name')
   parser.add_argument('-s', help='The start date in format: YYYY-MM')
   parser.add_argument('-e', help='The end date in format: YYYY-MM')
   args = parser.parse_args()

   company_name = args.n
   start_date = args.s
   end_date = args.e

## Get chart data in nice python format
chart_data = import_stock_prices(company_name, start_date, end_date)

## Draw screen background
screen.fill(config.WHITE)

## Draw chart
drawing_rect = (0,0,config.SCREEN_WIDTH, config.SCREEN_HEIGHT)
draw_candlestick_chart(screen, chart_data, drawing_rect, my_font)

## After drawing, make the drawing visible
pygame.display.flip()

## Event Handling Loop
running = True
while running:
   clock.tick(FPS)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
            running = False
            break

## Clean up and close program
pygame.quit()
