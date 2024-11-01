import random


def generate_mines(size, num_mines):
    board = [['0' for _ in range(size)] for _ in range(size)]

    mines_placed = 0
    while mines_placed < num_mines:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)


        if board[row][col] != '*':
            board[row][col] = '*'
            mines_placed += 1

    return board


def display_board(board):
    for row in board:
        print(' '.join(row))



size = 5
num_mines = 5
board = generate_mines(size, num_mines)
display_board(board)
