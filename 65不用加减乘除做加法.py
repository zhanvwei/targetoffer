#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 65不用加减乘除做加法.py
@time: 2020/04/24

"""

class Solution:
    def addTwoNumber(self, a, b):
        #
        while b: # 当没有进位，则达到退出条件，防止溢出
            # 第一步：不考虑进位
            sums = (a ^ b) & 0xffffffff  # python没有无符号右移操作，所以需要越界检查
            # 第二步： 有进位则向左移动
            carry = ((a & b) << 1) & 0xffffffff
            # 第三步：
            a = sums
            b = carry
        if a <= 0x7fffffff:
            result = a
        else:
            result = ~(a ^ 0xffffffff)
        return result

if __name__ == "__main__":
    s = Solution()
    print(s.addTwoNumber(-17, 5))