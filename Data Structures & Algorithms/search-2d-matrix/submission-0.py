class Solution:
    def binary_search(self, arr: List[int], x: int):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return mid
        return -1
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Search for correct column
        colstart = 0
        colend = len(matrix)-1
        colmid = None
        while colstart < colend:
            colmid = (colstart + colend)//2
            if target < matrix[colmid][0]:
                colend = colmid-1
            elif target > matrix[colmid][-1]:
                colstart = colmid+1
            else :
                colstart = colmid
                colend = colmid
        if colstart < 0 or colend >= len(matrix) or target < matrix[colstart][0] or target > matrix[colend][-1] :return False
        else :
            if self.binary_search(matrix[colstart], target) == -1:
                return False
            else: return True
        #Normal Binary once column is found
