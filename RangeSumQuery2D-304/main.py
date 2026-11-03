class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        self.x = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j > 0:
                    self.x[i][j] = matrix[i][j] + self.x[i][j - 1]
                else:
                    self.x[i][j] = matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2 + 1):
            if col1 > 0:
                sum += self.x[i][col2] - self.x[i][col1 - 1]
            else:
                sum += self.x[i][col2]
        return sum
