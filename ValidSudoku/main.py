class Solution:
    def sudoku(self, board:List[List[str]])->bool:
        res=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]!="."
                    res.extend([(i,board[i][j]),(board[i][j],j),(i//3,j//3,board[i][j])])
        return len(res)==len(set(res))
