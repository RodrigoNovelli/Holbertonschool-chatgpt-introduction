def print_board(board):
    """
    Imprime el tablero de Tic-Tac-Toe.
    
    Args:
        board (list of list of str): El tablero del juego.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Verifica si hay un ganador en el tablero de Tic-Tac-Toe.

    Args:
        board (list of list of str): El tablero del juego.
    
    Returns:
        bool: True si hay un ganador, False en caso contrario.
    """
    # Verifica filas
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Verifica columnas
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Verifica diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """
    Verifica si el tablero está lleno.

    Args:
        board (list of list of str): El tablero del juego.
    
    Returns:
        bool: True si el tablero está lleno, False en caso contrario.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Función principal para jugar al juego de Tic-Tac-Toe.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            
            if row not in range(3) or col not in range(3):
                print("Invalid row or column. Please enter 0, 1, or 2.")
                continue
            
            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board):
                    print_board(board)
                    print(f"Player {player} wins!")
                    break
                if is_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break
                # Cambia el turno
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    tic_tac_toe()
