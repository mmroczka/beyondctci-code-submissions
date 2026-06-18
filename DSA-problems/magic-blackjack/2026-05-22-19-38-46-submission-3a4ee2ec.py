# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def magic_blackjack():
  memo = {}
  
  def num_ways_rec(i):
    if i > 21:
      return 1
    if 16 <= i <= 21:
      return 0
    if i in memo:
      return memo[i]
    res = 0
    for card in range(1, 11):
      res += num_ways_rec(i + card)
    memo[i] = res
    return res

  return num_ways_rec(0)