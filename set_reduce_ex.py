#!usr/bin/env python3
#map and reduce
#map接收两个参数，一个是函数，另外一个是Iterable
def f(x):
	return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

#reduce函数，reduce把一个函数作用在一个序列[x1, x2......],这个函数必须接收两个参数，reduce将结果继续和序列的下一个元素做累计运算
#其效果是reduce(f, [x1, x2, x3, x4]) ==> f(f(f(x1, x2), x3), x4)

#下面是对一个序列求和
from functools import reduce
def add(x, y):
	retrun x + y
print(reduce(add, [1, 2, 3, 4, 5]))

#如果要把序列[1, 2, 3, 4, 5, 6]转换成为整数123456,可以这么干
from functools import reduce
def fn(x, y):
	return x * 10 + y
def char2num(s):
	return {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[s]

reduce(fn, map(char2num, '123456'))
#整理成为一个str2int的函数

def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[s]
	return reduce(fn, map(char2num, s))

 #还可以用lambda函数进一步简化
 def char2num(s):
 	return {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}[s]

 def str2int(s):
 	return reduce(lambda x, y :x * 10 + y, map(char2num, s))

