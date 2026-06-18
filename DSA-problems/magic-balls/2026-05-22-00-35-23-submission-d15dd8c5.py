# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def magic_balls(r, g, b):
  counts = []
  colors = []
  for count, color in [(r, 'R'), (g, 'G'), (b, 'B')]:
    if count > 0:
      counts.append(count)
      colors.append(color)

  # Case 1: All balls have same color
  if len(colors) == 1:
    return colors[0]

  # Case 2: Balls of every color
  if len(colors) == 3:
    return "RGB"

  # Case 3: Only two colors
  missing_color = 'RGB'.replace(colors[0], '').replace(colors[1], '')

  # Make counts[0] the larger count
  if counts[0] < counts[1]:
    counts[0], counts[1] = counts[1], counts[0]
    colors[0], colors[1] = colors[1], colors[0]

  if counts[1] == 1:
    if counts[0] == 1:
      return missing_color  # Case 3.a
    return missing_color + colors[1]  # Cases 3.c and 3.d
  return "RGB"  # Case 3.b