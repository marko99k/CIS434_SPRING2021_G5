import random
from tkinter import *


def coinToss():
    """Function to flip the coin and decide which user/AI goes first"""
    if random.randint(0, 1) == 0:
        # print ('AI') test
        return 'PC'
    else:
        return 'Player'
        # print ('Player') test


# Test
# for x in range(0, 10):
#    coinToss()


# adding board function
board_size = 500


def initialize_board(self):
    """Creating a board"""
    for i in range(2):
        self.canvas.create_line((i + 1) * board_size / 3, 0,
                                (i + 1) * board_size / 3, board_size)

    for i in range(2):
        self.canvas.create_line(0, (i + 1) * board_size / 3, board_size,
                                (i + 1) * board_size / 3)
