from src.player import Player
from src.board import Board
from src.game import Game


def main():
    
    b1 = Board()
    g1 = Game(b1)
    g1.start_game()
    g1.start_rounds()


if __name__ == "__main__":
    main()
