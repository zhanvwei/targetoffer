#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 在1到n整数中1出现的次数.py
@time: 2020/03/30

"""

'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
1~13中包含1的数字有1、10、11、12、13因此共出现6次。
'''


class Solution:
    # 直接进行统计
    def numberOf1Between1AndN(self, n):
        # write code here
        number = 0
        for i in range(1, n+1):
            number += self.numberOf1(i)
        return  number

    def numberOf1(self, number):
        # write code here
        n = 0
        while number:
            if number % 10 == 1:
                n += 1
            number = number // 10
        return  n

    def numberOf1Between1AndN2(self, n):
        # write code here
        ones, m = 0, 1
        if not n:
            return  0
        while m <= n:
            ones += (n//m + 8)//10*m + (n//m%10== 1)*(n%m + 1)
            m *= 10
        return  ones


    ### 延伸：将1改为k,其中 1<=k<=9
    def numberOfkBetween1AndN(self, n, k):
        # write code here
        if n < k:
            return  0
        if n <= 10:
            return  1
        count = 0
        base = 1
        round = n
        while round > 0:
            weight = round % 10
            round //= 10
            count += round*base
            if weight == k:
                count += (n%base) + 1
            elif weight < k:
                count += 0
            else:
                if not round == 0:
                    count += base
            base *= 10
        return  count




if __name__ == "__main__":
    s = Solution()
    num = s.numberOf1Between1AndN(100)
    num2 = s.numberOf1Between1AndN2(100)
    print(num)
    print(num2)
    # print(s.numberOf1(12))
    print(s.numberOfkBetween1AndN(100, 1))
