# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def most_ones_with_k_flips(arr, k):
  l, r = 0, 0
  window_zeros = 0
  cur_best = 0
  while r < len(arr):
    can_grow = window_zeros < k or arr[r] == 1
    if can_grow:
      window_zeros += 1 if arr[r] == 0 else 0
      r += 1
      cur_best = max(cur_best, r - l)
    elif l == r:
      l += 1
      r += 1
    else:
      window_zeros -= 1 if arr[l] == 0 else 0
      l += 1
  return cur_best
