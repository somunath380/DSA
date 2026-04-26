# https://leetcode.com/problems/rings-and-rods/

def countPoints(rings):
    idx_col_map = {i: set() for i in range(10)}
    n = len(rings)
    for i in range(0, n, 2):
        rod_no = int(rings[i+1])
        col = rings[i]
        idx_col_map[rod_no].add(col)
    count = 0
    for vals in idx_col_map.values():
        if vals and {'R', 'G', 'B'}.issubset(vals):
            count += 1
    return count
rings = "B0B6G0R6R0R6G9"
print(countPoints(rings))