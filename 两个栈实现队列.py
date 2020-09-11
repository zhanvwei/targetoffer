#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 两个栈实现队列.py
@time: 2020/02/17

"""
'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        ## 当stack1和stack2没有元素时，返回空
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return  None
        ## 当stack2为空，而stack1不为空的时候，
        # 则先将stack1的元素添加到stack2中
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                a = self.stack1.pop()
                self.stack2.append(a)
        return  self.stack2.pop()


if __name__ == "__main__":
    P = Solution()
    P.push(10)
    P.push(11)
    P.push(12)
    print(P.pop())
    P.push(13)
    print(P.pop())
    print(P.pop())
    print(P.pop())
    print(P.pop())
