class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # flip 
        n = len(matrix)
        for i in range(n//2):
            matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]
        print(matrix)
        for l in range(n):
            for j in range(l):
                print(l,j)
                matrix[l][j], matrix[j][l] = matrix[j][l], matrix[l][j]
