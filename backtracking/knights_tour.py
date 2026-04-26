from copy import deepcopy


def get_possible_positions(row, col, visited, n):
    op = []
    data = [(2, 1), (2, -1), (-2, +1), (-2, -1), (1,2), (-1, 2), (1,-2), (-1, -2)]
    for d in data:
        new_row = row+d[0]
        new_col = col+d[1]
        if new_row >= n or new_row < 0 or new_col >= n or new_col < 0:
            continue
        new_pos = new_row*n + new_col
        if new_pos in visited:
            continue
        op.append((new_row, new_col))
    return op

def knights_tour(grid):
    solution_board = [[-1]*n for _ in range(n)]
    compared = deepcopy(solution_board)
    visited_cells = set()
    def backtrack(row, col, position):
        current_pos = row*n+col
        visited_cells.add(current_pos)
        solution_board[row][col] = position
        if position == n*n-1:
            return True
        possible_positions = get_possible_positions(row, col, visited_cells, n)
        
        for each_possible_position in possible_positions:
            valid_pos = backtrack(each_possible_position[0], each_possible_position[1], position+1)
            if valid_pos:
                return True
        solution_board[row][col] = -1
        visited_cells.remove(current_pos)
        return False
    backtrack(0, 0, 0)
    if solution_board == compared:
        return [-1]
    else:
        return solution_board

n=4
print(knights_tour(n))