#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 数组中的重复数字2.py
@time: 2020/02/11

"""

"""
在一个长度为n的数组里的所有数字都在1-n范围内，
数组中至少有一个数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数字中任意一个重复的数字。前提条件是不能修改数组
"""

class Solution:
    """
    思路1：利用hash表解决，时间复杂度是O(n)，空间复杂度也为O(n)；
    思路2：二分查找算法+统计区间数字
    """

    def getDuplicationNum1(self, arr):
        """利用hash表"""
        pass

    def getDuplicationNum2(self, arr):
        """非递归实现"""
        length = len(arr)
        if arr == None or length <= 0:
            return  None
        start = 1
        end = length - 1
        while end >= start:
            middle = (end + start)>> 1
            count = self.countRange(arr, start, middle)
            if end == start:
                if count > 1:
                    return  start
                else:
                    break
            if count > (middle - start + 1):
                end = middle
            else:
                start = middle + 1
        return  None


    def countRange(self, arr, start, end):
        """统计区间[start, left]上的数的个数"""
        if arr == None:
            return 0
        count = 0
        for i in arr:
            if i >= start and i <= end:
                count += 1
        return  count


    def getDuplicationNum3(self, arr, start, end):
        """递归实现"""
        if arr == None or len(arr) <= 0:
            return  0
        for i in arr:
            if i <= 0 or i >= len(arr):
                return  0

        if start == end:
            #if count > 1:
            return  start
        middle = (start + end)//2
        count = 0
        for i in arr:
            if middle <= i <= end:
                count += 1

        if count > end - middle  + 1:
            return  self.getDuplicationNum3(arr, middle+1, end)
        else:
            return  self.getDuplicationNum3(arr, start, middle)










if __name__ == "__main__":
    arr = [2, 3, 5, 4, 3, 2, 6, 7]
    ss = Solution()
    repeatNum = ss.getDuplicationNum3(arr, 1, len(arr)-1)
    #repeatNum = ss.duplicate2(arr)
    #repeatNum = ss.duplicate3(arr)
    print(repeatNum)
