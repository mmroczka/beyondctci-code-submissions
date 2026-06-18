# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def count_subarrays_with_exactly_k_bad_days(sales, k):
  if k == 0:
    return count_at_most_k_bad_days(sales, 0)
  return count_at_most_k_bad_days(sales, k) - count_at_most_k_bad_days(sales, k - 1)

def count_at_most_k_bad_days(sales, k):
  l, r = 0, 0
  window_bad_days = 0
  count = 0
  while r < len(sales):
    can_grow = sales[r] >= 10 or window_bad_days < k
    if can_grow:
      if sales[r] < 10:
        window_bad_days += 1
      r += 1
      count += r - l
    else:
      if sales[l] < 10:
        window_bad_days -= 1
      l += 1
  return count