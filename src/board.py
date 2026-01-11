from src.player import Player

class Board:
    def __init__(self):
        self.plain_board_values = ['| |' for i in range(9)]
        self.current_board_values = ['| |' for i in range(9)]
        self.already_chosen_indexes = []
        self.player_indexes = []
        self.computer_indexes = []

    def display_plain_board(self):
        print(f"{self.plain_board_values[0]} {self.plain_board_values[1]} {self.plain_board_values[2]}\n"
              f"\n"
              f"{self.plain_board_values[3]} {self.plain_board_values[4]} {self.plain_board_values[5]}\n"
              f"\n"
              f"{self.plain_board_values[6]} {self.plain_board_values[7]} {self.plain_board_values[8]}")

    def display_index_guide(self):
        print(f"|1| |2| |3|\n"
              f"\n"
              f"|4| |5| |6|\n"
              f"\n"
              f"|7| |8| |9|\n")

    def update_board_player(self, update_value_index):
        self.current_board_values[update_value_index-1] = '|X|'
        self.already_chosen_indexes.append(update_value_index)
        self.player_indexes.append(update_value_index)
        

    def check_chosen_value(self, update_value_index):
        if len(self.already_chosen_indexes)%2 == 0: #It is player's turn
            if update_value_index in self.already_chosen_indexes:
                print(f"This value is already taken. Please enter a different value which is not taken already!!") 
            elif isinstance(update_value_index, int) == False:
                print(f"Please enter an integer")
            elif update_value_index >= 1 and update_value_index <= 9:
                return True
        else: #It is computer's turn
            if update_value_index in self.already_chosen_indexes:
                return False
            elif isinstance(update_value_index, int) == False:
                return False
            elif update_value_index >= 1 and update_value_index <= 9:
                return True

    def update_board_computer(self, update_value_index):
        self.current_board_values[update_value_index-1] = '|O|'
        self.already_chosen_indexes.append(update_value_index)
        self.computer_indexes.append(update_value_index)
        
    def display_current_board(self):
        print(f"{self.current_board_values[0]} {self.current_board_values[1]} {self.current_board_values[2]}\n"
              f"\n"
              f"{self.current_board_values[3]} {self.current_board_values[4]} {self.current_board_values[5]}\n"
              f"\n"
              f"{self.current_board_values[6]} {self.current_board_values[7]} {self.current_board_values[8]}")

    def check_winner(self):
        a = set(self.player_indexes)
        b = set(self.computer_indexes)
        if ({1, 2, 3}.issubset(a) or {4, 5, 6}.issubset(a) or {7, 8, 9}.issubset(a) or {1, 4, 7}.issubset(a) 
            or {2, 5, 8}.issubset(a) or {3, 6, 9}.issubset(a) or {1, 5, 9}.issubset(a) or {3, 5, 7}.issubset(a)):
            print(f"\nYou have won the game!!")
            # self.display_current_board()
            return True
        
        elif ({1, 2, 3}.issubset(b) or {4, 5, 6}.issubset(b) 
        or {7, 8, 9}.issubset(b) or {1, 4, 7}.issubset(b) 
        or {2, 5, 8}.issubset(b) or {3, 6, 9}.issubset(b) 
        or {1, 5, 9}.issubset(b) or {3, 5, 7}.issubset(b)):
            print(f"\nComputer has won the game")
            self.display_current_board()
            return True

        else:
            return False