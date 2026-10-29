class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefixsum=[[]]
            return 
        m,n=len(matrix),len(matrix[0])
        #initializing the prefix sum array with 0 as all the elements
        self.prefixsum=[[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                self.prefixsum[i+1][j+1]=(self.prefixsum[i][j+1] 
                                           + self.prefixsum[i+1][j] 
                                           - self.prefixsum[i][j] 
                                           + matrix[i][j])


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefixsum[row2+1][col2+1]-
        self.prefixsum[row2+1][col1]-
        self.prefixsum[row1][col2+1]
        +self.prefixsum[row1][col1])