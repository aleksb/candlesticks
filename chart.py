"""
Draws a candlestick chart on a PyGame screen.
"""

import json
import pygame
import datetime
from pygame.locals import QUIT
from config import (
    WHITE, BLACK, UP_CANDLE_COLOUR,
    AVG_LINE_COLOUR, SCREEN_WIDTH, SCREEN_HEIGHT
)
from candlestick import (
    draw_candlestick
)
from axes import draw_x_axis, draw_y_axis
SAMPLE_DATA = '{"ticker_symbol": "EXPL", "price_history": [{"open": 14.0,"close": 14.1,"low": 15.0,"high": 14.0,"date": ""}]}'

def draw_candlestick_chart(screen, chart_data, drawing_rect):
    """
    draws a candlestick chart at a particular position
       * screen is a PyGame surface
       * chart_data formatted as described in README.md.
       * drawing_rect is (x, y, w, h)
    """
    data = json.loads(SAMPLE_DATA)
    print(data)
    pygame.init()
    high_line = ((data["price_history"][0]['high'], 120), (data["price_history"][0]['close'], 100))
    stock_data = (80, 150 + data["price_history"][0]['close'], 40, data["price_history"][0]['open'] - data["price_history"][0]['close'])

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    my_font = pygame.font.SysFont('Noto Sans', 18)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 5)
        pygame.draw.rect(screen, BLACK, stock_data)

        #draw_candlestick(screen, False, stock_data)
        title = my_font.render(
            f'Stock Prices for {data["ticker_symbol"]}', True, BLACK)
        screen.blit(title, (430, 50))
        y_subtitle = my_font.render(
            f'Min and Max Price ($)', True, BLACK)
        y_subtitle = pygame.transform.rotate(y_subtitle, 90)
        x_subtitle = my_font.render(
            'Date Range - Daily', True, BLACK
        )
        screen.blit(x_subtitle, (430, 680))
        screen.blit(y_subtitle, (40, 300))
        pygame.display.flip()

draw_candlestick_chart(None, None, None)
# other defs can go here


