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
SAMPLE_DATA = '{"symbol": "EXPL", "historical": [{"open": 14.0,"close": 14.1,"low": 15.0,"high": 14.0,"date": ""}]}'

def draw_candlestick_chart(screen, chart_data, drawing_rect):
    """
    draws a candlestick chart at a particular position
       * screen is a PyGame surface
       * chart_data formatted as described in README.md.
       * drawing_rect is (x, y, w, h)
    """
    my_font = pygame.font.SysFont('Noto Sans', 18)
    high_line = ((chart_data["historical"][0]['high'], 120), (chart_data["historical"][0]['close'], 100))
    candlestick_points = (
        80, 150 + chart_data["historical"][0]['close'], 40,
        chart_data["historical"][0]['open'] - chart_data["historical"][0]['close']
    )
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, drawing_rect, 5)
    pygame.draw.rect(screen, BLACK, candlestick_points)
    # draw_candlestick(screen, False, stock_data)
    title = my_font.render(
        f'Stock Prices for {chart_data["symbol"]}', True, BLACK)
    y_subtitle = my_font.render(
        f'Min and Max Price ($)', True, BLACK)
    y_subtitle = pygame.transform.rotate(y_subtitle, 90)
    x_subtitle = my_font.render(
        'Date Range - Daily', True, BLACK
    )
    screen.blit(title, (430, 50))
    screen.blit(x_subtitle, (430, 680))
    screen.blit(y_subtitle, (40, 300))
    pygame.display.flip()

# other defs can go here


if __name__ == "__main__":
    pygame.init()
    data = json.loads(SAMPLE_DATA)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
        draw_candlestick_chart(screen, data, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))