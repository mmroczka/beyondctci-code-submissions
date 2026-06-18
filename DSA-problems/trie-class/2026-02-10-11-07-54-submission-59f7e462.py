# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class Node:
  def __init__(self):
    self.children = {}
    self.end = False

class Trie:
  def __init__(self):
    self.root = Node()

  def insert(self, s):
    curr = self.root
    for char in s:
      if char not in curr.children:
        curr.children[char] = Node()
      curr = curr.children[char]
    curr.end = True

  def contains(self, s):
    curr = self.root
    for char in s:
      if char not in curr.children:
        return False
      curr = curr.children[char]
    return curr.end

  def remove(self, s):

    def remove_rec(node, i):
      if i == len(s):
        if node.end:
          node.end = False
          return len(node.children) == 0
        return False

      if s[i] not in node.children:
        return False

      should_delete = remove_rec(node.children[s[i]], i + 1)
      if should_delete:
        del node.children[s[i]]
        return not node.end and len(node.children) == 0
      return False

    remove_rec(self.root, 0)