#write code for tic tac toe 
# create a 3*3 board
# take a input from player 1 and player 2 
#Check if the input is valid
#Check if the game is over 
#Check if the game is a draw 
#Check if the game is won 
#Print the board after each move
#print the winner or if it's a draw

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {turn % 2 + 1} ({player})'s turn.")
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
        except ValueError:
            print("Invalid input. Please enter numbers between 1 and 3.")
            continue

        if 0 <= row < 3 and 0 <= col < 3:
            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board, player):
                    print_board(board)
                    print(f"Player {turn % 2 + 1} ({player}) wins!")
                    break
                elif is_draw(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                turn += 1
            else:
                print("Cell already taken. Try again.")
        else:
            print("Invalid position. Try again.")

if __name__ == "__main__":
    main()

