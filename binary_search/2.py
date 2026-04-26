# 1351. Count Negative Numbers in a Sorted Matrix https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

def countNegatives(self, grid) -> int:
        m = len(grid) # rows
        n = len(grid[0]) # cols
        row = m-1
        col = 0
        total_neg_nums = 0
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                total_neg_nums += (n - col)
                row -= 1
            else:
                col += 1
        return total_neg_nums

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))
