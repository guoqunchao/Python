# -*- coding:utf-8 -*-

import random as r

class Fish():
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print("我现在的位置是：",self.x,self.y)

class GoldFish(Fish):
    pass

class Salmon(Fish):
    pass

class Carp(Fish):
    pass

class Shark(Fish):
    # 子类会覆盖父类的方法 
    def __init__(self): 
        Fish.__init__(self) # 方法1
        # super().__init__() # 方法2
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天吃...")
            self.hungry = False
        else:
            print("太撑了，吃不下了！")

g = GoldFish()
g.move()

s = Salmon()
s.move()

c = Carp()
c.move()

s = Shark()
s.move()
s.eat()