# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def edge_list_to_adjacency_list(edges, V):
  adj_list = [[] for _ in range(V)]
  for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)
  return adj_list
