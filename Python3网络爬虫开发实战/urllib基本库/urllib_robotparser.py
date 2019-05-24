__author__ = 'Inkwhite'

from urllib.robotparser import RobotFileParser
rp = RobotFileParser('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*','https://www.jianshu.com/p/b67554025d7d'))


# from urllib.request import urlopen
#
# rp1 = RobotFileParser()
# rp1.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
# print(rp1.can_fetch('*','https://www.jianshu.com/p/b67554025d7d'))