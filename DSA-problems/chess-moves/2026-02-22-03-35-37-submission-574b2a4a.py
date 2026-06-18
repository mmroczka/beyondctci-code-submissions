# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def chess_moves(board, piece, r, c):
  def is_valid(board, r, c):
    return 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] != 1

  moves = []
  king_directions = [
      [-1, 0], [1, 0], [0, -1], [0, 1],  # Vertical and horizontal
      [-1, -1], [-1, 1], [1, -1], [1, 1]  # Diagonals
  ]
  knight_directions = [[-2, 1], [-1, 2], [1, 2], [2, 1],
                       [2, -1], [1, -2], [-1, -2], [-2, -1]]

  if piece == "knight":
    directions = knight_directions
  else:
    directions = king_directions

  for dir_r, dir_c in directions:
    new_r, new_c = r + dir_r, c + dir_c
    if piece == "queen":
      while is_valid(board, new_r, new_c):
        moves.append([new_r, new_c])
        new_r += dir_r
        new_c += dir_c
    elif is_valid(board, new_r, new_c):
      moves.append([new_r, new_c])
  return moves
