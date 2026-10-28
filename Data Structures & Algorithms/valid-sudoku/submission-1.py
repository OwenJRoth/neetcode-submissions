class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for i in range(0,9):
            temp = [None]*9
            for j in range(0,9):
                if board[i][j] != '.' : 
                    if temp[int(board[i][j])-1] is not None: return False
                    temp[int(board[i][j])-1] = 1

        #collumns
        for j in range(0,9):
            temp = [None]*9
            for i in range(0,9):
                if board[i][j] != '.' : 
                    if temp[int(board[i][j])-1] is not None: return False
                    temp[int(board[i][j])-1] = 1
        #boxs
        boxes = [0,3,6]
        for i in range(0,9):
            temp = [None]*9
            for j in range(0,3):
                for k in range(0,3):
                    #print([(i%3)+j,boxes[i//3]+k])
                    if board[k+boxes[i%3]][j+boxes[i//3]] != '.' : 
                        if temp[int(board[k+boxes[i%3]][j+boxes[i//3]])-1] is not None: return False
                        temp[int(board[k+boxes[i%3]][j+boxes[i//3]])-1] = 1
        return True
        