#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 表示数值的字符串.py
@time: 2020/02/29

"""
"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""

class Solution:
    def regexFun(self, s):
        """正则表达式"""
        import re
        pattern = re.compile("[\\+\\-]?\\d*(\\.\\d+)?([eE][\\+\\-]?\\d+)?")
        return pattern.match(s).group(0) == s



    def isNumeric(self, s):
        """
        :param s: 字符串
        :return: boolean，是否为数字
        """
        if len(s) <= 0:
            return  False
        a_list = [w.lower() for w in s]
        if 'e' in a_list:
            e_index = a_list.index('e')
            front = a_list[:e_index]
            behind = a_list[e_index+1:]
            # e_dot_lst = ['e', '.']
            #if [True for c in behind if c in e_dot_lst ] or len(behind) == 0:
            if 'e' in behind or '.' in behind or len(behind) == 0:
                return  False
            is_front = self.scanDigit(front)
            is_behind = self.scanDigit(behind)
            return  is_front and is_behind
        else:
            is_num = self.scanDigit(a_list)
            return  is_num

    def scanDigit(self, a_list):
        dot_num = 0
        allow_val = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.', 'e']
        for i in range(len(a_list)):
            if a_list[i] not in allow_val:
                return  False
            if a_list[i] == ".":
                dot_num += 1
            if a_list[i] in "+-" and i != 0:
                return  False
        if dot_num > 1:
            return  False
        return  True






if __name__ == "__main__":
    s = Solution()
    print(s.regexFun('1.2e+5'))
    print(s.isNumeric("1.3e235"))
    print(s.isNumeric("+10.0"))

