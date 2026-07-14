class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check_ligne(nums):
            seen = dict()
            for i in nums:
                if i != '.' and i in seen:
                    return False
                elif i!= '.':
                    seen[i]=1
            return True

        for i in range(len(board)):
            if not check_ligne(board[i]):
                return False
            if not check_ligne([board[r][i] for r in range (9)]):
                return False

        for r in range(3):
            for c in range(3):
                box = []
                for i in range(3*r, 3*r+3):
                    for j in range(3*c, 3*c+3):
                        box.append(board[i][j])
                if not check_ligne(box):
                    return False

        return True
