#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 链表中环的入口节点.py
@time: 2020/03/03

"""
'''
一个链表中包含环，请找出该链表的环的入口结点。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def meetingNode(self, p_head):
        """
        若链表存在环，则通过两个一快一慢的指针找到其相遇的节点
        """
        if p_head is None:
            return None
        p_slow = p_head.next
        if p_slow is None:
            return  None
        p_fast = p_slow.next
        while p_fast:
            if p_slow == p_fast:
                return  p_slow
            p_slow = p_slow.next
            p_fast = p_fast.next
            if p_fast:
                p_fast = p_fast.next
        return  None

    def entryNodeOfLoop(self, p_head):
        """
        当找到环内的任意节点后，
        就可以得到环的节点数，并找到环的入口节点
        """
        meeted_node = self.meetingNode(p_head)
        if meeted_node is None:
            return  None

        p_node = meeted_node
        loop_node_nums = 1
        while p_node.next != meeted_node:
            loop_node_nums += 1
            p_node = p_node.next

        # 找到环的入口节点
        p_front = p_head
        for i in range(loop_node_nums):
            p_front = p_front.next

        p_rear = p_head
        while p_front != p_rear:
            p_front = p_front.next
            p_rear = p_rear.next
        return  p_front


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node6

    s = Solution()
    print(s.entryNodeOfLoop(node1).val)
