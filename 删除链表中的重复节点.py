#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 删除链表中的重复节点.py
@time: 2020/02/26

"""
'''
删除链表中重复的结点
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def deletDuplication(self, p_head: ListNode)-> ListNode:
        if p_head == None or p_head.next == None:
            return p_head
        ## 双指针解决
        p_node = p_head
        compare_node = p_head
        while compare_node != None:
            #compare_node = compare_node.next
            # 当要比较的节点和当前节点值不相等
            if p_node.val != compare_node.val:
                p_node = p_node.next
                p_node.val = compare_node.val
            compare_node = compare_node.next
        p_node.next = None
        return  p_head





class Solution2:
    def deleteDuplication2(self, p_head: ListNode)->ListNode:
        if p_head == None or p_head.next == None:
            return  p_head

        pre_node = None
        current_node = p_head
        while current_node != None:
            next_node = current_node.next
            is_deleted = False
            # 如果当前节点的值和其下一节点的值不相等
            if next_node != None and next_node.val == current_node.val:
                is_deleted = True
            if not is_deleted:
                pre_node = current_node
            else:
                ## 相等，则要删除
                val = current_node.val
                to_delete_node = current_node
                while to_delete_node != None and to_delete_node.val == val:
                    to_delete_node = to_delete_node.next
                if pre_node ==  None:
                    p_head = to_delete_node
                else:
                    pre_node.next = to_delete_node
            current_node = current_node.next
        return  p_head





if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(1)
    node4 = ListNode(3)
    node5 = ListNode(4)
    # node6 = ListNode(4)
    # node7 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    # node5.next = node6
    # node6.next = node7

    s = Solution2()
    print(s.deleteDuplication2(node1).next.val)
    #print(s.deletDuplication(node1).next.next.val)