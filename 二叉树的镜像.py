#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 二叉树的镜像.py
@time: 2020/03/09

"""

'''
操作给定的二叉树，将其变换为源二叉树的镜像。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Mirror(self, root):
        ## 递归实现
        if root is None:
            return
        if root.left == None and root.right == None:
            return  root
        p_temp = root.left
        root.left = root.right
        root.right = p_temp
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)






if __name__ == "__main__":
    pNode1 = TreeNode(8)
    pNode2 = TreeNode(6)
    pNode3 = TreeNode(10)
    pNode4 = TreeNode(5)
    pNode5 = TreeNode(7)
    pNode6 = TreeNode(9)
    pNode7 = TreeNode(11)

    pNode1.left = pNode2
    pNode1.right = pNode3
    pNode2.left = pNode4
    pNode2.right = pNode5
    pNode3.left = pNode6
    pNode3.right = pNode7

    S = Solution()
    S.Mirror(pNode1)
    print(pNode1.right.val)