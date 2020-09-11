#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 二进制中1的个数.py
@time: 2020/02/20

"""
"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""

class Solution:
    def numberOf1(self, n):
        # write code here
        if n < 0:
            n = n & 0xffffffff
        count = 0
        while n:
            if n & 1 == 1:
                count += 1
            n >>= 1

        return  count

    def numberOf2(self, n):
        # write code here
        if n < 0:
            n = n & 0xffffffff
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count

    def numberOf3(self, n):
        # write code here
        if n < 0:
            s = bin(n & 0xffffffff)
        else:
            s = bin(n)
        return s.count('1')




if __name__ == "__main__":
    ss = Solution()
    n = -10
    cnt = ss.numberOf1(n)
    print(cnt)