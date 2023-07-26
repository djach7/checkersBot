import math
from typing import List, Dict

ROW_COUNT = 8 # num of rows on checkers board
COL_COUNT = 8 # num of columns on checkers board
EMPTY = "*" # represent empty board spaces
board_piece = {EMPTY: ':white_medium_square: ', 'R': ':red_circle: ',
               'Y': ':yellow_circle: '}

class Board:
    # board for checkers game
    _board: List[List[str]]

    def __init__(self) -> None:
        key = 1
        arr = [[EMPTY * 8] for _ in range(8)]
        # iterate through adding numbered spaces
        for y in range(8):
            current = ''
            for x in range(0, 8, 2):
                str_key = str(key)
                if key < 10:
                    str_key = ' ' + str_key

                # if row is even
                if (y % 2) == 0:
                    current = current + EMPTY + ' ' + str_key + ' '
                else:
                    current = current + ' ' + str_key + ' ' + EMPTY

                current = current.rjust(2)

                key += 1
            arr[y][0] = current

        self._board = arr

    def print_board(self) -> str:
        msg = ''
        for row in self._board:
            row = (''.join(row))
            for item in row:
                try:
                    msg += board_piece[item]
                except KeyError:
                    msg += item
            msg += '\n'
        return msg
    