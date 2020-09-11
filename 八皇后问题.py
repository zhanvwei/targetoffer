#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 八皇后问题.py
@time: 2020/02/19

"""

'''
在8*8的国际象棋上摆放八个皇后, 使其不能相互攻击, 即任意两个皇后不得处在同一行, 同一列或者同一对角线上
'''
class Solution:
    """回溯法思想"""
    def queens(self, nums = 8, queen_str = ""):
        """
        :param nums: 整个棋盘中想要存放皇后的个数
        :param queen_str: 当前皇后以前所存的皇后的列的位置
        :return:  final_queens: List[int] 最后符合要求的皇后的位置
        """
        final_queens = []
        # 定义递归函数，获取所有八皇后的值
        def back(queen_str):
            if len(queen_str) == nums:
                final_queens.append(queen_str)
                return
            for col in range(nums):
                flag = self.valid(queen_str, col)
                ## 如果当前皇后和前面的所有皇后的位置没有冲突，则继续往下遍历
                if not flag:
                    back(queen_str + str(col))


        back(queen_str)
        return  final_queens

    def valid(self, queen_str, current_queen):
        """
        :param queen_str:  当前皇后以前所存的皇后的列的位置
        :param current_queen: 当前皇后的位置(列)
        :return:  flag: 当前位置的皇后是否与之前所有位置的皇后有冲突
        """
        rows = len(queen_str)
        flag = False
        for row in range(rows):
            ## 对角线上冲突：列的差的绝对值等于行的差的绝对值
            ## 列冲突：
            #if abs(rows - row) == abs(int(queen_str[row]) - current_queen) or int(queen_str[row]) == current_queen:
            if abs(current_queen - int(queen_str[row])) in (0, rows - row):
                flag = True
                break
        return  flag


if __name__ == "__main__":
    ss = Solution()
    final_queens = ss.queens()
    print(final_queens)
    print(len(final_queens))

