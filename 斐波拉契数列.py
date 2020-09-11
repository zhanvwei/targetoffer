#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 斐波拉契数列.py
@time: 2020/02/18

"""

"""
求斐波拉契数列的第n项
"""

class Solution:
    def Feibonacci1(self, n):
        """递归思想"""
        if n <= 0:
            return  0
        if n == 1:
            return  1
        return  self.Feibonacci1(n-1) + self.Feibonacci1(n-2)

    def Feibonacci2(self, n):
        """自下而上，循环的思想"""
        res = [0, 1]
        if n < 2:
            return  res[n]
        fib1 = 1
        fib2 = 0
        fib_n = 0
        for i in range(2, n+1):
            fib_n = fib1 + fib2
            fib2 = fib1
            fib1 = fib_n
        return  fib_n


    def jumpFloor1(self, n):
        """
        青蛙跳台阶, 每次可以跳1级或2级
        """
        res = [0, 1, 2]
        if n <= 2:
            return  res[(n+1) % 3 - 1]
        fib1 = 1
        fib2 = 2
        fib_n = 0
        for i in range(3, n+1):
            fib_n = fib1 + fib2
            fib1 = fib2
            fib2 = fib_n
        return  fib_n

    def jumpFloor2(self, n):
        """
        青蛙跳台阶，每次可以跳1级、2级...n级。
        """
        if n <= 0:
            return  0
        ans = 1
        if n >= 2:
            for i in range(n-1):
                ans = ans*2
        return ans









if __name__ == "__main__":
    ss = Solution()
    print(ss.Feibonacci1(10))
    print(ss.Feibonacci2(10))
    print(ss.jumpFloor1(4))
    print(ss.jumpFloor2(1))
