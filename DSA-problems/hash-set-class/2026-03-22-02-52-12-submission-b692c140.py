# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
class HashSet:
  def __init__(self, h):
    self.h = h
    self.capacity = 10
    self._size = 0
    self.buckets = [[] for _ in range(self.capacity)]

  def size(self):
    return self._size

  def contains(self, x):
    hash = self.h(x, self.capacity)
    for elem in self.buckets[hash]:
      if elem == x:
        return True
    return False

  def add(self, x):
    hash = self.h(x, self.capacity)
    for elem in self.buckets[hash]:
      if elem == x:
        return
    self.buckets[hash].append(x)
    self._size += 1
    load_factor = self._size / self.capacity
    if load_factor > 1:
      self.resize(self.capacity * 2)

  def resize(self, new_capacity):
    new_buckets = [[] for _ in range(new_capacity)]
    for bucket in self.buckets:
      for elem in bucket:
        hash = self.h(elem, new_capacity)
        new_buckets[hash].append(elem)
    self.buckets = new_buckets
    self.capacity = new_capacity

  def remove(self, x):
    hash = self.h(x, self.capacity)
    for i, elem in enumerate(self.buckets[hash]):
      if elem == x:
        self.buckets[hash].pop(i)
        self._size -= 1
        load_factor = self._size / self.capacity
        if load_factor < 0.25 and self.capacity > 10:
          self.resize(self.capacity // 2)