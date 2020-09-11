#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 礼物的最大价值.py
@time: 2020/04/06

"""

class Solution:
    """
    思路：定义f(i,j)表示到达坐标(i,j)的格子的最大值，
    f(i,j) = max(f(i-1, j), f(i, j-1)) + gift[i, j]
    """
    def getMaxValue(self, matrix):
        # write code here
        if matrix is None:
            return  0
        rows = len(matrix)
        cols = len(matrix[0])
        # 初始化二维数组
        res = [[0]*cols for i in range(rows)]
        res[0][0] = matrix[0][0]
        for i in range(1, rows):
            res[i][0] = res[i-1][0] + matrix[i][0]
        for j in range(cols):
            res[0][j] = res[0][j-1] + matrix[0][j]
        for i in range(1,rows):
            for j in range(1, cols):
                res[i][j] = max(res[i-1][j], res[i][j-1]) + matrix[i][j]
        return res[rows-1][cols-1]

    def getMaxValue1(self, matrix):
        # write code here
        if matrix is None:
            return  0
        rows = len(matrix)
        cols = len(matrix[0])
        res = [0]*cols
        for i in range(rows):
            for j in range(cols):
                up = 0
                left = 0
                if i > 0:
                    # 第i-1行的第j个元素
                    up = res[j]
                if j > 0:
                    # 第i行第j-1个元素
                    left = res[j-1]
                res[j] = max(up, left) + matrix[i][j]
        return res[cols-1]



if __name__ == "__main__":
    matrix = [[1, 10, 3, 8],
              [12, 2, 9, 6],
              [5, 7, 4, 11],
              [3, 7, 16, 5]]
    s = Solution()
    print(s.getMaxValue(matrix))
    print(s.getMaxValue1(matrix))


