# -*- coding:utf-8 -*-

class Base01:
    def foo01(self):
        print("我是foo01，我为Base01代言...")

class Base02:
    def foo02(self):
        print("我是foo02，我为Base02代言...")

class C(Base01,Base02):
    pass

c = C()
c.foo01()
c.foo02()