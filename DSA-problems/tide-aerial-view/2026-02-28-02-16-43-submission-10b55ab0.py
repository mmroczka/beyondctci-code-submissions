# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def tide_aerial_view(pictures):
    def count_water(i):
        picture = pictures[i]
        total_water = 0
        for r in range(len(picture)):
            for c in range(len(picture[0])):
                if picture[r][c] == 1:
                    total_water += 1
        return total_water

    def is_before(i):
        total_pixels = len(pictures[i]) * len(pictures[i][0])
        return count_water(i) / total_pixels < 0.5

    l, r = 0, len(pictures) - 1

    if is_before(r):
        return r
    if not is_before(l):
        return l

    while r - l > 1:
        mid = (l + r) // 2
        if is_before(mid):
            l = mid
        else:
            r = mid

    total_pixels = len(pictures[0]) * len(pictures[0][0])
    l_diff = abs(2 * count_water(l) - total_pixels)
    r_diff = abs(2 * count_water(r) - total_pixels)
    if l_diff <= r_diff:
        return l
    else:
        return r