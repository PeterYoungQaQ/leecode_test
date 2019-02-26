# coding=utf-8
# @Time: 2/26/2019 1:43 PM
from typing import List


class Solution:
    def isValue(self, board, x, y):
        # 检查填入的坐标是否与行中已有的元素相等
        for i in range(9):
            if i != x and board[i][y] == board[x][y]:
                return False
        # 检查行是否符合
        for j in range(9):
            if j != y and board[x][j] == board[x][y]:
                return False

        # 检查每个正方形是否符合
        m = 3 * (x // 3)
        n = 3 * (y // 3)
        for i in range(3):
            for j in range(3):
                if (i + m != x or j + n != y) and board[i + m][j + n] == board[x][y]:
                    return False
        return True

    def dfs(self, board):
        # 遍历每一个坐标
        for i in range(9):
            for j in range(9):
                # 找board里的需要填入的位置
                if board[i][j] == '.':
                    for k in '123456789':
                        board[i][j] = k
                        # 在if的时候调用递归
                        if self.isValue(board, i, j) and self.dfs(board):
                            return True
                        # 到这个位置说明填入的数不太行，所以先空着
                        board[i][j] = '.'
                    # 进行完当前可选的所有数字都不行，说明上一次决策有问题，返回false

                    return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.dfs(board)

