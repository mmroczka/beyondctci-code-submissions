# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict,deque
def most_protected_node(root):
  if not root:
    return 0

  # Map from node to its current minimum protection level
  protection = defaultdict(lambda: math.inf)
  nodes_per_level = defaultdict(int)
  node_to_index_in_level = {}

  # First pass: BFS to get depth and position in level
  Q = deque([(root, 0)])
  while Q:
    node, depth = Q.popleft()
    if not node:
      continue

    # Add node to its level
    nodes_per_level[depth] += 1
    # Store node's position in its level
    node_to_index_in_level[node] = nodes_per_level[depth] - 1

    # Update protection with min of ancestor count (depth) and left count
    protection[node] = min(depth, node_to_index_in_level[node])

    Q.append((node.left, depth + 1))
    Q.append((node.right, depth + 1))

  # Second pass: DFS to get descendant heights
  # Passes current depth down the tree.
  # Passes subtree height up the tree.
  # Updates protection level of nodes in global map.
  def dfs(node, depth):
    if not node:
      return -1
    height = 1 + max(dfs(node.left, depth + 1),
                     dfs(node.right, depth + 1))

    protection[node] = min(protection[node], height)

    # Update protection with right counts
    protection[node] = min(
        protection[node], nodes_per_level[depth] - node_to_index_in_level[node] - 1)

    return height

  dfs(root, 0)

  # Return highest protection level
  return max(protection.values())