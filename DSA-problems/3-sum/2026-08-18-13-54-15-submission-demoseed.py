# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def three_sum(arr, w):
  if len(arr) < 3:
    return False

  sorted_arr = sorted(arr)

  for i in range(len(sorted_arr) - 2):
    l = i + 1
    r = len(sorted_arr) - 1

    while l < r:
      current_sum = sorted_arr[i] + sorted_arr[l] + sorted_arr[r]
      if current_sum == w:
        return True
      elif current_sum < w:
        l += 1
      else:
        r -= 1

  return False