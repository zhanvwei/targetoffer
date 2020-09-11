#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 股票的最大利润.py
@time: 2020/04/24

"""

"""
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
例如，一只股票在某些时间节点的价格为{9,11,8,5,7,12,16,14}。如果我们能在价格为5的时候买入
并在价格为16时卖出，则能收获最大的利润11。
"""

class Solution:
    def maxDiff(self, numbers):
        """
        :param numbers: list 按时间顺序保存的价格列表
        :return: int 所获最大利润值
        """
        if numbers is None or len(numbers) <= 0:
            return  0
        # 记录i前面i-1个数的最小值
        mins = numbers[0]
        # 记录到第i个数时所能获得的最大利润值
        maxs = numbers[1] - mins
        for i in range(2, len(numbers)):
            if numbers[i] < mins:
                mins = numbers[i]
            current = numbers[i] - mins
            if current > maxs:
                maxs = current
        return maxs

if __name__ == "__main__":
    s = Solution()
    alist = [9, 11, 8, 5, 7, 12, 16, 14]
    print(s.maxDiff(alist))


