#!/usr/bin/env python3
d = {'a' : 1, 'b' : 2, 'c' : 3}
for key in d:
	print(key)
#python的迭代条件放的真是宽泛，也就是说更加的抽象
#迭代key和value
for key, value in d.items():
	print(key, ' ', value)
#迭代值
for value in d.values():
	print(value)

#下面的代码是判断一个对象是否可以迭代
from collections import Iterable
print(isinstance('abc', Iterable))#str是否可以迭代
print(isinstance([1, 2, 3], Iterable))#list是否可以迭代
print(isinstance(123, Iterable))#整数是否可以迭代

#enumerate函数可以将一个list变为索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)
#for循环中使用两个变量是很平常的


