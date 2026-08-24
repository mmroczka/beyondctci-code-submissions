# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def search_in_sorted_array(arr, target):
  if not arr:
    return -1

  def is_before(i):
    return arr[i] < target

  # Handle edge cases to ensure l is in the before region
  # and r is in the after region
  l, r = 0, len(arr) - 1
  if not is_before(l):
    if arr[l] == target:
      return l
    return -1
  if is_before(r):
    return -1

  # Main binary search loop
  while r - l > 1:
    mid = (l + r) // 2
    if is_before(mid):
      l = mid
    else:
      r = mid

  if arr[r] == target:
    return r
  return -1
