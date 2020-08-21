# -*_ coding:utf-8 -*-

import time as t

class MyTimer():
    def __init__(self):
        self.prompt = "未开始计时"
        self.lasted = []
        self.begin = 0
        self.end = 0
        self.unit = ["年","月","日","时","分","秒"]

    # 开始计时
    def start(self):
        self.begin = t.localtime()
        print("计时开始...")

    # 停止计时
    def stop(self):
        self.end = t.localtime()
        self._calc()
        print("计时结束！")

    # 内部方法 计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])

        print(self.prompt)

t1 = MyTimer()
t1.start()
t.sleep(61)
t1.stop()