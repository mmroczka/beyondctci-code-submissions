# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def count_substrings_without_letter(s):
  sections = s.split('a')
  total = 0
  for section in sections:
    n = len(section)
    total += n * (n + 1) // 2
  return total
