# -*- coding:utf-8 -*-

class Ball():
    def setName(self,name):
        self.name = name
    def kick(self):
        print("我叫%s, 该死的，谁踢我..." %self.name)

a = Ball()
a.setName("a")
a.kick()
