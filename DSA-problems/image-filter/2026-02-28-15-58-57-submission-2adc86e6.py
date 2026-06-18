# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def image_filter(img):
  if not img or not img[0]:
    return img

  rows, cols = len(img), len(img[0])
  result = [[0] * cols for _ in range(rows)]

  # Directions for all 8 neighbors plus center
  directions = [
      [-1, -1], [-1, 0], [-1, 1],
      [0, -1], [0, 0], [0, 1],
      [1, -1], [1, 0], [1, 1]
  ]

  def is_valid(r, c):
    return 0 <= r < rows and 0 <= c < cols

  for r in range(rows):
    for c in range(cols):
      total = 0
      count = 0
      for dr, dc in directions:
        new_r, new_c = r + dr, c + dc
        if is_valid(new_r, new_c):
          total += img[new_r][new_c]
          count += 1
      result[r][c] = total // count

  return result