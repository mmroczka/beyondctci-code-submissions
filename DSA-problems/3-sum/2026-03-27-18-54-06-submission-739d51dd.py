# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def three_sum(arr, w):
  # Build value to indices map
  val_to_indices = {}
  for i, x in enumerate(arr):
    if x not in val_to_indices:
      val_to_indices[x] = []
    val_to_indices[x].append(i)

  # Try all pairs i,j and look for k
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      target = w - arr[i] - arr[j]
      if target in val_to_indices:
        # Check if we can use an index different from i,j
        for k in val_to_indices[target]:
          if k > j:  # Ensures k > j > i
            return True
  return False