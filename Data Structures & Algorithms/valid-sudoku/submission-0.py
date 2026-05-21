class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        ''' 
         1: check rows

         2: check columns

         3: check squares
                - get 'coordinates' of each square e.g. 0, 0 -> top left 2, 2 -> bottom right 
                - index of row // 3, index of col // 3 = coordinates of square
                - key = tuple(coords) value = set(seen nums)
        '''
        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue
                
                if ((board[r][c] in rows[r]) or 
                    (board[r][c] in cols[c]) or 
                    (board[r][c] in squares[r // 3, c // 3])
                    ):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r // 3, c // 3].add(board[r][c])
        return True