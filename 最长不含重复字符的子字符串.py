#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 最长不含重复字符的子字符串.py
@time: 2020/04/06

"""
"""
题目：请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
假设字符串中只包含'a'~'z'的字符串。例如，在字符串"arabcacfr"中，最长的不含重复
字符的子字符串是"acfr"，长度为4。
"""

class Solution:
    # 滑窗法1
    def longestSubstringWithoutDuplication1(self, string):
        # write code here

        if string is None:
            return 0
        queue = []
        max_length = 0
        current_length = 0
        for s in string:
            current_length += 1
            while s in queue:
                current_length -= 1
                queue.pop(0)
            queue.append(s)
            max_length = max(max_length, current_length)
        return  max_length

    # 滑窗法2
    def longestSubstringWithoutDuplication2(self, string):
        # write code here
        if string is None:
            return 0
        length = len(string)
        l_index = 0
        dicts = dict()
        max_length = 0
        for i in range(length):
            s = string[i]
            if s in dicts.keys():
                l_index = max(l_index, dicts.get(s)) + 1
            max_length = max(max_length, i - l_index + 1)
            dicts[s] = i
        return max_length


    """
    动态规划：用f(i)表示以第i个字符结尾的不包含重复字符的子字符串的最长长度。
            当第i个字符之前没有出现过，那么计算f(i) = f(i-1) + 1,
            当第i个字符在之前已经出现过，则计算第i个字符和它上次出现在字符串中位置的距离d:
            当d <= f(i-1)时，表明第i个字符出现在f(i-1)对应的最长子字符串中，此时f(i) = d;
            当d > f(i-1)时，表明第i个字符未出现在f(i-1)对应的最长子字符串中，此时f(i) = f(i-1) + 1。
                
    """
    def longestSubstringWithoutDuplication3(self, string):
        # write code here
        if string is None:
            return  0
        length = len(string)
        # 保存字符出现的位置
        dicts = dict()
        max_length = 0
        current_length = 0
        for i in range(length):
            s = string[i]
            # d = i - dicts[s]
            if s not in dicts.keys() or current_length < i - dicts[s]:
                current_length += 1
            else:
                current_length = i - dicts[s]
            dicts[s] = i
            max_length = max(max_length, current_length)
        return max_length




if __name__ == "__main__":
    s = Solution()
    string = "arabcacfr"
    print(s.longestSubstringWithoutDuplication1(string))
    print(s.longestSubstringWithoutDuplication2(string))
    print(s.longestSubstringWithoutDuplication3(string))

