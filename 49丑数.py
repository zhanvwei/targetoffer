#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 49丑数.py
@time: 2020/04/06

"""


'''
把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''

class Solution:
    # 直接逐个判断，时间复杂度过高
    def nthUglyNumber1(self, n):
        # write code here
        if n <= 0:
            return  0
        number = 0
        ugly_found = 0
        while ugly_found < n:
            number += 1
            if self.isUglyNumber(number):
                ugly_found += 1
        return  number


    def isUglyNumber(self, number):
        # write code here
        while number % 2 == 0:
            number //= 2
        while number % 3 == 0:
            number //= 3
        while number % 5 == 0:
            number //= 5
        return number == 1

    # 动态规划
    def nthUglyNumber2(self, n):
        # write code here
        # 初始化
        dp, a, b, c = [1]*n, 0, 0, 0
        for i in range(1, n):
            dp[i] = min(dp[a]*2, dp[b]*3, dp[c]*5)
            if dp[i] == dp[a] * 2: a+= 1
            if dp[i] == dp[b] * 3: b += 1
            if dp[i] == dp[c] * 5: c += 1
        return dp[-1]


    ## 最小堆
    def nthUglyNumber3(self, n):
        # write code here
        import  heapq
        # 初始化堆，用于保存根据因数2、3和5产生丑数
        heap = [1]
        heapq.heapify(heap)
        res = 0
        for _ in range(n):
            # 堆中最小的丑数
            res = heapq.heappop(heap)
            # 去重堆中的重复元素
            while heap and res == heap[0]:
                res = heapq.heappop(heap)
            a, b, c = res*2, res*3, res*5
            for t in [a, b, c]:
                heapq.heappush(heap, t)
        return  res





if __name__ == "__main__":
    s = Solution()
    print(s.nthUglyNumber1(4))
    print(s.nthUglyNumber2(7))
    print(s.nthUglyNumber3(4))