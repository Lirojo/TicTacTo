import random


# Funkcja do drukowania planszy
def create_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


# Funkcja sprawdzająca czy ktoś wygrał
def check_win(field, symbol):
    # Kombinacje wygrywające (wiersze, kolumny, przekątne)
    win = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # wiersze
               (0, 3, 6), (1, 4, 7), (2, 5, 8),  # kolumny
               (0, 4, 8), (2, 4, 6)]  # przekątne

    for combination in win:
        if field[combination[0]] == field[combination[1]] == field[combination[2]] == symbol:
            return True
    return False


# Funkcja sprawdzająca czy plansza jest pełna (remis)
def full_board(board):
    return ' ' not in board


# Funkcja obsługująca ruch człowieka
def move_user(board):
    while True:
        try:
            position = int(input("Wybierz pozycję (1-9): ")) - 1
            if board[position] == ' ':
                board[position] = 'X'
                break
            else:
                print("To miejsce jest już zajęte!")
        except (ValueError, IndexError):
            print("Nieprawidłowa pozycja! Wybierz liczbę od 1 do 9.")


# Funkcja obsługująca ruch komputera (losowy wybór wolnego pola)
def move_computer(board):
    free_position = [i for i, pole in enumerate(board) if pole == ' ']
    position = random.choice(free_position)
    board[position] = 'O'


# Główna funkcja gry
def game():
    # Pusta plansza (9 pól)
    board = [' ' for _ in range(9)]
    game_on = True
    current_player = "czlowiek"  # Człowiek zaczyna

    while game_on:
        create_board(board)

        if current_player == "czlowiek":
            move_user(board)
            if check_win(board, 'X'):
                create_board(board)
                print("Gratulacje, wygrałeś!")
                game_on = False
            current_player = "komputer"
        else:
            move_computer(board)
            if check_win(board, 'O'):
                create_board(board)
                print("Komputer wygrał!")
                game_on = False
            current_player = "czlowiek"

        if full_board(board) and game_on:
            create_board(board)
            print("Remis!")
            game_on = False


# Uruchomienie gry
if __name__ == "__main__":
    game()
