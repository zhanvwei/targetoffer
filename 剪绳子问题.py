#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 剪绳子问题.py
@time: 2020/02/20

"""

"""
给一根长度为n的绳子，请把绳子剪成m段(n, m > 1)，每段长度记为k[0],k[1],k[2],...,
求k[0]*k[1]*k[2]*...*k[m]的最大乘积。
"""

class Solution:
    """动态规划思想和贪婪法思想"""
    def maxProductAfterCutting(self, n):
        if n <= 3:
            return  n - 1
        # 保存结果
        products = [0, 1, 2, 3]
        for i in range(4, n+1):
            temp_max = 0
            for j in range(1, i // 2+1):
                if temp_max < products[j]*products[i-j]:
                    temp_max = products[j]*products[i-j]
            products.append(temp_max)
        max_product = max(products)
        return max_product


if __name__ == "__main__":
    ss = Solution()
    res = ss.maxProductAfterCutting(6)
    print(res)