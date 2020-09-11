#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 数字序列中某一位的数.py
@time: 2020/04/03

"""
'''
数字以0123456789101112...的格式序列化到一个字符序列中。在这个序列中，
第5位（从0开始计数）是5，第13位是1，第19位是4，等等。写一个函数，求任
意第n位对应的数字。
'''

class Solution:
    def digitAtIndex(self, n):
        # write code here
        if n < 0:
            return -1
        if n == 0:
            return  0
        digit = 1 # 整数的长度
        base = 1 # 每个区间的个数，如[0,9]为10，[10, 90]为100

        #
        while n > 9*base*digit:
            n -= 9*base*digit # n剩余的位数
            digit += 1
            base *= 10

        # 当前数字，注意为n-1，因为数字是从0开始
        current_num = (n - 1) // digit + base
        index = (n - 1) % digit
        return  str(current_num)[index]



if __name__ == "__main__":
    s = Solution()
    print(s.digitAtIndex(1001))
