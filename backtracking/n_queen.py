def my_n_queen(n):
    path = []
    solutions = []
    diag_1 = set()
    diag_2 = set()
    used_cols = set()
    def backtrack(row: int):
        if row == n:
            # base case
            solutions.append(path[:])
            return
        for col in range(n):
            if col in used_cols or (row-col) in diag_1 or (row+col) in diag_2:
                continue
            
            #making choice
            path.append(col)
            diag_1.add(row-col)
            diag_2.add(row+col)
            used_cols.add(col)

            backtrack(row+1)

            #undo choice
            path.pop()
            diag_1.remove(row-col)
            diag_2.remove(row+col)
            used_cols.remove(col)

    backtrack(0)
    def make_board():
        op = []
        for each_solution in solutions:
            rows = []
            for each_pos in each_solution:
                temp = ['.']*n
                temp[each_pos] = 'Q'
                rows.append(''.join(temp))
            op.append(rows)
        return op
    return make_board()

def n_queens(n):
    path = []
    solutions = []
    used_cols = set()
    used_diag1 = set()  # r - c
    used_diag2 = set()  # r + c
    def backtrack(r: int):
        if r == n:
            # base case
            solutions.append(path[:])
            return
        for col in range(n):
            if col in used_cols or (r-col) in used_diag1 or (r+col) in used_diag2:
                continue
            
            #making choice
            path.append(col)
            used_cols.add(col)
            used_diag1.add(r-col)
            used_diag2.add(r+col)

            backtrack(r+1)

            #undo choice
            path.pop()
            used_cols.remove(col)
            used_diag1.remove(r-col)
            used_diag2.remove(r+col)

    backtrack(0)
    return solutions

n=1
print(my_n_queen(n))