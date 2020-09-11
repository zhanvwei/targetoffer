#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 连续子数组的最大和.py
@time: 2020/03/30

"""
'''
输入一个整型数组,数组里有整数也有负数。
数组中一二或连续的多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)
'''

class Solution:
    def findGreatestSumOfSubArray(self, arra):
        # write code here
        if arra is None or len(arra) <= 0:
            return 0

        current_sum = 0 # 当前所求和
        greatest_sum = 0 # 当前最大和
        for i in range(len(arra)):
            # 若当前和小于0，则当前和为arra[i], 否则加上arra[i]
            if current_sum <= 0:
                current_sum = arra[i]
            else:
                current_sum += arra[i]
            if current_sum > greatest_sum:
                greatest_sum = current_sum
        return  greatest_sum


    def findGreatestSumOfSubArray2(self, arra):
        # 动态规划
        # write code here
        if arra is None or len(arra) <= 0:
            return 0
        alist = [0]*len(arra)
        for i in range(len(alist)):
            if i == 0 or alist[i-1] <= 0:
                alist[i] = arra[i]
            else:
                alist[i] = alist[i-1] + arra[i]
        return  max(alist)

if __name__ == "__main__":
    alist = [1, -2, 3, 10, -4, 7, 2, -5]
    s = Solution()
    gsum = s.findGreatestSumOfSubArray(alist)
    gsum2 = s.findGreatestSumOfSubArray2(alist)
    print(gsum)
    print(gsum2)

