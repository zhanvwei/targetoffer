#!usr/local/bin/python3
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 32之字形打印二叉树.py
@time: 2020/03/17

"""

'''
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 利用两个栈按奇数层和偶数层分别存储
    def zigzagPrint(self, root):
        if root is None:
            return []

        result, nodes = [], [root]
        right_to_left = True
        while nodes:
            # stack1用于保存读取结果，stack2用于保存下一层节点
            stack1, stack2 = [], []
            if right_to_left:
                # 奇数层的时候，stack2从左往右保存下一层的节点
                for node in nodes:
                    stack1.append(node.val)
                    if node.left:
                        stack2.append(node.left)
                    if node.right:
                        stack2.append(node.right)
            else:
                # 偶数层的时候，stack2从右往左保存下一层节点
                for node in nodes:
                    stack1.append(node.val)
                    if node.right:
                        stack2.append(node.right)
                    if node.left:
                        stack2.append(node.left)
            stack2.reverse()
            nodes = stack2
            right_to_left = not right_to_left
            result.append(stack1)
        return result


    ## 列表
    def zigzagPrint2(self, root):
        # write code here
        if root is None:
            return []
        result, nodes = [], [root]
        is_enven = True
        while nodes:
            stack1 = []
            stack2 = []
            is_enven = not is_enven
            for node in nodes:
                # 获取每一层节点时，若是偶数层则将每个节点的值插入到列表的前面
                if is_enven:
                    stack1.insert(0, node.val)
                else:
                    # 获取每一层节点时，若是奇数层则将每个节点的值添加到列表后面
                    stack1.append(node.val)

                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
            nodes = stack2
            result.append(stack1)
        return result



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
    result = S.zigzagPrint(pNode1)
    print(result)
    print(S.zigzagPrint2(pNode1))