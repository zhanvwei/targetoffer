#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 圆圈中最后剩下的数字.py
@time: 2020/04/23

"""
"""
0,1，…n-1这n个数字排成一个圆圈，从数字0开始，
每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。
"""

class Node:
    def __init__(self, x):
        self.x = x
        self.next = None


class Solution:
    # 利用链表
    def lastRemaining1(self, n, m):
        # write code here
        if n <= 0 or m <= 0:
            return -1

        # 构造环形链表
        p_head = current = Node(0)
        for i in range(1, n):
            current.next = Node(i)
            current = current.next
        current.next = p_head #成环

        # 从0节点开始遍历
        current = p_head
        while current.next is not current:
            for _ in range(m - 1):# 遍历到第m个节点
                pre = current
                # 循环结束后，此时current为第m个节点
                current = current.next
            # 删除第m个节点
            pre.next = current.next
            # 从pre.next节点重新开始遍历
            current = pre.next
        return current.x


    ## 利用递归
    def lastRemaining2(self, n, m):
        # write code here
        if n <= 0 or m <= 0:
            return  -1
        # 若只有一个数字,即n = 1时，则返回该数字
        last = 0

        # 否则 f(n, m) = [f(n-1, m) + m] % n
        for i in range(2, n+1):
            last = (last + m) % i
        return  last


if __name__ == "__main__":
    s = Solution()
    print(s.lastRemaining1(5, 5))
    print(s.lastRemaining2(5, 5))
