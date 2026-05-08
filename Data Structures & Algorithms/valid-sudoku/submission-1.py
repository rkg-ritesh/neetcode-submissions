from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowEle=defaultdict(set)
        colEle=defaultdict(set)
        squareEle=defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                digit=board[i][j]

                if digit in rowEle[i] or digit in colEle[j] or digit in squareEle[(i//3,j//3)]:
                    return False
                rowEle[i].add(board[i][j])
                colEle[j].add(board[i][j])
                squareEle[(i//3,j//3)].add(board[i][j])
        return True

        