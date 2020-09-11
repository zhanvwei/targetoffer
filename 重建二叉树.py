#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 重建二叉树.py
@time: 2020/02/14

"""

'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''



class BinaryTreeNode:
    ## 定义二叉树节点
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def reConstructBinaryNode(self, pre_order_list, in_order_list):
        ## 递归实现，返回树的根节点
        if not pre_order_list:
            return  None

        # 根据前序遍历找出根节点
        #print(pre_order_list[0])
        root = BinaryTreeNode(pre_order_list[0])
        index = in_order_list.index(root.val)
        left_num = index
        #减1是因为去掉根节点
        #right_num = len(pre_order_list) - left_num - 1
        if set(pre_order_list) != set(in_order_list):
            return  None
        root.left = self.reConstructBinaryNode(pre_order_list[1: 1+left_num], in_order_list[0: left_num])
        root.right = self.reConstructBinaryNode(pre_order_list[left_num+1:], in_order_list[1+left_num:])
        return  root


    def printNodeAtLevel(self, treeNode, level):
        ## 按层序遍历输出树中的某一层的值
        if not treeNode or level < 0:
            return  0
        if level == 0:
            return  treeNode.val
        self.printNodeAtLevel(treeNode.left, level-1)
        self.printNodeAtLevel(treeNode.right, level-1)





if __name__ == "__main__":
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    ss = Solution()
    newTree = ss.reConstructBinaryNode(pre, tin)
    #newTree = ss.reConstruct(pre, tin)


    print(newTree.left)
    #print(ss.printNodeAtLevel(newTree, 1))

