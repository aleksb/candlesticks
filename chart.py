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

SAMPLE_DATA = '{"ticker_symbol": "EXPL", "price_history": [{"open": 14.0,"close": 14.1,"low": 15.0,"high": 14.0,"date": ""}]}'

def draw_candlestick_chart(screen, chart_data, drawing_rect):
    """
    draws a candlestick chart at a particular position
       * screen is a PyGame surface
       * chart_data formatted as described in README.md.
       * drawing_rect is (x, y, w, h)
    """
    data = json.loads(SAMPLE_DATA)
    print(SAMPLE_DATA)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # my_font = pygame.font.SysFont(FONT_NAME, FONT_PX)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), 2)
        pygame.display.flip()

draw_candlestick_chart(None, None, None)
# other defs can go here


