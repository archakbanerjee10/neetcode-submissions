class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            left=0
            right=len(matrix[0])-1
            while left <= right:
                if target == matrix[i][(left+right)//2]:
                    return True
                elif(target>matrix[i][(left+right)//2]):
                    left=((left+right)//2)+1
                else:
                    right=((left+right)//2)-1
        return False


        