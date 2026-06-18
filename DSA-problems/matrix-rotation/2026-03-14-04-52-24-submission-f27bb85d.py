# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def matrix_rotation(mat):
  n = len(mat)
  for r in range(n // 2):
    for c in range((n + 1) // 2):
      # 4-way swap
      temp = mat[r][c]
      mat[r][c] = mat[n - c - 1][r]
      mat[n - c - 1][r] = mat[n - r - 1][n - c - 1]
      mat[n - r - 1][n - c - 1] = mat[c][n - r - 1]
      mat[c][n - r - 1] = temp