#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 调整数组顺序使奇数位于偶数前面.py
@time: 2020/03/01

"""

'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''


class Solution:
    def reorderOddEven(self, array):
        """类似快排"""
        if len(array) < 1:
            return  array

        front = 0
        rear = len(array) - 1
        while front < rear:
            # 向后移动front，直到它指向偶数
            while array[front] & 0x1 == 1:
                front += 1
            # 向前移动rear, 直到它指向基数
            while array[rear] & 0x1 == 0:
                rear -= 1
            # 如果front < rear,则交换两数的位置，否则则说明已经所有的基数已经在偶数前面了
            if front < rear:
                array[front], array[rear] = array[rear], array[front]
        return  array

    def reorderOddEven2(self, array):
        left = [x for x in array if x&0x1 == 0]
        right = [x for x in array if x&0x1 == 1]
        return  left + right

    def reoderOddEven3(self, array):
        if len(array) < 1:
            return  array
        odd_array = []
        even_array = []
        for i in array:
            if i&0x1:
                odd_array.append(i)
            else:
                even_array.append(i)
        return  even_array + odd_array


    ## 可扩展性写法
    def reoder(self, array, length, func):
        if length == 0:
            return
        p_begin = 0
        p_end = length - 1
        while p_begin < p_end:
            while p_begin < p_end and not func(array[p_begin]):
                p_begin += 1
            while p_begin < p_end and  func(array[p_end]):
                p_end -= 1
            if p_begin < p_end:
                array[p_begin], array[p_end] = array[p_end], array[p_begin]

        return  array

    def isEven(self, n):
        return  not n&0x1

    def isNegtive(self, n):
        return n >= 0

    def reorderOddEven4(self, array):
        length = len(array)
        return  self.reoder(array, length, self.isEven)






if __name__ == "__main__":
    s = Solution()
    array = [1, 2, 3, 4, 5]
    #result = s.reorderOddEven(array)
    result = s.reorderOddEven4(array)
    print(result)