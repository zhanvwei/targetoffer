#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 左旋转字符串.py
@time: 2020/04/15

"""
"""
题目：
字符串的左旋转操作是吧字符串前面的若干个字符转移到字符串的尾部。
定义一个函数实现该操作，如输入字符串"abcdefg"和数字2，该函数
将返回左旋转两位得到的结果"cdefgab"。
"""

class Solution:
    # 将字符串分为两部分：strs[:n]和strs[n:]
    # 先分别对strs[:n]和strs[n:]翻转
    # 再对整个字符串进行翻转
    def leftRotateString(self, strs, n):
        # write code here
        if strs is None or len(strs) <= 0:
            return ''
        strs_list = list(strs)
        length = len(strs_list)
        strs_list = self.reverse(strs_list, 0, n-1)
        strs_list = self.reverse(strs_list, n, length - 1)
        strs_list = self.reverse(strs_list, 0, length - 1)
        return ''.join(strs_list)

    def reverse(self, strs, start, end):
        # write code here
        if strs is None or len(strs) <= 0:
            return ''
        while start < end:
            strs[start], strs[end] = strs[end], strs[start]
            end -= 1
            start += 1
        return strs

if __name__ == "__main__":
    s = Solution()
    strs = 'abcdefg'
    print(s.leftRotateString(strs, 2))


