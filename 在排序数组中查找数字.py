#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 在排序数组中查找数字.py
@time: 2020/04/09

"""

class Solution:
    def getNumberK(self, arra, k):
        # write code here
        number = 0
        length = len(arra)
        if arra is not None and len(arra) > 0:
            first = self.getFirstK(arra, k, 0, length - 1)
            last = self.getLastK(arra, k, 0, length - 1)
            if first > -1 and last > -1:
                number = last - first + 1
        return number


    def getFirstK(self, arra, k, start, end):
        # write code here
        if start > end:
            return -1
        mid_index = (end + start) // 2
        mid_val = arra[mid_index]
        if mid_val == k:
            if (mid_index > 0 and arra[mid_index-1] != k) or mid_index == 0:
                return mid_index
            else:
                end = mid_index - 1
        elif mid_val > k:
            end = mid_index - 1
        else:
            start = mid_index + 1
        return self.getFirstK(arra, k, start, end)

    def getLastK(self, arra, k, start, end):
        # write code here
        if start > end:
            return -1
        length = len(arra)
        mid_index = (end + start) // 2
        mid_val = arra[mid_index]
        if mid_val == k:
            if (mid_index < length - 1 and arra[mid_index + 1] != k) or mid_index == length - 1:
                return mid_index
            else:
                start = mid_index + 1
        elif mid_val < k:
            start = mid_index + 1
        else:
            end = mid_index - 1
        return self.getLastK(arra, k, start, end)


if __name__ == "__main__":
    arra = [1, 2, 3, 3, 3, 3, 4, 5]
    s = Solution()
    print(s.getNumberK(arra, 3))