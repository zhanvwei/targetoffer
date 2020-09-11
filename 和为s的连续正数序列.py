#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 和为s的连续正数序列.py
@time: 2020/04/15

"""
'''
输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数），
例如，输入15，由于1+2+3+4+5 = 4+5+6 = 7+8，所以打印出3个连续序列
1~5、4~6和7~8。
'''

class Solution:
    def findContinuousSequence(self, sums):
        # write code here

        small = 1
        big = 2
        mid = (sums + 1) // 2
        current_sums = small + big
        result = []
        while small < mid:
            if current_sums == sums:
                # 若当前连续序列的和等于目标和则将该序列添加到result列表中
                temp = self.getContinuousSequence(small, big)
                result.append(temp)
            while current_sums > sums and small < mid:
                # 若当前连续序列的和大于目标和时，则small往右移，且current_sums减去small
                current_sums -= small
                small += 1
                if current_sums == sums:
                    temp = self.getContinuousSequence(small, big)
                    result.append(temp)
            # 否则右移增加big
            big += 1
            current_sums += big
        return result





    def getContinuousSequence(self, small, big):
        # write code here
        alist = []
        for i in range(small, big+1):
            alist.append(i)
        return  alist


if __name__ == "__main__":
    s = Solution()
    print(s.findContinuousSequence(17))