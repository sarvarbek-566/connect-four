def create_board():
    board = []
    for _ in range(6):
        row = [' '] * 7
        board.append(row)
    return board


def print_board(board):
    for row in board:
        print('|', end='')
        for cell in row:
            print(cell, end='|')
        print()
        print('_' * 15)


def is_valid_move(board, col): 
    if col < 0 or col >= 7:
        return False
    return board[0][col] == ' '


def make_move(board, col, player):
    for row in range(5, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            return True
    return False


def check_winner(board, player):
    for row in range(6):
        for col in range(4):
            if board[row][col] == player and \
               board[row][col+1] == player and \
               board[row][col+2] == player and \
               board[row][col+3] == player:
                return True
                   
    for row in range(3):
        for col in range(7):
            if board[row][col] == player and \
               board[row+1][col] == player and \
               board[row+2][col] == player and \
               board[row+3][col] == player:
                return True

    for row in range(3):
        for col in range(4):
            if board[row][col] == player and \
               board[row+1][col+1] == player and \
               board[row+2][col+2] == player and \
               board[row+3][col+3] == player:
                return True

    for row in range(3):
        for col in range(3, 7):
            if board[row][col] == player and \
               board[row+1][col-1] == player and \
               board[row+2][col-2] == player and \
               board[row+3][col-3] == player:
                return True

    return False


def play_game():
    board = create_board()
    current_player = 'X'

    while True:
        print_board(board)

        try:
            col = int(input(f'Player {current_player}, enter a column number (0-6): '))
        except ValueError:
            print("Faqat 0–6 orasidagi raqam kiriting!")
            continue

        if is_valid_move(board, col):
            if make_move(board, col, current_player):
                if check_winner(board, current_player):
                    print_board(board)
                    print(f'Player {current_player} Wins!!!')
                    break
                elif ' ' not in board[0]:
                    print_board(board)
                    print("It's a tie!")
                    break
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Bu ustun tola. Boshqasini tanla.")
        else:
            print("Notogri ustun tanlandi. Qaytadan urinib koring.")


play_game()


