from .board import Board
from .human import Human
from .computer import Computer
from random import random

class Game:
  def __init__(self):
    self.board = Board()
    self.piece1 = 'X'
    self.piece2 = 'O'
    self.players = self.setup_players()
    self.move_count = 0

  def play(self):
    winner = None
    while not winner and not self.board.is_full():
      self.display_board()
      move = self.cur_player().get_move(self.board)
      self.board.set_piece(move.row, move.col, self.cur_player().piece)
      self.move_count += 1
      winner = self.get_winner()

    self.display_board()
    if winner:
      print('Player '+winner+' wins!')
    else:
      print("It's a tie!")

    restart = input('Play again? (Y/n): ')
    should_restart = restart == 'Y' or restart == 'y'
    if should_restart:
      self.reset()
      self.play()

  def display_board(self):
    print('-------')
    for row in self.board.rows():
      print('|'+'|'.join(map(lambda cell: cell.piece, row))+'|')
      print('-------')

  def cur_player(self):
    return self.players[self.move_count % 2]

  def get_winner(self):
    for path in self.board.paths():
      first_cell = path[0]
      if first_cell.is_empty():
        continue

      all_same = True
      for cell in path:
        if cell.piece != first_cell.piece:
          all_same = False
          break
      if all_same:
        return first_cell.piece
    return None

  def reset(self):
    self.board.clear()
    self.move_count = 0

  def setup_players(self):
    if random() < 0.5:
      return [ Human(self.piece1), Computer(self.piece2) ]
    else:
      return [ Computer(self.piece1), Human(self.piece2) ]
