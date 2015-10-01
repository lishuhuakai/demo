#!/usr/bin/env python3

#构建一个set集合，并且输出set
#创建一个set，需要提供一个list作为输入的集合
s = set([1, 2, 3])
print(s)

#所谓的set可以过滤掉重复的元素
s = set([1, 1, 1, 2, 2, 3, 3, 3])
print(s)

s.add(4)
print(s)

s.remove(4)
print(s)

s1 = set([1, 2, 3])
s2 = set([3, 4, 5])
print(s1 & s2)#取两者的交集
print(s1 | s2)#取两者的合集


