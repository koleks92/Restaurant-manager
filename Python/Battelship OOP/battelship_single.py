import random

class Board_game:
    def __init__(self, board):
        self.board = board

    def letters_to_numbers():
        letters_to_numbers = {'A':0, 'B': 1, 'C': 2,'D': 3,'E': 4,'F': 5,'G' : 6, 'H' : 7}
        return letters_to_numbers
    
    def print_board(self):
        print("  A B C D E F G H ")
        print("  +-+-+-+-+-+-+-+")
        row_number=1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1

class Battleship:
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == 'X':
                self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] = 'X'
            return self.board

    def user_input(self):
        try:
            x_row = input("Enter the row of the ship: ")
            while x_row not in '12345678':
                print("Not an appropriate choice, please selecet a valid row (1-8) !")
                x_row = input("Enter the row of the ship: ")

            y_column = input("Enter the column of the ship: ").upper()
            while y_column not in 'ABCDEFGH':
                print("Not an appropriate choice, please selecet a valid column (A-H)) !")
                y_column = input("Enter the column of the ship: ") 

            return int(x_row) - 1, Board_game.letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid input") 
            return self.user_input()

    def count_hit_ships(self):
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == 'X':
                    hit_ships += 1
        return hit_ships   


def RunGame():
    computer_board = Board_game([[" "] * 8 for i in range(8)])
    user_guess_board = Board_game([[" "] * 8 for i in range(8)])

    turns=10
    while turns > 0:
        Board_game.print_board(user_guess_board)
        user_x_row, user_y_column = Battleship.user_input(object)

        while user_guess_board.board[user_x_row][user_y_column] == "-" or user_guess_board.board[user_x_row][user_y_column] == "X":
            print("You guessed that one already!")
            user_x_row, user_y_column = Battleship.user_input(object)
        
        if computer_board.board[user_x_row][user_y_column] == 'X':
            print("You sunk one of computer's battelships !")
            user_guess_board.board[user_x_row][user_y_column] = "X"
        else:
            print("You missed ! ")
            user_guess_board.board[user_x_row][user_y_column] = "-"
        
        if Battleship.count_hit_ships(user_guess_board) == 5:
            print("You hit all 5 battleships!")
            break
        else:
            turns -= 1
            print(f"You have {turns} turns remaning!")
            if turns == 0:
                print("Sorry, run out of turns!")
                Board_game.print_board(user_guess_board)
                break
    
if __name__ == '__main__':
    RunGame()


        
