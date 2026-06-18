# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class Matrix:
  def __init__(self, grid):
    self.matrix = [row.copy() for row in grid]

  def transpose(self):
    matrix = self.matrix
    for r in range(len(matrix)):
      for c in range(r):
        matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

  def reflect_horizontally(self):
    self.matrix.reverse()

  def reflect_vertically(self):
    for row in self.matrix:
      row.reverse()

  def rotate_clockwise(self):
    self.transpose()
    self.reflect_vertically()

  def rotate_counterclockwise(self):
    self.transpose()
    self.reflect_horizontally()