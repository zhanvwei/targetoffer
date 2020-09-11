#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: test01.py
@time: 2020/02/24

"""

def groupSum(start, nums, target):
    if start >= len(nums):
        print(start, target)
        return  target == 0
    else:
        return  groupSum(start + 1, nums, target - nums[start]) or\
            groupSum(start + 1, nums, target)



## 排列组合
def perm(list_var):
    if len(list_var) == 1:
        return  [list_var]
    result = []
    for i in range(len(list_var)):
        rest_list = list_var[:i] + list_var[i+1:]
        per_result = perm(rest_list)
        lists = []
        for x in per_result:
            lists.append(list_var[i:i+1] + x)
        result += lists
    return  result



def main():
    #print(groupSum(0, [1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
    print(perm([1, 2, 3]))




print(perm([1, 2, 3]))


