#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 二叉搜索树的第k大节点.py
@time: 2020/04/10

"""

'''
给定一颗二叉搜索树，请找出其中的第k大的结点。例如，
    5
   / \
  3  7
 /\ /\
2 4 6 8 中，
按结点数值大小顺序第三个结点的值为4。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.tree_node = []

    # 中序遍历：递归
    def kthNode1(self, root, k):
        # write code here
        if root is None or k == 0:
            return None
        self.inOrder(root)
        if len(self.tree_node) < k:
            return -1
        return self.tree_node[k-1]


    def inOrder(self, root):
        # write code here
        if root is None:
            return None
        if root.left:
            self.inOrder(root.left)
        self.tree_node.append(root)
        if root.right:
            self.inOrder(root.right)


    # 中序遍历：非递归
    def kthNode2(self, root, k):
        # write code here
        if root is None or k == 0:
            return None
        stack, nodes = [], []
        p_node = root
        while p_node or len(stack) > 0:
            while p_node:
                stack.append(p_node)
                p_node = p_node.left
            if len(stack) > 0:
                p_node = stack.pop()
                nodes.append(p_node)
                p_node = p_node.right
        if len(nodes) < k:
            return -1
        return nodes[k-1]




