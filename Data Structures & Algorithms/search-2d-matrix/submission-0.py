class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = (len(matrix) * len(matrix[0])) - 1

        def convert_coord(value: int):
            y_cord = value // len(matrix[0])
            x_cord = value % len(matrix[0])

            return y_cord, x_cord

        while left <= right:
            mid = (right + left) // 2
            y_cord, x_cord = convert_coord(mid)

            if matrix[y_cord][x_cord] == target:
                return True
            elif matrix[y_cord][x_cord] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False