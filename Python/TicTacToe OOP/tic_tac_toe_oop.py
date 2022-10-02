## Tic tac toe game
## Practice with OOP in Python

class Game_Board:
    def __init__(self, board):
        self.board = board
    
    def letters_to_numbers():
        letters_to_numbers = {'A': 0,'B': 1,'C': 2}
        return letters_to_numbers
    
    def print_board(self):
        print("   A   B   C ")
        print(" +---+---+---+")
        row_number = 1
        for row in self.board:
            print("%d| %s |" % (row_number, " | ".join(row)))
            row_number += 1
        print(" +---+---+---+")

class Xs:
    def __init__(self, board):
        self.board = board

    def user_input(self):
        try:
            x_row = input("Player 1 please enter the row of the ship: ")
            while x_row not in '123':
                print("Not an appropriate choice, please selecet a valid row (1-3) !")
                x_row = input("Enter the row of the ship: ")

            y_column = input("Player 1 please enter the column of the ship: ").upper()
            while y_column not in 'ABC':
                print("Not an appropriate choice, please selecet a valid column (A-C)) !")
                y_column = input("Enter the column of the ship: ") 

            return int(x_row) - 1, Game_Board.letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid input") 
            return self.user_input()

class Os:
    def __init__(self, board):
        self.board = board

    def user_input(self):
        try:
            x_row = input("Player 2 please enter the row of the ship: ")
            while x_row not in '123':
                print("Not an appropriate choice, please selecet a valid row (1-3) !")
                x_row = input("Enter the row of the ship: ")

            y_column = input("Player 2 please enter the column of the ship: ").upper()
            while y_column not in 'ABC':
                print("Not an appropriate choice, please selecet a valid column (A-C)) !")
                y_column = input("Enter the column of the ship: ") 

            return int(x_row) - 1, Game_Board.letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid input") 
            return self.user_input()

def check_win(Game_Board):
    if Game_Board.board[0][0] == 'X' and Game_Board.board[0][1] == 'X' and Game_Board.board[0][2] == 'X':
        print("Player 1 has won !")
        return False
    if Game_Board.board[0][0] == 'O' and Game_Board.board[0][1] == 'O' and Game_Board.board[0][2] == 'O':
        print("Player 2 has won !")
        return False
    if Game_Board.board[1][0] == 'X' and Game_Board.board[1][1] == 'X' and Game_Board.board[1][2] == 'X':
        print("Player 1 has won !")
        return False
    if Game_Board.board[1][0] == 'O' and Game_Board.board[1][1] == 'O' and Game_Board.board[1][2] == 'O':
        print("Player 2 has won !")
        return False    
    if Game_Board.board[2][0] == 'X' and Game_Board.board[2][1] == 'X' and Game_Board.board[2][2] == 'X':
        print("Player 1 has won !")
        return False
    if Game_Board.board[2][0] == 'O' and Game_Board.board[2][1] == 'O' and Game_Board.board[2][2] == 'O':
        print("Player 2 has won !")
        return False
    if Game_Board.board[0][0] == 'X' and Game_Board.board[1][0] == 'X' and Game_Board.board[2][0] == 'X':
        print("Player 1 has won !")
        return False
    if Game_Board.board[0][0] == 'O' and Game_Board.board[1][0] == 'O' and Game_Board.board[2][0] == 'O':
        print("Player 2 has won !")
        return False
    if Game_Board.board[0][1] == 'X' and Game_Board.board[1][1] == 'X' and Game_Board.board[2][1] == 'X':
        print("Player 1 has won !")
        return False
    if Game_Board.board[0][1] == 'O' and Game_Board.board[1][1] == 'O' and Game_Board.board[2][1] == 'O':
        print("Player 2 has won !")
        return False
    if Game_Board.board[0][2] == 'X' and Game_Board.board[1][2] == 'X' and Game_Board.board[2][2] == 'X':
        print("Player 1 has won !")
        return False
    if Game_Board.board[0][2] == 'O' and Game_Board.board[1][2] == 'O' and Game_Board.board[2][2] == 'O':
        print("Player 2 has won !")
        return False
    if Game_Board.board[0][0] == 'X' and Game_Board.board[1][1] == 'X' and Game_Board.board[2][2] == 'X':
        print("Player 1 has won !")
        return False
    if Game_Board.board[0][0] == 'O' and Game_Board.board[1][1] == 'O' and Game_Board.board[2][2] == 'O':
        print("Player 2 has won !")
        return False
    if Game_Board.board[0][2] == 'X' and Game_Board.board[1][1] == 'X' and Game_Board.board[2][0] == 'X':
        print("Player 1 has won !")
        return False
    if Game_Board.board[0][2] == 'O' and Game_Board.board[1][0] == 'O' and Game_Board.board[2][0] == 'O':
        print("Player 2 has won !")
        return False        

def gameOn():
    main_board=Game_Board([[" "] * 3 for i in range(3)]) ## Create board 3x3
    game = True ## Start game
    while game: ## As long as not break
        p1x, p1y = Xs.user_input(object) ## Frist player input
        while main_board.board[p1x][p1y] == 'X' or main_board.board[p1x][p1y] == 'O':
            print("It's already taken !") ## If taken go back
            p1x, p1y = Xs.user_input(object)
        
        main_board.board[p1x][p1y] = 'X' # Place X
        main_board.print_board() ## Look at the board before second player

        if check_win(main_board) == False:  ## Win check
            main_board.print_board()
            break

        main_board.print_board()
        
        p2x, p2y = Os.user_input(object) ## Second player turn

        while main_board.board[p2x][p2y] == 'X' or main_board.board[p2x][p2y] == 'O': ## Check if taken
            print("It's already taken !")
            p2x, p2y = Os.user_input(object)
        
        main_board.board[p2x][p2y] = 'O' ## Place
        
        if check_win(main_board) == False: ## WIn check
            main_board.print_board()
            break

        main_board.print_board()

if __name__ == '__main__':
    gameOn()

