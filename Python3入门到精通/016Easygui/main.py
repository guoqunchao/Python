# -*- coding:utf-8 -*-

import easygui as g
import sys

while 1:
    g.msgbox("嗨，欢迎进入第一个界面小游戏")
    msg = "请问你希望再鱼C工作室学习到什么知识呢?"
    title = "小游戏互动"
    choices = ["谈恋爱","编程","OOXX","琴棋书画"]

    choce = g.choicebox(msg=msg, title=title, choices=choices)
    g.msgbox("你的选择是:" + str(choce),"结果")

    msg = "你希望重新开始小游戏吗？"
    title = "请选择"

    if g.ccbox(msg,title):
        pass
    else:
        sys.exit()