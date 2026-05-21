class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # we need to check rows, cols, and 'squares'
        # squares are 3x3 in size
        
        # we need to check each square, but how do we denote which square is which?
        # use a dict, with a tuple (x, y) as the key 
        # where 'x' is the x axis square number, and y is the y axis square number
        # how do we get the square coordinate?
        # looping through rows, perform i // 3 = x, loop through cols, perform i // 3 = y
        # then add the numbers for key to its value and check for membership

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                elif (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r // 3, c // 3]):
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[r // 3, c // 3].add(board[r][c])
        return True

