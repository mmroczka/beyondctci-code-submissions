# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def dutch_flag_problem(arr):
  # Count occurrences of each color
  r_count = sum(1 for c in arr if c == 'R')
  w_count = sum(1 for c in arr if c == 'W')

  # Rewrite array with the right number of each color
  i = 0
  for _ in range(r_count):
    arr[i] = 'R'
    i += 1
  for _ in range(w_count):
    arr[i] = 'W'
    i += 1
  while i < len(arr):
    arr[i] = 'B'
    i += 1
