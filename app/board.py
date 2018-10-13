from .cell import Cell

class Board:
  def __init__(self):
    self.dim = 3
    self.cells = self._generate_cells()

  def clear(self):
    self.cells = self._generate_cells()

  def set_piece(self, row, col, piece):
    self.cells[row][col].piece = piece

  def get_cell(self, row, col):
    return self.cells[row][col]

  def get_center(self):
    return self.get_cell(self.dim // 2, self.dim // 2)

  def is_cell_empty(self, row, col):
    return self.cells[row][col].is_empty()

  def is_full(self):
    for row in self.cells:
      for cell in row:
        if cell.is_empty():
          return False
    return True

  def paths(self):
    return self.rows() + self.cols() + self.diagonals()

  def rows(self):
    return self.cells

  def cols(self):
    return [[row[i] for row in self.cells] for i in range(len(self.cells[0]))]

  def diagonals(self):
    return [
      [self.cells[i][i] for i in range(self.dim)],
      [self.cells[self.dim-1-i][i] for i in range(self.dim)]
    ]

  def _generate_cells(self):
    cells = []
    for r in range(self.dim):
      row = []
      for c in range(self.dim):
        row.append(Cell(r, c))
      cells.append(row)
    return cells
