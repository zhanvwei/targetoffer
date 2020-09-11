#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 链表中的倒数第k个节点.py
@time: 2020/03/01

"""

'''
输入一个链表，输出该链表中倒数第k个结点。
'''

'''
这道题的思路很好
如果在只希望一次遍历的情况下, 寻找倒数第k个结点, 可以设置两个指针
第一个指针先往前走k-1步, 然后从第k步开始第二个指针指向头结点
然后两个指针一起遍历
当地一个指针指向尾节点的时候, 第二个指针正好指向倒数第k个结点
推广: 寻找中间节点, 两个指针一起, 第一个指针每次走两步, 第二个指针每次走一步,  快指针指到尾部, 慢指针正好指到中间
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def findKthToTail(self, head, k):
        if head == None or k <= 0:
            return  None
        p_head = head
        for i in range(k-1):
            # 判断链表的节点数是否大于k的情况
            if p_head.next != None:
                p_head = p_head.next
            else:
                return  None
        p_behind = head
        while p_head.next:
            p_head = p_head.next
            p_behind = p_behind.next

        return  p_behind


if __name__ == "__main__":
    node1 = ListNode(10)
    node2 = ListNode(11)
    node3 = ListNode(13)
    node1.next = node2
    node2.next = node3

    S = Solution()
    print(S.findKthToTail(node1, 2).val)