class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_row = 0
        right_row = len(matrix) - 1

        while left_row <= right_row:
            mid_row = (left_row + right_row) // 2

            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                left = 0
                right = len(matrix[mid_row]) - 1

                while left <= right:
                    mid = (left + right) // 2

                    if matrix[mid_row][mid] == target:
                        return True
                    elif matrix[mid_row][mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
                
                return False

            elif matrix[mid_row][0] > target:
                right_row = mid_row - 1
            elif matrix[mid_row][-1] < target:
                left_row = mid_row + 1

        return False
        
