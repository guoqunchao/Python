# -*- coding:utf-8 -*-

class Turtle: #Python中的类名约定以大写开头
    '''关于类的一个简单例子'''
    # 属性
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'

    # 方法
    def climb(self):
        print("我正在很努力的向前爬...")

    def run(self):
        print("我正在飞快的向前跑...")

    def bite(self):
        print("咬死你咬死你...")

    def eat(self):
        print("有得吃,真满足...")

    def sleep(self):
        print("困了，睡了，晚安")

tt = Turtle()
tt.color
tt.bite()

print('\n===========================================')

class A():
    def fun(self):
        print("我是小A...")
    
class B():
    def fun(self):
        print("我是小B...")

a = A()
b = B()

a.fun()
b.fun()