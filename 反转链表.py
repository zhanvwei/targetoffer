#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 反转链表.py
@time: 2020/03/03

"""

"""
输入一个链表，反转链表后，输出链表的所有元素
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def reverseList(self, p_head):
        # 用于存储反转后链表的头节点
        p_reverse_head= None
        # 当前节点
        p_current = p_head
        # 当前节点的上一节点
        p_pre = None
        while p_current :
            # 得到当前节点的下一节点
            p_next = p_current.next
            if p_next is None:
                p_reverse_head = p_current
            # 断开当前节点与其下一节点的连接，
            # 并将当前节点的下一节点指向其原先的上一个节点
            p_current.next = p_pre
            # 后移当前节点的下一节点及本身
            p_pre = p_current
            p_current = p_next
        return  p_reverse_head


    def reverseListRcursion(self, p_head, new_head): # p_head为原链表的头节点， new_head为反转后链表的头节点
        """递归实现"""
        # 如果当前节点为空或只有一个单一节点，则返回该节点
        if p_head is None:
            return  None
        if p_head.next is None:
            new_head = p_head
        else:
            new_head = self.reverseListRcursion(p_head.next, new_head)
            print(new_head)
            p_head.next.next = p_head
            p_head.next = None
        return  new_head

    def reverseListRcusion1(self, p_head):
        if p_head is None:
            return  None
        if p_head.next is None:
            new_head = p_head
        else:
            new_head = self.reverseListRcusion1(p_head.next)
            #print(new_head)
            p_head.next.next = p_head
            p_head.next = None
        return  new_head



if __name__ == "__main__":
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(13)
    node1.next = node2
    node2.next = node3

    S = Solution()
    #p1 = S.reverseList(node1)
    # p2 = S.reverseListRcursion(node1, None)
    #print(p1.val)
    #print(p2.val)
    p3 = S.reverseListRcusion1(node1)
    print(p3.next.val)

