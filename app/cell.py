EMPTY = ' '

class Cell:
  def __init__(self, row, col):
    self.piece = EMPTY
    self.row = row
    self.col = col

  def is_empty(self):
    return self.piece == EMPTY
