#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 60n个骰子的点数.py
@time: 2020/04/23

"""
'''
把n个骰子扔在地上, 所有骰子朝上一面的点数和为s。
输入n, 打印出s的所有可能的值出现的概率
'''

class Solution:
    # 利用两个数组保存骰子点数的每个总数出现的次数
    # 第一个数组表示在该轮循环中，第n个数字表示和为n出现的次数
    # 第二个数组保存在下一轮循环中,新增一个骰子出现的次数总和，
    # 则第二个数组中和为n的次数应该等于上一轮和为n-1, n-2,...,n-6的总和。
    def printProbability(self, number: int):
        # write code here
        #

        max_val = 6 #最大的点数
        res = [[], []]
        res[0] = [0]*(max_val*number+1)
        flag = 0  # 用于转换行数
        for i in range(1, max_val + 1): # 初始化，投掷第一颗骰子
            res[flag][i] = 1
        for time in range(2, number + 1): # 投掷的骰子颗数
            res[1-flag] = [0]*(max_val*number+1)
            for j in range(time, max_val*time+1): # 和的取值范围
                r = j if j < 6  else 6+1 # j = 3 , r = 4, f[3] = f[3-1]+ f[3-2] + f[3-3]
                for k in range(1, r): # f[n] = f[n-1]+f[n-2]+...+f[n-6], 取min(n, 6)
                    res[1-flag][j] += res[flag][j-k]
            flag = 1 - flag

        total = max_val**number
        for i in range(number, max_val*number+1):
            ratio = res[flag][i] /float(total)
            print("{}: {:e}".format(i, ratio), end=' ')


    def print_probability(self, n):
        if n < 0:
            return []
        cols = 6 * n + 1  # 保留0个骰子情况
        dp = [0 for i in range(cols)]
        # 1个骰子时的初始值
        for i in range(1, 7):
            dp[i] = 1
        for i in range(2, n + 1):  # 2到n个骰子时
            # for j in range(i,6*i+1,1):#可能出现的点数之和
            for j in range(6 * i, i - 1, -1):  # 注意这里要从后往前算，
                # 如果从前往后算，计算do【3】使用的dp【2】是当前骰子的次数，不是n-1个骰子的次数
                dp[j] = 0
                for cur in range(1, 6 + 1):
                    if j - cur <= 0:
                        break
                    dp[j] += dp[j - cur]

        res = []
        allcount = pow(6, n) * 1.0  # 所有情况出现的次数,转成float
        for i in range(n, 6 * n + 1):
            res.append(dp[i] / allcount)
        return res

if __name__ == "__main__":
    s = Solution()
    s.printProbability(3)
    print(s.print_probability(3))


