#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 翻转字符串.py
@time: 2020/04/15

"""

'''
输入一个英文句子, 翻转句子中单词的顺序,但单词内字符的顺序不变
为简单起见, 标点符号和普通字母一样处理
'''

class Solution:
    """
    step1:先翻转整个句子
    step2:再翻转单个单词
    """
    def reverseSetence(self, setence):
        # write code here
        if setence is None or len(setence) <= 0:
            return ''
        list_setence = list(setence)
        # 先将整个句子翻转
        reverse_setence = self.reverse(list_setence)

        print(reverse_setence)

        begin = 0
        # 因为Python的字符串结束没有结束符, 所以需要判断最后的end是否已经指到最后一个字符
        end = 0
        result = ''
        temp_list = []
        # 翻转句子中的每个单词
        while end < len(setence):
            # 若遍历到字符结尾，则翻转到最后一个单词后直接跳出
            if end == len(setence) - 1:
                temp_list.append(self.reverse(reverse_setence[begin:]))
                break
            # 若遍历到空格，则end和begin都要右移跳过空格，并将空格添加到temp_list
            if reverse_setence[begin] == " ":
                begin += 1
                end += 1
                temp_list.append(' ')
            elif reverse_setence[end] == " ":
                # 若遍历到单词分隔符（空格），则翻转该单词，同时将begin移动到end位置
                temp_list.append(self.reverse(reverse_setence[begin: end]))
                begin = end
            else:
                end += 1

        for i in temp_list:
            result += ''.join(i)
        return result



    # 翻转链表
    def reverse(self, alist):
        # write code here
        if alist is None or len(alist) <= 0:
            return  ''
        start = 0
        end = len(alist) - 1
        while start < end:
            alist[start], alist[end] = alist[end], alist[start]
            start += 1
            end -= 1
        return alist

    def reverse2(self, s):
        # write code
        l = s.split(' ')
        return ' '.join(l[::-1])




if __name__ == "__main__":
    setence = 'I am a student.'
    s = Solution()
    print(s.reverseSetence(setence))



