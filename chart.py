"""
Draws a candlestick chart on a PyGame screen.
"""

import json
import pygame
import datetime
import math
from operator import (
    itemgetter
)
from pygame.locals import QUIT
from config import (
    WHITE, BLACK, GREEN, RED, UP_CANDLE_COLOUR,
    AVG_LINE_COLOUR, SCREEN_WIDTH, SCREEN_HEIGHT
)
from candlestick import (
    draw_candlestick
)
from axes import draw_x_axis, draw_y_axis



def draw_candlestick_chart(screen, chart_data, drawing_rect, my_font):
    """
    draws a candlestick chart at a particular position
       * screen is a PyGame surface
       * chart_data formatted as described in README.md.
       * drawing_rect is (x, y, w, h)
    """
    window = 5
    historical = chart_data['historical']
    graph = pygame.draw.rect(
        screen,
        BLACK,
        drawing_rect, window
    )

    x_xaxis, y_xaxis = get_coordinates(
        graph, "x_axis"
    )

    x_axis = draw_x_axis_joe(
        screen,
        x_xaxis, y_xaxis,
    )
    x_yaxis, y_yaxis = get_coordinates(
        graph, "y_axis"
    )

    y_axis = draw_y_axis_joe(
        screen,
        x_yaxis, y_yaxis
    )

    draw_title(
        screen,
        my_font,
        chart_data["symbol"],
        graph
    )

    draw_subtitles(
        screen,
        my_font,
        x_axis,
        graph,
        y_axis
    )
    # draw_candlestick(screen, False, stock_data)
    xlabels = draw_x_labels(
        screen,
        x_axis,
        historical
    )
    high, low = find_high_low(historical)

    y_length = y_axis.bottom - y_axis.top
    # generate appropriate scaling for graph
    unit = y_length / (high - low)
    y_labels = draw_y_labels(
        screen,
        y_axis,
        unit
    )
    candle_length = (xlabels[1].left - xlabels[0].left) / 2 # length between each stroke
    for i, label in enumerate(xlabels):
        make_candlestick_demo(
            screen, label,
            historical[i], y_axis,
            unit, candle_length, high, low
        )
    pygame.display.flip()

def find_high_low(historical):
    highest_highs = sorted(
        historical,
        key=itemgetter('high'),
        reverse=True
    )
    # sort lowest on order
    lowest_lows = sorted(
        historical,
        key=itemgetter('low')
    )
    
    return (
        highest_highs[0]['high'],
        lowest_lows[0]['low']
    )

def make_candlestick_demo(screen, label, stock_data, y_axis, *vals):
    unit, candle_length, high, low = vals
    ends_high = stock_data['close'] > stock_data['open']
    high_point = (
        stock_data['close']
        if ends_high
        else stock_data['open']
    )
    low_point = (
        stock_data['close']
        if not ends_high
        else stock_data['open']
    )
    line = pygame.draw.line(
        screen, BLACK,
        (
            label.left,
            y_axis.top + unit * (
                high - stock_data['high']
                )
            ),
        (
            label.left,
            y_axis.top + unit * (
                high - stock_data['low']
                )
            )
    )
    color = GREEN if ends_high else RED
    high_offset = unit * (
        high - high_point
    )
    low_offset = unit * (
        high - low_point
    )

    pygame.draw.rect(
        screen, color,
        (
            label.left - candle_length/2,
            y_axis.top + high_offset,
            candle_length,
            low_offset - high_offset
        )
    )

def get_coordinates(graph, cooridinates):
    return {
        "x_axis": ((
            graph.left + 100,
            graph.bottom - 100
        ), (
            graph.right - 100,
            graph.bottom - 100
        )),
        "y_axis": ((
            graph.left + 100,
            graph.bottom - 100
        ), (
            graph.left + 100,
            graph.top + 100
        ))
    }.get(cooridinates)


# other defs can go here
def draw_x_axis_joe(screen, x, y):
    """
    draw x axis but return rect object. this will provide properties
    like left, right. bottom, top and center
    """
    return pygame.draw.line(screen, BLACK, x, y)

def draw_y_axis_joe(screen, x, y):
    """
    same thing, this will return a rect object with helpful props
    """
    return pygame.draw.line(screen, BLACK, x, y)

def draw_title(screen, my_font, symbol, graph):
    """
    draw title
    """
    title = my_font.render(
    f'Stock Prices for {symbol}', True, BLACK)
    title_left, title_right = graph.center[0] - 120, graph.top + 50
    screen.blit(title, (title_left, title_right))

def draw_subtitles(screen, my_font, x_axis, graph, y_axis):
    """
    draw subtitles using the x axis rect object. for a reference
    """
    y_subtitle = my_font.render(
    f'Min and Max Price ($)', True, BLACK)
    y_subtitle = pygame.transform.rotate(y_subtitle, 90)
    x_subtitle = my_font.render(
        'Date Range - Daily', True, BLACK
    )

    xsub_left, xsub_right = x_axis.center[0] - 80, graph.bottom - 80
    ysub_left, ysub_right = graph.left + 25, y_axis.center[0] + 120
    screen.blit(x_subtitle, (xsub_left, xsub_right))
    screen.blit(y_subtitle, (ysub_left, ysub_right))

def draw_x_labels(screen, x_axis, dates):
    """
    I want this to return
    return a list of lines (Rects) this way i can easily determine candlestick center
    """
    labels = []
    x_axis_length = x_axis.right - x_axis.left
    stroke = int(x_axis_length / len(dates))
    for value in range(
        x_axis.left + stroke,
        x_axis_length + stroke * 2,
        stroke
    ):
        labels.append(pygame.draw.line(
            screen, BLACK,
            (value, x_axis.bottom),
            (value, x_axis.bottom + 5)
        ))
    return labels
def draw_y_labels(screen, y_axis, unit):
    """
    draw y labels, these should be returned as rects as well
    """

    point = y_axis.top
    for value in range(point, y_axis.bottom, int(unit/2)):
        pygame.draw.line(
            screen, BLACK,
            (y_axis.left, value),
            (y_axis.left - 10, value)
        )


# change the dict values as recieved from the api
SAMPLE_DATA = '{"symbol": "EXPL", "historical": [{"open": 14.0,"close": 14.1,"low": 15.0,"high": 14.0,"date": ""}]}'

if __name__ == "__main__":
    pygame.init()
    my_font = pygame.font.SysFont('sans', 18)
    data = json.loads(SAMPLE_DATA)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        screen.fill(WHITE)
        draw_candlestick_chart(screen, data, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT), my_font)
    pygame.quit()

