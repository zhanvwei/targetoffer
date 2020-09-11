#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 从尾到头打印链表.py
@time: 2020/02/13

"""
"""
输入一个链表的头节点，从尾到头反过来打印出每个节点的值
"""

class ListNode:
    """链表节点"""
    def __init__(self, val):
        self.val = val
        self.next = None



class Solution:
    """"利用栈"""
    def printListFromTail2Head1(self, list_node):
        if list_node.val == None:
            return  None
        stack_list = []
        head = list_node
        while head:
            stack_list.insert(0, head.val)
            head = head.next
        return  stack_list

    def printListFromTail2Head2(self, list_node):
        """递归思想"""
        if list_node == None:
            return  []
        return  self.printListFromTail2Head2(list_node.next) + [list_node.val]


if __name__ == "__main__":
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(13)
    node1.next = node2
    node2.next = node3
    ss = Solution()
    print(ss.printListFromTail2Head2(node1))



