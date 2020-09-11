#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 字符串的排列.py
@time: 2020/03/22

"""

'''
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
结果请按字母顺序输出。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''


class Solution:
    # 字符串的排列
    def permutation(self, ss):
        # write code here
        if ss is None:
            return  []
        if len(ss) == 1:
            return  [ss]
        result = []
        for i in range(len(ss)):
            # 固定好一个元素，对其余元素递归做排列
            rest_lst = ss[:i] + ss[i+1:]
            permaut_lst = self.permutation(rest_lst)
            # 保存排列好的元素
            temp = []
            for x in permaut_lst:
                # 将前面固定好的元素i与递归排列好的结果进行排列组合
                temp.append(ss[i: i+1] + x)
            result += temp
        return result

    # 字符串的组合
    def group(self, ss):
        # wirte code here
        ss = list(set(ss))
        if len(ss) == 0:
            return []
        # 递归的边界
        if len(ss) == 1:
            return [ss]
        result = []
        for i in range(len(ss)):
            # 固定第i个元素，将剩下的[i+1:]的元素进行组合
            result.append(ss[i: i+1])
            groups = self.group(ss[i+1:])
            for j in groups:
                # 将固定的第i个元素与[i+1:]的组合结果再进行组合
                result.append(ss[i: i+1] + j)
        return  result












if __name__ == "__main__":
    lists = [1, 2, 3]
    s = Solution()
    result = s.permutation(lists)
    gresult = s.group(lists)
    print(result)
    print(gresult)