#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 二叉搜索树与双向链表.py
@time: 2020/03/20

"""

'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convert(self, root):
        if root is None:
            return None
        if not root.left and not root.right:
            return  root

        # 处理左子树
        self.convert(root.left)
        left = root.left

        # 连接根与左子树的最大节点
        if left:
            while left.right:
                left = left.right
            root.left, left.right =  left, root

        # 处理右子树
        self.convert(root.right)
        right = root.right

        # 连接根与右子树最小结点
        if right:
            while right.left:
                right = right.left
            root.right, right.left = right, root

        ## 找到双向链表的头节点
        while root.left:
            root = root.left
        return  root

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
    newList = S.convert(pNode1)
    # print(newList.right.right.right.right.val)