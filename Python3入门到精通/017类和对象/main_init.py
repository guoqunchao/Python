# -*- coding:utf-8 -*-

class Ball:
    def __init__(self,name):
        self.name = name

    def kick(self):
        print("我叫%s, 该死的，谁踢我..." %self.name)

a = Ball('a')
a.kick()



class Person:
    # name = "Hello Ketty"
    __name = "Hello Ketty"
    def getName(self):
        return self.__name

p = Person()
print(p.getName())
