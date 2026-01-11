import random
import time 
from src.player import Player
from src.board import Board

class Game:
    def __init__(self, p1, p2, b1):
        self.player = p1
        self.computer = p2
        self.board = b1

    def start_game(self):
        print(f"Welcome to the TicTacToe game. You will play against the computer\n")
        return self.board.display_plain_board()

    def start_rounds(self):
        while True: #Asks for another round to the player
            print(f"Use this guide to choose your move")
            self.board.display_index_guide()
            while not self.board.check_winner(): # Game loop to continue till someone (either the player or the computer) wins the game
                while True: #Keep trying unless player enters a valid value. In that case do break
                    try:
                        self.board.display_current_board()
                        # self.board.display_index_guide()
                        print(f"\n")
                        chosen_index = int(input(f"Choose your move from 1 to 9:"))    
                        if self.board.check_chosen_value(chosen_index):
                            self.board.update_board_player(chosen_index)
                            break
                    except:
                        print(f"Please enter a valid integer from 1 to 9")
                        
                self.board.display_current_board()
    
                if self.board.check_winner():
                    break
                # if self.board.check_winner() or len(self.board.already_chosen_indexes) == 9:
                #     if not self.board.check_winner() and len(self.board.already_chosen_indexes) == 9:
                #         print(f"It's a draw")
                #     break
    
                if not self.board.check_winner() and len(self.board.already_chosen_indexes) == 9:
                    print(f"It's a draw")
                    break
                
                
                print(f"Computer is thinking..")
                time.sleep(3)
                while True: #Keep trying until valid value is chosen by the computer
                    
                    comp_choice = random.randint(1, 9)
                    if self.board.check_chosen_value(comp_choice):    
                        self.board.update_board_computer(comp_choice)
                        print(f"\n")
                        break

    
    
                # if self.board.check_winner():
                #     break
            print(f"Game over!!\n")
            print(f"Would you like to play again?\n"
                 f"Press 1 to play another round\n"
                 f"Press 0 to exit the game\n")

            while True:
                choice_after_round = input(f"Enter your choice (1 or 0):")
                if choice_after_round == '0':
                    time.sleep(1)
                    print(f"Exiting game. Bye!!")
                    return
                elif choice_after_round == '1':
                    self.board = Board()
                    break
                else:
                    print(f"Invalid choice entered. Please choose 0 (Exit) or 1 (Play again)")