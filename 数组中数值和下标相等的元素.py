#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 数组中数值和下标相等的元素.py
@time: 2020/04/10

"""

"""
假设一个单调递增的数组里的每个元素都是整数并且是唯一的。编写函数找出数组中任意一个数值
等于其下标的元素。例如，在数组{-3, -1, 1, 3, 5}中，数字和它的下标相等。
"""

class Solution:
    """
      设当下标i对应的值为m，则当m > i时，有下标i+k对应的值m_(i+k) - m_(i) >= k，
      则m_(i+k) >= m_(i) + k > i + k
      即对于k>0来说，下标为i+k的数字所对应的值m_(i+k)大于下标i + k
      同样对于m < i时，有i+k的数字所对应的值m_(i+k)小于下标i + k
    """
    def getNumberSameAsIndex(self, arra):
        # write code here
        if arra is None:
            return  -1
        left = 0
        right = len(arra) - 1
        while left <= right:
            mid = (left + right) >> 1
            if arra[mid] == mid:
                return mid
            if arra[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1
        return  -1


if __name__ == "__main__":
    arra = [-3, -1, 2, 4, 5, 6]
    s = Solution()
    print(s.getNumberSameAsIndex(arra))