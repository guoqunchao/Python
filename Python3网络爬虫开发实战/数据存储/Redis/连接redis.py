# -*- coding: UTF-8 -*-

__author__ = 'Ink.White'

from redis import StrictRedis

redis = StrictRedis(host='localhost',port=6379,password='123456',db=0)
redis.set('name','Bob')
print(redis.get('name'))
print(redis.exists('name'))
print(redis.dbsize())