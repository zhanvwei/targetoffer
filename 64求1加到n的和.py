#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 64求1加到n的和.py
@time: 2020/04/24

"""

class Solution:
    def sumNumbers1(self, n):
        """
        :param n: int: 表示1+2+...+n
        :return: int: 1+2+...+n的和
        """
        return  (1+n)*n // 2



    # if(A and B)  // 若 A == false ，则 B 的判断不会执行（即短路），直接判定 A and B 为 false
    # if(A or B) // 若 A 为 true ，则 B 的判断不会执行（即短路），直接判定 A or B 为 true
    def sumNumbers2(self, n):
        self.sum = 0
        n > 0 and self.sumNumbers2(n-1)
        self.sum += n
        return  self.sum


if __name__ == "__main__":
    s = Solution()
    result1 = s.sumNumbers1(100)
    result2 = s.sumNumbers2(100)
    print(result1)
    print(result2)
