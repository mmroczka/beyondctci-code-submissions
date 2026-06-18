# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def split(s, c):
  if not s:
    return []

  res = []
  current = []
  i = 0
  while i < len(s):
    if s[i] == c:
      res.append(''.join(current))
      current = []
    else:
      current.append(s[i])
    i += 1
  res.append(''.join(current))
  return res
