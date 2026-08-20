class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        js=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    js.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if 0 in matrix[i]:
                    matrix[i][j]=0 
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j in js:
                    matrix[i][j]=0       
        
