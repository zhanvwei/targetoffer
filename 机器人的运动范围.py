#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 机器人的运动范围.py
@time: 2020/02/19

"""
'''
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''

class Solution:
    # 回溯法
    def  movingCount(self, threshold, rows, cols):
        if threshold < 0 or rows <= 0 or cols <= 0:
            return  0
        visited = [0]*(rows*cols)
        ## 从坐标(0, 0)开始计数
        count = self.movingCountCore(threshold, rows, cols, 0, 0, visited)

        return  count

    def movingCountCore(self, threshold, rows, cols, row, col, visited):
        count = 0
        if self.check(threshold, rows, cols, row, col, visited):
            visited[row * cols + col] = True
            count = 1 + self.movingCountCore(threshold, rows, cols, row - 1, col, visited) \
                    + self.movingCountCore(threshold, rows, cols, row + 1, col, visited) \
                    + self.movingCountCore(threshold, rows, cols, row, col - 1, visited) \
                    + self.movingCountCore(threshold, rows, cols, row, col + 1, visited)

        return  count

    def check(self, threshold, rows, cols, row, col, visited):
        """判断机器人能否进入坐标为(row, col)的方格"""
        if row >= 0 and row < rows and col >= 0 and col < cols and \
           (self.getDigitSum(row) + self.getDigitSum(col)) <= threshold and \
            not visited[row * cols + col]:
            return  True
        return  False

    def getDigitSum(self, number):
        """计算一个数字的数位之和"""
        sums = 0
        while number > 0:
            sums += number % 10
            number //= 10
        return  sums





if __name__ == "__main__":
    s = Solution()
    print(s.movingCount(5, 10, 10))