from .player import Player
from .move import Move

class Human(Player):
  def __init__(self, piece):
    super().__init__(piece)

  def get_move(self, board):
    def is_move_valid(move):
        if not len(move) == 3:
          return False
        row, _, col = move
        try:
          row, col = int(row), int(col)
          return (
            0 <= row < board.dim and
            0 <= col < board.dim and
            board.is_cell_empty(row, col)
          )
        except ValueError:
          return False

    move = input('Player '+self.piece+' please choose your move: ')
    while not is_move_valid(move):
      move = input(move+' is not a valid move. Please enter another move: ')

    row, _, col = move
    return Move(int(row), int(col))
