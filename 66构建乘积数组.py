#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 66构建乘积数组.py
@time: 2020/04/24

"""

"""
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，
其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
"""

class Solution:
    def constructArr(self, alist:list)->list:
        # write code here
        # 初始化
        length = len(alist)
        blist = [1]*length
        temp = 1

        # 计算下三角 c[i] = a[0]*a[1]*...*a[i-1], d[i] = a[i+1]*a[i+2]+...+a[n-1]
        # c[i] = c[i-1]*a[i-1], d[i] = d[i+1]*a[i+1]
        for i in range(1, len(alist)):
            blist[i] = blist[i-1] * alist[i-1]

        for j in range(length - 2, -1, -1):
            # temp保存a[n-1]*a[n-2]*...a[j+1]的值
            temp *= alist[j+1]
            blist[j] *= temp
        return blist


if __name__ == "__main__":
    s = Solution()
    alist = [1,2,3,4,5]
    print(s.constructArr(alist))
