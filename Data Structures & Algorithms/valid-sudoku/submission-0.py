class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                # print(i,j)
                found = set()
                for si in range(3):
                    for sj in range(3):
                        # print(found)
                        if board[si+i][sj+j] in found:
                            return False
                        if board[si+i][sj+j] !='.':
                            found.add(board[si+i][sj+j])
        # print("block pass")
        for row in board:
            found = set()
            print(found)
            for i in range(len(row)):
                if row[i] in found:
                    # print(row[i], found)
                    return False
                if row[i] !='.':
                    found.add(row[i])
        # print("row pass")
        for j in range(len(board)):
            found = set()
            for i in range(len(board)):
                if board[i][j] in found:
                    return False
                if board[i][j] !='.':
                    found.add(board[i][j])
        # print("col pass")
        return True