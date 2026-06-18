# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def prefix_suffix_swap(arr):
  if len(arr) == 0:
    return

  n = len(arr)

  # Reverse the whole array
  l, r = 0, n - 1
  while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1

  # Reverse the last n/3 elements
  l, r = 2 * n // 3, n - 1
  while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1

  # Reverse the first 2n/3 elements
  l, r = 0, (2 * n // 3) - 1
  while l < r:
    arr[l], arr[r] = arr[r], arr[l]
    l += 1
    r -= 1
