import random
import time 
from src.player import Player
from src.board import Board

class Game:
    def __init__(self, b1):
        # self.player = p1
        # self.computer = p2
        self.board = b1
        
    def start_game(self):
        print(f"Welcome to the TicTacToe game. You will play against the computer\n")
        player1_name = input(f"Enter Player1 (using X symbol) name:")
        self.p1 = Player(player1_name)
        player2_name = input(f"Enter Player2 (using O symbol) name:")
        self.p2 = Player(player2_name)

        return self.board.display_plain_board()


    def start_rounds(self):
        while True: #Asks for another round to the player
            print(f"Use this guide to choose your move")
            self.board.display_index_guide()

            
            while self.board.check_winner() > 2: # Game loop to continue till someone (either the player or the computer) wins the game

                # For Player 1
                while True: #Keep trying unless player enters a valid value. In that case do break
                    try:
                        self.board.display_current_board()
                        # self.board.display_index_guide()
                        print(f"\n")
                        chosen_index = int(input(f"{self.p1.name} Choose your move from 1 to 9:"))    
                        if self.board.check_chosen_value(chosen_index):
                            self.board.update_board_player1(chosen_index)
                            break
                    except:
                        print(f"{self.p1.name} Please enter a valid integer from 1 to 9")
                        
                self.board.display_current_board()
    
                if self.board.check_winner() == 1 :
                    print(f"\n{self.p1.name} has won the game")
                    break
                # if self.board.check_winner() or len(self.board.already_chosen_indexes) == 9:
                #     if not self.board.check_winner() and len(self.board.already_chosen_indexes) == 9:
                #         print(f"It's a draw")
                #     break
    
                if self.board.check_winner() > 2 and len(self.board.already_chosen_indexes) == 9:
                    print(f"\nIt's a draw")
                    break
                
                
                # print(f"{self.p2.name} Please select your move from 1 to 9")
                # time.sleep(3)

                # For player 2
                while True: #Keep trying unless player enters a valid value. In that case do break
                    try:
                        # self.board.display_current_board()
                        # self.board.display_index_guide()
                        print(f"\n")
                        chosen_index = int(input(f"{self.p2.name} Choose your move from 1 to 9:"))    
                        if self.board.check_chosen_value(chosen_index):
                            self.board.update_board_player2(chosen_index)
                            break
                    except:
                        print(f"{self.p2.name} Please enter a valid integer from 1 to 9")
                        
                # self.board.display_current_board()

                if self.board.check_winner() == 2 :
                    print(f"\n{self.p2.name} has won the game")
                    break
    
                # if self.board.check_winner():
                #     break
            print(f"Game over!!\n")
            print(f"Would you like to play again?\n"
                 f"Press 1 to play another round\n"
                 f"Press 0 to exit the game\n")
    
            choice_after_round = input(f"Enter your choice (1 or 0):")
            if choice_after_round == '0':
                break
            else:
                self.board = Board()