# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def decode_a_string(s):
  count_stack = []  # Stack to store multipliers
  string_stack = []  # Stack to store substrings
  current_string = []  # Current substring being built
  k = 0  # Current multiplier

  for char in s:
    if char.isdigit():
      k = k * 10 + int(char)
    elif char == '{':
      count_stack.append(k)
      string_stack.append(current_string)
      current_string = []
      k = 0
    elif char == '}':
      multiplier = count_stack.pop()
      previous_string = string_stack.pop()
      current_string = previous_string + current_string * multiplier
    else:
      current_string.append(char)

  return "".join(current_string)
