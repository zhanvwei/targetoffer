#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 32从上到下打印二叉树.py
@time: 2020/03/12

"""

'''
题目一：不分行从上往下打印出二叉树的每个节点，同层节点从左至右打印。
题目二：分行从上往下打印出二叉树的每个节点，同层节点按从左至右打印。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def printFromTopToBottom(self, root):
        """层次遍历"""
        if root is None:
            return []
        # 利用列表代替队列
        queue = []
        # 保存遍历结果
        result = []
        queue.append(root)
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result


    def printFromTopToBottomWithLayer(self, root):
        """
        增加两个变量，to_be_printed用于表示当前层中还没有打印的节点数，
        next_level用于表示下一层节点的数目
        """
        if root is None:
            return

        # 利用列表代队列
        queue = []
        queue.append(root)
        to_be_printed = 1
        next_level = 0
        res = []
        temp = []
        while queue != []:
            current_node = queue.pop(0)
            to_be_printed -= 1
            # print(current_node.val, end= " ")
            temp.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
                next_level += 1
            if current_node.right:
                queue.append(current_node.right)
                next_level += 1
            if to_be_printed == 0:
                #print("\n")
                res.append(temp)
                to_be_printed = next_level
                next_level = 0
                temp = []
        return res


if __name__ == "__main__":
    pNode1 = TreeNode(3)
    pNode2 = TreeNode(9)
    pNode3 = TreeNode(20)
    pNode4 = TreeNode(None)
    pNode5 = TreeNode(None)
    pNode6 = TreeNode(15)
    pNode7 = TreeNode(7)

    pNode1.left = pNode2
    pNode1.right = pNode3
    pNode2.left = pNode4
    pNode2.right = pNode5
    pNode3.left = pNode6
    pNode3.right = pNode7

    S = Solution()
    print(S.printFromTopToBottom(pNode1))
    print(S.printFromTopToBottomWithLayer(pNode1))
