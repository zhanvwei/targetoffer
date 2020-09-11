#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 把数字翻译成字符串.py
@time: 2020/04/05

"""
"""
给定一个数字，按照如下规则翻译成字符串：0翻译成“a”，1翻译成“b”...25翻译成“z”。
一个数字有多种翻译可能，例如12258一共有5种，分别是bccfi，bwfi，bczi，mcfi，mzi。
实现一个函数，用来计算一个数字有多少种不同的翻译方法。
"""

class Solution:
    # 递归
    def getTranslationCount(self, number):
        # write code here
        if number < 0:
            return 0
        if number < 26:
            if number < 10:
                return  1
            else:
                return  2
        else:
            str_number = str(number)
            if len(str_number) > 2:
                return self.getTranslationCount(int(str_number[1:])) + \
                       self.getTranslationCount(int(str_number[2:]))
            else:
                return self.getTranslationCount(int(str_number[1:]))

    def getTranslationCount1(self, number):
        # write code here
        if number < 0:
            return 0

        str_number = str(number)
        length = len(str_number)
        # 初始化
        # dp = [1]*length
        dp = [1 for _ in range(length+1)]
        #print(len(dp))
        for i in range(2, length+1):
            # 当第一个数和第二个数组成的数在[10, 25]中则有两种翻译情况，即把第一个和第二个分开或不分开翻译
            # 否则只有一种情况，即不分开翻译
            if int(str_number[i-2: i]) >= 10 and\
               int(str_number[i-2: i]) <= 25:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        print(dp)
        return  dp[length]






if __name__ == "__main__":
    s = Solution()
    print(s.getTranslationCount(34))
    print(s.getTranslationCount1(1011))
