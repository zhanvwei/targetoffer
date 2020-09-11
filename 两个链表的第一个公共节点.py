#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 两个链表的第一个公共节点.py
@time: 2020/04/07

"""
'''
输入两个链表，找出它们的第一个公共结点。
'''

class ListNode:
    def __init__(self, x):
        self.x = x
        self.next = None



class Solution:
    def findFirstCommonNode(self, phead1, phead2):
        # write code here
        if phead1 is None or phead2 is None:
            return  None
        length1 = self.getListLength(phead1)
        length2 = self.getListLength(phead2)
        length_diff = abs(length1 - length2)

        if length1 > length2:
            p_long = phead1
            p_short = phead2
        else:
            p_long = phead2
            p_short = phead1
        for _ in range(length_diff):
            p_long = p_long.next

        while p_long is not None and p_short is not None and p_long != p_short:
            p_long = p_long.next
            p_short = p_short.next
        return  p_long


    def getListLength(self, phead):
        # write code here
        if phead is None:
            return  0
        length = 0
        while phead is not  None:
            phead = phead.next
            length += 1
        return  length


if __name__ == "__main__":
    s = Solution()
    phead1 = ListNode(1)
    pnode2 = ListNode(2)
    pnode3 = ListNode(3)

    phead2 = ListNode(4)
    pnode5 = ListNode(5)
    pnode6 = ListNode(6)
    pnode7 = ListNode(7)

    phead1.next = pnode2
    pnode2.next = pnode3
    pnode3.next = pnode6
    pnode6.next = pnode7

    phead2.next = pnode5
    pnode5.next = pnode6

    common_node = s.findFirstCommonNode(phead1, phead2)
    print(common_node.x)