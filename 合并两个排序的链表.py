#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 合并两个排序的链表.py
@time: 2020/03/04

"""

'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def merge(self, p_head1, p_head2):
        if p_head1 is None:
            return  p_head2
        if p_head2 is None:
            return  p_head1

        merge_head = None
        if p_head1.val > p_head2.val:
            merge_head = p_head2
            merge_head.next = self.merge(p_head1, p_head2.next)
        elif p_head1.val < p_head2.val:
            merge_head = p_head1
            merge_head.next = self.merge(p_head1.next, p_head2)
        return  merge_head

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(5)
    node1.next = node2
    node2.next = node3

    node4 = ListNode(2)
    node5 = ListNode(4)
    node6 = ListNode(6)
    node4.next = node5
    node5.next = node6

    S = Solution()
    result = S.merge(None, None)
    print(result.val)