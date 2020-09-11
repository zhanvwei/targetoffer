#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 数组中的重复数字.py
@time: 2020/02/11

"""
"""
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是重复的数字2或者3。
"""


class Solution:
    """
    思路1：先对数组进行排序，扫描排序后的数组，时间复杂度为O(nlogn)；
    思路2：利用hash表解决，时间复杂度是O(n)，空间复杂度也为O(n)；
    思路3：利用数组中值和其下标的关系
    """
    def duplicate1(self, arr):
        """排序后查找"""
        arr_sorted = sorted(arr)
        length = len(arr)
        repeatNum = []
        for i in range(1, length):
            if arr_sorted[i] == arr_sorted[i-1]:
                repeatNum.append(arr_sorted[i])
        return  repeatNum


    def duplicate2(self, arr):
        """hash表"""
        hash_map = dict()
        repeatNum = []
        for i, val in enumerate(arr):
            if val in hash_map.keys():
                repeatNum.append(val)
                #break
            hash_map[val] = i
        return  repeatNum



    def  duplicate3(self, arr):
        """时间换空间"""
        if arr == None or len(arr) <= 0:
            return  None
        for i in arr:
            if i < 0 or i > len(arr) - 1:
                return  None
        repeatNum = []
        for i in range(len(arr)):
            while arr[i] != i:
                if arr[i] == arr[arr[i]]:
                    repeatNum.append(arr[i])
                    #break
                else:
                    index = arr[i]
                    arr[i], arr[index] = arr[index], arr[i]
        return  repeatNum


if __name__ == "__main__":
    arr = [2, 3, 1, 0, 2, 5, 3]
    ss = Solution()
    repeatNum = ss.duplicate1(arr)
    #repeatNum = ss.duplicate2(arr)
    #repeatNum = ss.duplicate3(arr)
    print(repeatNum)

