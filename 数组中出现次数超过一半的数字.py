#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 数组中出现次数超过一半的数字.py
@time: 2020/03/25

"""
'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，
因此输出2。如果不存在则输出0。
'''

class Solution:
    def moreThanHalfNumber(self, arra):
        # write code here
        if len(arra) == 1:
            return  arra[0]
        if self.checkInvalidArray(arra):
            return  0
        length = len(arra)
        mid = length >> 1
        start = 0
        end = length - 1
        index = self.partition(arra, start, end)
        while index != mid:
            if index > mid:
                end = index - 1
                index = self.partition(arra, start, end)
            else:
                start = index + 1
                index = self.partition(arra, start, end)
        result = arra[mid]
        if not self.checkMoreThanHalf(arra, result):
            return  0
        return result

    def partition(self, arra, start, end):
        # write code here
        if arra is None or start <0 or end > len(arra):
            return None

        pivot = arra[start]
        left = start + 1
        right = end
        while left != right:
            while left < right and arra[left] < pivot:
                left += 1
            while right > left and arra[right] >= pivot:
                right -= 1
            if left < right:
                arra[left], arra[right] = arra[right], arra[left]
        # 将pivot所指元素同left和right指针重合点的元素交换
        arra[start] = arra[left]
        arra[left] = pivot
        return  left

    # 检查数组是否合法
    def checkInvalidArray(self, arra):
        # write code here
        input_invalid = False
        if arra == None or len(arra) <= 0:
            input_invalid = True
        return input_invalid

    # 检查查找到中位数的元素出现次数是否超过所有元素数量的一半
    def checkMoreThanHalf(self, arra, number):
        # write code here
        times = 0
        for i in range(len(arra)):
            if arra[i] == number:
                times += 1
        if times * 2 <= len(arra):
            return False
        return True

    def moreThanHalfNumber2(self, arra):
        # write code here
        if self.checkInvalidArray(arra):
            return  0
        result = arra[0]
        times = 1
        for i in arra:
            if times == 0:
                result = i
                times = 1
            elif result == i:
                times += 1
            else:
                times -= 1

        if not self.checkMoreThanHalf(arra, result):
            return
        return result
if __name__ == "__main__":
    s = Solution()
    arra = [1, 2, 3, 2, 2, 2, 5, 4, 2, 3, 2]
    print(s.moreThanHalfNumber(arra))
    print(s.moreThanHalfNumber2(arra))
