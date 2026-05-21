class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Brute Force
        for row in range(len(matrix)):
            for num in range(len(matrix[0])):
                if matrix[row][num] == target:
                    return True
        return False