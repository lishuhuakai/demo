#!/usr/bin/env python3
L = ('Michael', 'Jack', 'Hadoop')
print(L[0:3])
x  = ['Michael', 'Jack', 'Hadoop']
print(x[:3])
print(x[1:3])
print(x[-2:3])

J = list(range(100))
print(J)
print(J[:10])
print(J[-10:])
#前十个数，每两个数一取
print(J[:10:2])
#所有数，每五个一取
print(J[::5])
#什么都不写，只写[:]就可以原样复制一个list
print(J[:])
#tuple也是一种list，唯一的区别就是tuple不可变，tuple切片操作或任然是tuple
print((0, 1, 2, 3, 4, 5)[:3])
#字符串'xxx'也可以看成是一种list，每个元素就是一个字符，字符串也可以切片
#结果仍然是字符串
print('ABCDEFG'[:3])
print('ABCDEFG'[::3])

