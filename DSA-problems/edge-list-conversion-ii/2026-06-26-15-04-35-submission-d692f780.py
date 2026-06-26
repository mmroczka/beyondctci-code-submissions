# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def edge_list_to_adjacency_matrix(edges, V):
  matrix = [[0] * V for _ in range(V)]
  for u, v in edges:
    matrix[u][v] = 1
    matrix[v][u] = 1
  return matrix
