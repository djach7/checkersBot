import math
from typing import List, Dict

ROW_COUNT = 8 # num of rows on checkers board
COL_COUNT = 8 # num of columns on checkers board
UNUSED = '*' # represent empty board spaces
RED = 'r'
YELLOW = 'y'
board_piece = {UNUSED: ':white_medium_square: ', RED: ':red_circle: ',
               YELLOW: ':yellow_circle: '}

class Board:
    # board for checkers game
    #_board: List[List[str]]
    _board: List[List[int]]
    _printedBoard = str

    # def __init__(self) -> None:
    #     key = 1
    #     arr = [[EMPTY * 8] for _ in range(8)]
    #     # iterate through adding numbered spaces
    #     for y in range(8):
    #         current = ''
    #         for x in range(0, 8, 2):
    #             str_key = str(key)
    #             if key < 10:
    #                 str_key = ' ' + str_key

    #             # if row is even
    #             if (y % 2) == 0:
    #                 current = current + EMPTY + ' ' + str_key + ' '
    #             else:
    #                 current = current + ' ' + str_key + ' ' + EMPTY

    #             current = current.rjust(2)

    #             key += 1
    #         arr[y][0] = current

    #     self._board = arr

    # def print_board(self) -> str:
    #     msg = ''
    #     for row in self._board:
    #         row = (''.join(row))
    #         for item in row:
    #             try:
    #                 msg += board_piece[item]
    #             except KeyError:
    #                 msg += item
    #         msg += '\n'
    #     return msg

    def __init__(self) -> None:
        arr = []
        i = 1
        for row in range(8):
            arr.append([])
            for col in range(4): #not caring about blank spaces rn
                if row < 3: #if in yellow starting rows
                    arr[row].append(YELLOW)
                if 2 < row < 5: #middle rows
                    arr[row].append(str(i))
                if row > 4: #red starting rows
                    arr[row].append(RED)
                i += 1
        
        #print(arr)
        
        # arr = []
        # for x in range(33):
        #     if x < 12:
        #         arr.append(Y)
        #     elif 12 < x < 21:
        #         arr.append(str(x))
        #     elif x > 20:
        #         arr.append(R)

        self._board = arr


    def print_board(self) -> str:
        p_board = self._board
        #print(p_board)

        #add in blank spaces
        for row in range(0,len(p_board)):
            if (row % 2) == 0: #if row is even, remebering first row will be even
                for col in range(0,len(p_board[row])):
                    p_board[row].insert(col*2, UNUSED)
            else: #row is odd, blank should be second
                for col in range(1, (len(p_board[row]))):
                    p_board[row].insert(col*2, UNUSED)
                p_board[row].insert(1, UNUSED)
        
        #print(p_board)



        p_board_str = ''
        # p_board_str = (' '.join(p_board[0:8])) + '\n' + (' '.join(p_board[8:16])) + '\n' + (' '.join(p_board[16:24])) + '\n' + (' '.join(p_board[24:32])) + '\n' + (' '.join(p_board[32:40])) + '\n' + (' '.join(p_board[40:48])) + '\n' + (' '.join(p_board[48:56])) + '\n' + (' '.join(p_board[56:64]))

        for row in p_board:
            for item in row:
                try: #check if space isn't filled, aka an int
                    int(item)
                    num_str = ' ' + item + '  '
                    num_str = num_str.rjust(2)
                    p_board_str += num_str
                except ValueError:
                    p_board_str += board_piece[item]
            p_board_str += '\n'

        #print(p_board)
        self._printedBoard = p_board_str
        return p_board_str