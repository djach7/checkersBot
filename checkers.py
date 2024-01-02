import math
from typing import List, Dict

ROW_COUNT = 8 # num of rows on checkers board
COL_COUNT = 8 # num of columns on checkers board
UNUSED = 'x' # represent empty board spaces
RED = 'r'
YELLOW = 'y'
EMPTY = '*'
board_piece = {UNUSED: ':white_medium_square: ', RED: ':red_circle: ',
               YELLOW: ':yellow_circle: ', EMPTY: ':black_medium_square: '}

class Board:
    # board for checkers game
    _board: List[List[int]]
    _printedBoard = str

    # init a board, no unused spaces included, p1 red, p2 yellow
    def __init__(self) -> None:
        arr = []
        i = 1
        for row in range(8):
            arr.append([])
            for col in range(4):
                if row < 3: # if in yellow starting rows
                    if (row % 2) == 0:
                        arr[row].append(UNUSED)
                        arr[row].append(YELLOW)
                    else:
                        arr[row].append(YELLOW)
                        arr[row].append(UNUSED)
                if 2 < row < 5: # middle rows
                    if (row % 2) == 0:
                        arr[row].append(UNUSED)
                        arr[row].append(EMPTY)
                    else:
                        arr[row].append(EMPTY)
                        arr[row].append(UNUSED)
                if row > 4: # red starting rows
                    if (row % 2) == 0:
                        arr[row].append(UNUSED)
                        arr[row].append(RED)
                    else:
                        arr[row].append(RED)
                        arr[row].append(UNUSED)
                i += 1

        self._board = arr

    # print board, adding in unused spaces
    def print_board(self) -> str:
        p_board = self._board
        p_board_str = ''

        # iterate board, adding to str
        i = 0
        for row in p_board:
            for item in row:
                p_board_str += board_piece[item]
            p_board_str += '  '+ str(i) + '\n'
            i += 1
        for i in range(8):
            p_board_str += '  ' + str(i) + '   '

        self._printedBoard = p_board_str
        return p_board_str
    
    def red_move_no_jump(self, r: int, c: int, r2: int, c2: int):
        m_board = self._board
        # set prior location to empty space
        m_board[r][c] = EMPTY
        m_board[r2][c2] = RED

        print("in red move")

        self._board = m_board

    def yellow_move_no_jump(self, r: int, c: int, r2: int, c2: int):
        m_board = self._board
        # set prior location to empty space
        m_board[r][c] = EMPTY
        m_board[r2][c2] = YELLOW

        print("in yellow move")

        self._board = m_board

    def red_jump_move(self, r: int, c: int, r2: int, c2: int):
        m_board = self._board
        # set prior location to empty space
        m_board[r][c] = EMPTY
        # set location being jumped to empty space
        m_board[r2][c2] = EMPTY

        # landing row will always be 1 less than r2 
        r3 = r2 - 1
        # set landing column according to jump direction
        c3 = 0
        if c2 > c:
            c3 = c2 + 1
        else:
            c3 = c2 - 1
        
        m_board[r3][c3] = RED

        print("in red jump")

        self._board = m_board

    def yellow_jump_move(self, r: int, c: int, r2: int, c2: int):
        m_board = self._board
        # set prior location to empty space
        m_board[r][c] = EMPTY
        # set location being jumped to empty space
        m_board[r2][c2] = EMPTY

        # landing row will always be 1 more than r2 
        r3 = r2 + 1
        # set landing column according to jump direction
        c3 = 0
        if c2 > c:
            c3 = c2 + 1
        else:
            c3 = c2 - 1
        
        m_board[r3][c3] = YELLOW

        print("in yellow jump")

        self._board = m_board

    def cur_piece(self, r: int, c: int) -> str:
        cur_board = self._board
        cur_piece = cur_board[r][c]

        print(cur_piece)
        return cur_piece


    
    # def red_move_valid_no_jump(self, r: int, c: int, r2: int, c2: int):
    #     cur_pos = self._board[r][c] # current position
    #     p_move = self._board[r2][c2] # potential move position
    #     if r == 0: # at top of board
    #         return False
    #     else:
    #         if (r % 2) == 0: # if row is even
    #             if c == 3: # far right column
    #                 if p_



    


