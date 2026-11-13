class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check_duplicates(lst):
            lst_stripped = [item for item in lst if item != "."]
            lst_set = set(lst_stripped)

            if len(lst_stripped) == len(lst_set):
                return True
            return False

        ## Check Rows
        for row in board: # board = (row, row, row, ...)
            if not check_duplicates(row):
                print("break row")
                return False

        ## Check Columns 
        columns = list(zip(*board))

        for column in columns: 
            if not check_duplicates(column):
                print("break column")
                return False

        ## Check Boxes
        row, column = 0, 0
        board_lst = []

        while row < 3:

            while column < 3:
                for i in range(3):
                    for j in range (3):
                        board_lst.append(board[3*row + i][3*column + j])
                
                if not check_duplicates(board_lst):
                    print("Fail here")
                    print(f"Column: {column} and Row: {row}")
                    print(board_lst)
                    return False
                column += 1
                board_lst = []

            column = 0 
            row += 1 

        return True
