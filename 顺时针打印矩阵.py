#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 顺时针打印矩阵.py
@time: 2020/03/17

"""

'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''

class Solution:
    #  matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if matrix is None:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        while rows > start * 2 and cols > start * 2:
            self.printMatrixInCircle(matrix, rows, cols, start)
            start += 1
        print('')


    def printMatrixInCircle(self, matrix, rows, cols, start):
        end_x = rows - 1 - start
        end_y = cols - 1 - start

        ## 从左到右打印一行
        for i in range(start, end_y+1):
            number = matrix[start][i]
            print(number, ' ', end = ' ')

        ## 从上到下打印一列
        if start < end_x:
            # 如果终止行号大于起始行号
            for i in range(start+1, end_x+1):
                number = matrix[i][end_y]
                print(number, ' ', end= ' ')

        ## 从右往左打印一行
        ## 终止行号大于起始行号且终止列号大于起始列号
        if start < end_x and start < end_y:
            for i in range(end_y-1, start, -1):
                number = matrix[end_x][i]
                print(number, ' ', end=' ')

        ## 从上到下打印一列
        ## 至少三行两列，终止行号比起始行号至少大于2
        ## 且终止列号要大于起始列号
        if start < end_x - 2 and start < end_y:
            for i in range(end_x-1, start, -1):
                number = matrix[i][start]
                print(number, ' ', end=' ')


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    matrix2 = [[1], [2], [3], [4], [5]]
    matrix3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    S = Solution()
    S.printMatrix(matrix)
    S.printMatrix(matrix2)
    #S.printMatrix(matrix3)
