#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 替换空格.py
@time: 2020/02/12

"""

"""
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""

class Solution:
    """双指针"""
    def replaceSpace1(self, string):
        if not isinstance(string, str) or len(string) <= 0 or string == None:
            return  ""
        space_num = 0
        for i in string:
            if i == ' ':
                space_num += 1

        ## 每替换一个空格，长度需要增加2
        new_string_len = len(string) + 2*space_num
        new_string = new_string_len*[None]
        new_index, original_index = new_string_len - 1, len(string) - 1
        while original_index >= 0 and new_index >= original_index:
            if string[original_index] == " ":
                new_string[new_index-2: new_index+1] = ['%', '2', '0']
                original_index -= 1
                new_index -= 3
            else:
                new_string[new_index] = string[original_index]
                new_index -= 1
                original_index -= 1
        return  new_string




if __name__ == "__main__":
    s = 'we are happy'
    ss = Solution()
    new_string = ss.replaceSpace1(s)
    print(new_string)



