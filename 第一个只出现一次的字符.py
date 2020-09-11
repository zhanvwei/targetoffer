#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 第一个只出现一次的字符.py
@time: 2020/04/07

"""
'''
在一个字符串(1<=字符串长度<=10000，全部由大写字母组成)中找到第一个只出现一次的字符。
'''

class Solution:
    def firstNotRepeatingChar1(self, string):
        # write code here
        if string is None:
            return -1
        for s in string:
            if string.count(s) == 1:
                return s
        return -1


    def firstNotRepeatingChar2(self, string):
        # write code here
        if string is None:
            return  -1
        # 第一次遍历用于保存字符出现的次数
        alphabet = {}
        # 第二次遍历找到首次不重复出现的字符
        alist = list(string)
        for s in string:
            if s not in alphabet.keys():
                alphabet[s] = 0
            alphabet[s] += 1
        for i in alist:
            if alphabet.get(i) == 1:
                return i
        return  -1



if __name__ == "__main__":
    s = Solution()
    print(s.firstNotRepeatingChar1('abaccdeff'))
    print(s.firstNotRepeatingChar2('abaccdeff'))