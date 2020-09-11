#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 两个队列实现一个栈.py
@time: 2020/02/18

"""

'''
用两个队列实现一个栈
'''

class Solution:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, node):
        self.queue1.append(node)

    def pop(self):
        # 若栈为空，则返回None值
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            return None
        else:
            if len(self.queue1) != 0:
                while len(self.queue1) > 1:
                    a = self.queue1.pop(0)
                    self.queue2.append(a)
                return  self.queue1.pop(0)
            else:
                while len(self.queue2) > 1:
                    a = self.queue2.pop(0)
                    self.queue1.append(a)
                return  self.queue2.pop(0)


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