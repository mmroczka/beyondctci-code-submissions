# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def tiling_floor(n):
  memo = dict()

  def tilings_rec(i):
    if i <= 1:
      return 1
    if i in memo:
      return memo[i]
    memo[i] = tilings_rec(i - 1) + tilings_rec(i - 2)
    return memo[i]

  return tilings_rec(n)