#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 二维数组中查找.py
@time: 2020/02/11

"""

'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

class Solution:
    """
    从数组的右上角(or左下角)的元素开始查找，
    若当target大于右上角的元素，则下移一位继续查找，
    若当target小于右上角的元素，则左移一位继续查找。
    """

    def findTarget(self, array, target):
        # 判断数组是否为空
        if array == []:
            return  False

        row_nums = len(array)
        col_nums = len(array[0])

        xrow = 0
        xcol = col_nums - 1
        while xcol >= 0 and xrow < row_nums:
            x = array[xrow][xcol]
            if x == target:
                return  True
            elif x > target:
                xcol -= 1
            else:
                xrow += 1
        return  False


if __name__ == "__main__":
    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    tartget = 8
    ss = Solution()
    flag = ss.findTarget(array, tartget)
    print(flag)