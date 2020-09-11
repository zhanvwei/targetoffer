#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 45把数组排成最小的数.py
@time: 2020/04/04

"""

'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''

class Solution:
    # 直接求，利用全排列的思想,时间复杂度为n！
    def printMinNumber(self, arra):
        # write code here
        result = self.permutation(arra)
        #result = [int(i) for i in result]
        return  min(result)

    def permutation(self, arra):
        # write code here
        if arra is None:
            return  []
        if len(arra) == 1:
            return arra
        result = []
        for i in range(len(arra)):
            rest = arra[:i] + arra[i+1:]
            permut_lst = self.permutation(rest)
            temp = []
            for j in range(len(permut_lst)):
                temp.append(str(arra[i]) + str(permut_lst[j]))
            result += temp
        return result


    # 定义比较算法，对于数m和n，若mn>nm，则m>n，否则n>=m
    def printMinNumber2(self, arra):
        # write code here
        from functools import cmp_to_key
        if arra is None or  len(arra) == 0:
            return  ""
        str_arra = [str(i) for i in arra]
        # key是一种排序规则，比较x+y和y+x的大小
        key = cmp_to_key(lambda x, y: int(x+y)-int(y+x))
        str_arra.sort(key= key)
        #print(str_arra)
        return "".join(str_arra)

    # 冒泡排序









if __name__ == "__main__":
    numbers = [3, 32, 321]
    s = Solution()
    print(s.printMinNumber(numbers))
    print(s.printMinNumber2(numbers))