#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 字符流中第一个只出现一次的字符.py
@time: 2020/04/07

"""
'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
如果当前字符流没有存在出现一次的字符，返回#字符。
'''

from collections import OrderedDict

class Solution:
    def __init__(self):
        # 有序字典（否则用dict()+list）
        self.dicts = OrderedDict()
    def firstAppearingOnce(self):
        # write code here
        for c in self.dicts.keys():
            if self.dicts.get(c) == 1:
                return  c
        return -1

    def insert(self, char):
        # write code here
        if char in self.dicts.keys():
            self.dicts[char] += 1
        else:
            self.dicts[char] = 1
