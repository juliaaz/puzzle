'''
This module provides functions that deal with puzzle.
My github repository: https://github.com/juliaaz/puzzle
'''


def first_rule(board: list) -> bool:
    """
    Function checks whether the colored cells
    of each line contain numbers from 1 to 9 without repetition.
    Returns True if this rule of the game is followed.
    >>> first_rule(["**** ****","***1 ****","**  3****","* 4 1****",\
    "     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    True
    """
    uniqueness = True
    for row in board:
        square_seen = []
        for square in row:

            if square.isdigit() and square in square_seen:
                uniqueness = False
            square_seen.append(square)

    return uniqueness

# print(first_rule(["**** ****","***1 ****","**  3****","* 4 1****",\
#     "     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"]))


def second_rule(board: list) -> bool:
    """
    Function checks whether the colored cells
    of each column contain the numbers 1 to 9 without repetition.
    Returns True if this rule of the game is followed.
    >>> second_rule(["**** ****","***1 ****","**  3****","* 4 1****",\
    "     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    False
    """
    uniqueness = True
    board_len = len(board)
    for row in range(board_len):
        column_seen = []
        for column in range(board_len):
            cell = board[column][row]

            if cell.isdigit() and cell in column_seen:
                uniqueness = False
            column_seen.append(cell)

    return uniqueness
# print(second_rule(["**** ****","***1 ****","**  3****","* 4 1****",\
#     "     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"]))


def third_rule(board: list) -> bool:
    """
    Function checks whether each block of cells
    of the same color contain numbers from 1 to 9 without repetition.
    Returns True if this rule of the game is followed.
    >>> third_rule(["**** ****","***1 ****","**  3****","* 4 1****",\
    "     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    True
    """
    uniqueness = True
    for row in range(0, 5):
        digit_seen = []
        for column in range(4 - row, 9 - row):
            cell = board[column][row]
            # if (8 - row) != (row + column) and cell.isdigit():
            if cell.isdigit() and cell in digit_seen:
                uniqueness = False
            else:
                if cell in ('*', ' '):
                    continue
                else:
                    digit_seen.append(cell)

        for column in range(row + 1, row + 5):
            cell = board[8 - row][column]
            if cell.isdigit() and cell in digit_seen:
                uniqueness = False
            else:
                if cell in ('*', ' '):
                    continue
                else:
                    digit_seen.append(cell)

    return uniqueness


def validate_board(board: list) -> bool:
    """
    Function is used to set whether
    the puzzle board is ready to start the game.
    The function returns True if the puzzle board is ready to start the game.
    >>> validate_board(["**** ****","***1 ****","**  3****","* 4 1****",\
    "     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"])
    False
    """
    return first_rule(board) and second_rule(board) and third_rule(board)

# print(validate_board(["**** ****","***1 ****","**  3****","* 4 1****",\
#     "     9 5 "," 6  83  *","3   1  **","  8  2***","  2  ****"]))
