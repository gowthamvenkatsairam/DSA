class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        check_row = [set() for _ in range(9)]
        check_col = [set() for _ in range(9)]
        check_grid = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    grid_id = (i//3) * 3 + (j//3)
                    check_row[i].add(board[i][j])
                    check_col[j].add(board[i][j])
                    check_grid[grid_id].add(board[i][j])
        def solve(row, col):
            if row == 9:
                return True
            if col == 9:
                return solve(row+1, 0)
            if board[row][col] != ".":
                return solve(row, col+1)
            grid_id = (row//3) * 3 + (col//3)
            for num in "123456789":
                if num in check_row[row] or num in check_col[col] or num in check_grid[grid_id]:
                    continue
                board[row][col] = num
                check_row[row].add(num)
                check_col[col].add(num)
                check_grid[grid_id].add(num)
                if solve(row, col + 1):
                    return True
                board[row][col] = "."
                check_row[row].remove(num)
                check_col[col].remove(num)
                check_grid[grid_id].remove(num)
            return False
        solve(0, 0)
                
                    


