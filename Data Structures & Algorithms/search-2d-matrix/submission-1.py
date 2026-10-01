class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            m,n = len(matrix),len(matrix[0])
            def cord_to_idx(i,j):
                return i*n + j
            def idx_to_cord(i):
                return (i//n, i%n)
            l = 0
            r = m*n
            while l < r:
                middle = (l+r)//2
                mi,mj = idx_to_cord(middle)
                # print(l,r,middle,mi,mj)
                if matrix[mi][mj] == target:
                    return True
                elif matrix[mi][mj] < target:
                    l = middle+1
                else:
                    r = middle
            return False