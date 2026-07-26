# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
# Available at runtime:
#
# class DynamicArray:
#   def __init__(self):
#     self.capacity = 10
#     self._size = 0
#     self.fixed_array = [None] * self.capacity
#
#   def get(self, i):
#     if i < 0 or i >= self._size:
#       raise IndexError('Index out of bounds')
#     return self.fixed_array[i]
#
#   def set(self, i, x):
#     if i < 0 or i >= self._size:
#       raise IndexError('Index out of bounds')
#     self.fixed_array[i] = x
#
#   def size(self):
#     return self._size
#
#   def append(self, x):
#     if self._size == self.capacity:
#       self._resize(self.capacity * 2)
#     self.fixed_array[self._size] = x
#     self._size += 1
#
#   def _resize(self, new_capacity):
#     new_fixed_size_arr = [None] * (new_capacity)
#     for i in range(self._size):
#       new_fixed_size_arr[i] = self.fixed_array[i]
#     self.fixed_array = new_fixed_size_arr
#     self.capacity = new_capacity
#
#   def pop_back(self):
#     if self._size == 0:
#       raise IndexError('Pop from empty array')
#     self._size -= 1
#     if self._size / self.capacity < 0.25 and self.capacity > 10:
#       self._resize(self.capacity//2)
#


class DynamicArrayExtras(DynamicArray):
  def pop(self, i):
    if i < 0 or i >= self._size:
      raise IndexError('Index out of bounds')

    x = self.fixed_array[i]

    for j in range(i, self._size - 1):
      self.fixed_array[j] = self.fixed_array[j + 1]

    self._size -= 1
    if self._size / self.capacity < 0.25 and self.capacity > 10:
      self.resize(self.capacity // 2)
    return x

  def contains(self, x):
    for i in range(self._size):
      if self.fixed_array[i] == x:
        return True
    return False

  def insert(self, i, x):
    if i < 0 or i > self._size:
      raise IndexError('Index out of bounds')

    if self._size == self.capacity:
      self.resize(self.capacity * 2)

    for j in range(self._size - 1, i - 1, -1):
      self.fixed_array[j + 1] = self.fixed_array[j]

    self.fixed_array[i] = x
    self._size += 1

  def remove(self, x):
    for i in range(self._size):
      if self.fixed_array[i] == x:
        self.pop(i)
        return i
    return -1
