class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix), len(matrix[0])
        low , high = 0, (n*m) - 1
        while low<= high:
            mid = (low+high)//2 #floor down
            value = matrix[mid//m][mid%m] #divide and modulo converting 1D to 2D
            if value == target:
                return True
            elif value < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


        