from .player import Player
from .move import Move
from time import sleep
from random import choice

class Computer(Player):
  def __init__(self, piece):
    super().__init__(piece)

  def get_move(self, board):
    print('Player '+self.piece+' is thinking...')
    sleep(1)
    move = self.apply_strategies([
      self.find_winning_move,
      self.find_prevent_winning_move,
      self.find_two_in_a_path_move,
      self.find_empty_cell_move
    ], board)
    return move

  def apply_strategies(self, strategies, board):
    move = None
    for strategy in strategies:
      move = strategy(board)
      if move: break
    return move

  def find_winning_move(self, board):
    for path in board.paths():
      empty, own, _ = self.partition_cells(path)
      if len(own) == 2 and len(empty) == 1:
        return self.to_move(empty[0])
    return None

  def find_prevent_winning_move(self, board):
    for path in board.paths():
      empty, _, opponent = self.partition_cells(path)
      if len(opponent) == 2 and len(empty) == 1:
        return self.to_move(empty[0])
    return None

  def find_two_in_a_path_move(self, board):
    for path in board.paths():
      empty, own, _ = self.partition_cells(path)
      if len(empty) == 2 and len(own) == 1:
        return self.to_move(empty[0])
    return None

  def find_empty_cell_move(self, board):
    center = board.get_center()
    if center.is_empty():
      return self.to_move(center)

    empty = []
    for row in board.rows():
      for cell in row:
        if cell.is_empty():
          empty.append(cell)
    return self.to_move(choice(empty))

  def partition_cells(self, cells):
    empty, own, opponent = [], [], []
    for cell in cells:
      if cell.is_empty():
        empty.append(cell)
      elif cell.piece == self.piece:
        own.append(cell)
      else:
        opponent.append(cell)
    return [ empty, own, opponent ]

  def to_move(self, cell):
    return Move(cell.row, cell.col)
