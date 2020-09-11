#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 0-n-1中缺失的数字.py
@time: 2020/04/10

"""
"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0~n-1之内。
在范围0~n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
"""

class Solution:
    # 直接利用和相减
    def getMissingNumber1(self, arra):
        # write code here
        number = len(arra)+1
        sum1 = number*(number - 1) >> 1
        sum2 = 0
        for i in arra:
            sum2 += i
        return  sum1 - sum2


    # 二分法
    def getMissingNumber2(self, arra):
        # write code here
        if arra is None or len(arra) <= 0:
            return -1
        start = 0
        end = len(arra) - 1
        while start <= end:
            middle = (start + end) >> 1
            if arra[middle] != middle:
                if middle == 0 or arra[middle-1] == middle - 1:
                    return middle
                end = middle - 1
            else:
                start += 1
        if start == len(arra):
            return  len(arra)
        return  -1


if __name__ == "__main__":
    arra = [0, 1, 2, 3, 4, 6, 7, 8, 9]
    s = Solution()
    print(s.getMissingNumber1(arra))
    print(s.getMissingNumber2(arra))
