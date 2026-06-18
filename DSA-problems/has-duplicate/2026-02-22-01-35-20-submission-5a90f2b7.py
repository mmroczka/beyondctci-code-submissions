# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def has_duplicate(arr):
  seen = set()
  for num in arr:
    if num in seen:
      return True
    seen.add(num)
  return False