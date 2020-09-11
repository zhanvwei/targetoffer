#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 数组中只出现一次的数字.py
@time: 2020/04/13

"""

"""
数组中只出现一次的两个数字。
一个整型数组里除两个数字之外，其他数字都出现了两次。要求时间复杂度O(n),
空间复杂度为O(1)。
"""
class Solution:
    def numberAppearOnce(self, arra):
        # write code here
        a = 0
        for i in arra:
            a^= i
            # print(a)
        return a

    def findNumberAppearOnce(self, arra):
        # write code here
        if arra is None or len(arra) <= 0:
            return []
        temp = 0
        for i in arra:
            temp ^= i
        index = self.findFirstBitIs1(temp)
        num1, num2 = 0, 0
        for i in range(len(arra)):
            if self.isBit1(arra[i], index):
                num1 ^= arra[i]
            else:
                num2 ^= arra[i]
        return [num1, num2]


    def findFirstBitIs1(self, n):
        # write code here
        index_bit = 0
        while n & 1 == 0 and index_bit <= 64:
            index_bit += 1
            n >>= 1
        return index_bit
    # 判断一个数的二进制的第index位是否为1
    def isBit1(self, n, index):
        # write code here
        n = n >> index
        return n & 1





"""
题二：
数组中只出现一次的一个数字。
一个整型数组里除一个数字之外，其他数字都出现了三次。要求时间复杂度O(n),
空间复杂度为O(1)。
"""

class Solution2:
    def singleNumber(self, arra):
        # write code here
        positive, negtive = 0, 0
        for i in range(32):
            pos_count, neg_count = 0, 0
            for num in arra:
                if num >= 0:
                    if num & (1 << i):
                        pos_count += 1
                else:
                    if abs(num) & (1 << i):
                        neg_count += 1
            if pos_count % 3 == 1:
                positive += 1 << i
            if neg_count % 3 == 1:
                negtive += 1 << i
        return positive if positive else -negtive






if __name__ == "__main__":
    s1= Solution()
    s2 = Solution2()
    arra1 = [1,5,3,1,3,6]
    arra2 = [1, 1, 1, -3, 5, 6, 6, 5, 6, 5]
    # print(s.numberAppearOnce(arra1))
    print(s1.findNumberAppearOnce(arra1))
    print(s2.singleNumber(arra2))


