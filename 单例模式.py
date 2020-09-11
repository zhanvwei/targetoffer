#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:zhangxiaowei
@file: 单例模式.py
@time: 2020/02/11

"""
"""
单例模式：就是保证一个类有且只有一个实例对象。

"""
#重写__new__和__init__方法
class Singleton1(object):
    """单例模式的实现方式一"""
    __instance = None
    __isFirstInit = False

    def __new__(cls, name):
        if not cls.__instance:
            Singleton1.__instance = super().__new__(cls)
        return  cls.__instance

    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            Singleton1.__isFirstInit = True

    def getName(self):
        return  self.__name




##自定义metaclass
class Singleton2(type):
    """单例实现方式二"""
    def __init__(self, what, bases = None, dict = None):
        super().__init__(what, bases, dict)
        cls._instance = None #初始化全局变量cls._instance为None

    def __call__(cls, *args, **kwargs):
        # 控制对象的创建过程，如果cls._instance为None, 则创建，否则直接返回
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return  cls._instance

class CustomClass(metaclass= Singleton2):
    """用户自定义的类"""
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return  self.__name



if __name__ == "__main__":
    tony = Singleton1("Tony")
    karry = Singleton1("Karry")
    print(tony.getName(), karry.getName())
    print("id(tony): ", id(tony), "  id(karry): ", id(karry))
    print("tony == karry: ", tony == karry)