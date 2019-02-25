# coding=utf-8
# @Time: 2/25/2019 2:45 PM

class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    board[i][j] = 0

        for i in range(9):
            for j in range(9):
                if board[i][j] != 0:
                    for column in range(9):
                        if column != j and board[i][j] == board[i][column]:
                            return False
                    for row in range(9):
                        if row != i and board[i][j] == board[row][j]:
                            return False
                    for row in range((i // 3) * 3, (i // 3) * 3 + 3):
                        for col in range((j // 3) * 3, (j // 3) * 3 + 3):
                            if row != i and col != j and board[i][j] == board[row][col]:
                                return False
        return True