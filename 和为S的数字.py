#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 和为S的数字.py
@time: 2020/04/15

"""

'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
对应每个测试案例，输出两个数，小的先输出。
'''

class Solution:
    # 利用字典
    def findNumbersWithSums1(self, arra, sums):
        # write code here
        if arra is None or len(arra) <= 0:
            return -1
        # 利用字典保存遍历的数字
        dicts = dict()
        for i in range(len(arra)):
            if arra[i] not in dicts.keys():
                k = arra[i]
                dicts[k] = i
            if sums - arra[i] in dicts.keys():
                return arra[i], sums - arra[i]
        return -1

    ## 从数组两边遍历
    def findNumbersWithSums2(self, arra, sums):
        # write code here
        if arra is None or len(arra) <= 0 or arra[-1] + arra[-2] < sums:
            return []
        start = 0
        end = len(arra) - 1
        while start < end:
            temp = arra[start] + arra[end]
            # 如果两数之和大于目标值则左移end指针
            if temp > sums:
                end -= 1
            elif temp < sums: # 反之则右移start指针
                start += 1
            else:
                return arra[start], arra[end]
        return  []






if __name__ == "__main__":
    arra = [1, 2, 4, 7, 11, 15]
    s = Solution()
    print(s.findNumbersWithSums1(arra, 15))
    print(s.findNumbersWithSums2(arra, 15))


