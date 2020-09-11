#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 二叉树的下一个节点.py
@time: 2020/02/17

"""

'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''



class BinaryTreeNode:
    ## 定义二叉树节点
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None



class Solution:
    def getNextNode(self, tree_node):
        ## 如果该点为None则返回None
        if tree_node == None:
            return  None
        p_next = None
        # 如果该节点有右子树，则它的下一个节点就是它的右子树中的最左子节点
        if tree_node.right != None:
            p_right = tree_node.right
            while p_right.left:
                p_right = p_right.left
            p_next = p_right
        else:
            ## 当该节点没有右子树时，且其父节点不为空时
            if tree_node.parent != None:
                p_current = tree_node
                p_parent = tree_node.parent
                # 如果该节点为其父节点的左子节点，则该节点的下一个节点就是其父节点
                if p_current == p_parent.left:
                    p_next = p_parent
                else:
                    # 当该节点为其父节点的右子节点时，则沿着该节点指向父节点方向一直往上遍历
                    # 直到找到一个是其父节点的左子节点，若存在，则该父节点即为该节点的下一个节点
                    while p_parent and p_parent.right == p_current:
                        p_current = p_parent
                        p_parent = p_parent.parent
                    if p_parent:
                        p_next = p_parent

        return  p_next





