#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 二叉树的深度.py
@time: 2020/04/10

"""
'''
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    def treeDepth1(self, root):
        # write code here
        if root is None:
            return 0
        else:
            return  max(self.treeDepth1(root.left), self.treeDepth1(root.right)) + 1

    def treeDepth2(self, root):
        # write code here
        if root is None:
            return 0
        self.depth = 1
        def preOrder(root, currnt_depth):
            if root is None:
                return
            if root.left is None and root.right is None:
                self.depth = max(self.depth, currnt_depth)
            preOrder(root.left, currnt_depth + 1)
            preOrder(root.right, currnt_depth + 1)
        preOrder(root, 1)
        return self.depth

    # 非递归
    def treeDepth3(self, root):
        # write code here
        stack = []
        if root is None:
            return 0
        else:
            stack.append((1, root))
        depth = 0
        while len(stack) > 0:
            # 前序遍历，并记录每个节点的深度
            # 不断更新最大深度
            current_depth, root = stack.pop()
            if root:
                depth = current_depth if current_depth > depth else depth
                stack.append((current_depth+1, root.left))
                stack.append((current_depth+1, root.right))
        return depth





