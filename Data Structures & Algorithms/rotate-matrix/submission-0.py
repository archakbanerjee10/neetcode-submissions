class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        n=len(matrix)

        #we are only gonna traverse throught the upper triangular matrix to avoid double swap
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        # after doing so our matrix has been transposed and now we just need to reverse the rows of the matrix

        for i in range(n):
            matrix[i].reverse()




        