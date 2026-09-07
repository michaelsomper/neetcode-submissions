class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Check rows
        for row in board:
            seen = set()
            for dig in row:
                if dig == ".":
                    continue
                else:
                    if dig in seen:
                        return False
                    else:
                        seen.add(dig)
        
        # 2. Check columns
        for col in zip(*board):
            seen = set()
            for dig in col:
                if dig == ".":
                    continue
                else:
                    if dig in seen:
                        return False
                    else:
                        seen.add(dig)

        # 3. Check grid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                # Here we have a pointer to a 3x3 grid
                seen = set()
                for x in range(3):
                    for y in range(3):
                        if board[j+y][i+x] == ".":
                            continue
                        else:
                            if board[j+y][i+x] in seen:
                                return False
                            else:
                                seen.add(board[j+y][i+x])
        
        return True


