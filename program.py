import random


def generate_mines(size, num_mines):
    # Создаем пустое поле
    board = [['0' for _ in range(size)] for _ in range(size)]

    # Размещаем мины
    mines_placed = 0
    while mines_placed < num_mines:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)

        # Проверяем, не стоит ли уже мина в этой клетке
        if board[row][col] != '*':
            board[row][col] = '*'
            mines_placed += 1

    return board


def display_board(board):
    for row in board:
        print(' '.join(row))


# Пример использования функции
size = 5  # Размер поля
num_mines = 5  # Количество мин
board = generate_mines(size, num_mines)
display_board(board)
