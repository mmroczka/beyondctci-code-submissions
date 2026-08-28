# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def tunnel_depth(tunnel_network):
  R = len(tunnel_network)
  C = len(tunnel_network[0])
  visited = set()
  max_depth = 0

  def dfs(row, col):

    def is_valid(row, col):
      return 0 <= row < R and 0 <= col < C and (row, col) not in visited and tunnel_network[row][col] == 1

    nonlocal max_depth
    visited.add((row, col))
    max_depth = max(max_depth, row)

    for next_row, next_col in [(row + 1, col), (row - 1, col),
                               (row, col + 1), (row, col - 1)]:
      if is_valid(next_row, next_col):
        dfs(next_row, next_col)

  dfs(0, 0)
  return max_depth
