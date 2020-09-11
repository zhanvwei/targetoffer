#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 复杂链表的复制.py
@time: 2020/03/20

"""
'''
在复杂链表中，每个节点除了有next指针指向下一个节点，还有random指针指向链表
中的任意节点或者None.
'''

class ComplexListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


class Solution:
    """
    step1: 把复制的节点链接在原始链表的每个对应节点的后面
    step2: 把复制节点的random指针指向原节点的random指针指向的节点
    step3: 拆分链表，奇数位置为原链表，偶数位置为复制链表，且需注意复制链表中最后一个
           节点的指针不能和原链表指向同一个None节点，而需要重新赋值。
    """
    def clone(self, p_head):
        # write code here
        if p_head is None:
            return
        dummy = p_head
        # step1
        while dummy:
            dummy_next = dummy.next
            copy_node = ComplexListNode(dummy.val)
            dummy.next = copy_node
            copy_node.next = dummy_next
            dummy = dummy_next

        # step2
        dummy = p_head
        while dummy:
            dummy_random = dummy.random
            copy_node = dummy.next
            if dummy_random is not None:
                # 若遍历到的当前节点的random指针指向不为空
                # 则将当前节点的复制节点copy_node也指向原节
                # 点的random指针指向节点的复制节点
                # copy_node -> dummy.next, dummy_random --> dummy_random.next
                copy_node.random = dummy_random.next
            dummy = copy_node.next

        # step3
        dummy = p_head
        copy_head = p_head.next
        while dummy:
            copy_node = dummy.next
            # print(copy_node.val)
            dummy_next = copy_node.next
            dummy.next = dummy_next
            dummy = dummy_next
            if dummy_next:
                copy_node.next = dummy_next.next
            else:
                copy_node.next = None
        return  copy_head


    # 利用字典
    def clone2(self, p_head):
        # write code here
        node_list = []      # 存放各个节点
        random_list = []    # 存放各个节点指向的随机节点，无则为None
        value_list = []     # 存放各个节点的值

        while p_head:
            node_list.append(p_head)
            random_list.append(p_head.random)
            value_list.append(p_head.val)
            p_head = p_head.next
        # 随机节点的索引，random节点的索引，如果没有则为 -1
        random_index_list = list(map(lambda c: node_list.index(c) if c else -1, random_list))

        dummy = ComplexListNode(0)
        pre = dummy
        # 节点列表，只要把这些节点的random设置好，顺序串起来就ok了。
        #node_list = list(map(lambda c: ComplexListNode(c), value_list))
        #print(node_list)
        # 把每个节点的random绑定好，根据对应的index来绑定
        for i in range(len(node_list)):
            if random_index_list[i] != -1:
                node_list[i].random = node_list[random_index_list[i]]
        for i in node_list:
            pre.next = i
            pre = pre.next
        return dummy.next

if __name__ == "__main__":
    node1 = ComplexListNode('A')
    node2 = ComplexListNode('B')
    node3 = ComplexListNode('C')
    node4 = ComplexListNode('D')
    node5 = ComplexListNode('E')


    node1.next = node2
    node1.random = node3
    node2.next = node3
    node2.random = node5
    node3.next = node4
    node4.next = node5
    node4.random = node2

    s = Solution()
    copy_node = s.clone2(node1)
    print(copy_node.next.next.val)
    #print(node1.next.val)