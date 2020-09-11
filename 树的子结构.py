#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 树的子结构.py
@time: 2020/03/04

"""


'''
输入两棵二叉树A，B，判断B是不是A的子结构
空树不是任意一个树的子结构
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasSubTree(self, p_root1, p_root2):
        result = False
        if p_root1 != None and p_root2 != None:
            if p_root1.val == p_root2.val:
                result = self.doseTree1HasTree2(p_root1, p_root2)
            if not result:
                result = self.hasSubTree(p_root1.left, p_root2)
            if not result:
                result = self.hasSubTree(p_root1.right, p_root2)
        return  result

    def doseTree1HasTree2(self, p_root1, p_root2):
        if p_root2 is None:
            return  True
        if p_root1 is None:
            return  False
        if p_root1.val != p_root2.val:
            return  False
        return  self.doseTree1HasTree2(p_root1.left, p_root2.left) and \
            self.doseTree1HasTree2(p_root1.right, p_root2.right)


if __name__ == "__main__":
    pRoot1 = TreeNode(8)
    pRoot2 = TreeNode(8)
    pRoot3 = TreeNode(7)
    pRoot4 = TreeNode(9)
    pRoot5 = TreeNode(2)
    pRoot6 = TreeNode(4)
    pRoot7 = TreeNode(7)
    pRoot1.left = pRoot2
    pRoot1.right = pRoot3
    pRoot2.left = pRoot4
    pRoot2.right = pRoot5
    pRoot5.left = pRoot6
    pRoot5.right = pRoot7

    pRoot8 = TreeNode(8)
    pRoot9 = TreeNode(9)
    pRoot10 = TreeNode(2)
    pRoot8.left = pRoot9
    pRoot8.right = pRoot10

    S = Solution()
    print(S.hasSubTree(pRoot1, pRoot8))