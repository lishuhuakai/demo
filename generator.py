#!/usr/bin/env python3
#下面使用genertor
#列表元素简介在循环的过程中不断推算出后续的元素
#创建一个generator，方法很多，第一种格式只要将一个列表生成式的[]变为()
L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#需要注意的是迭代器的范围不能越界
#上面的代码不太直观，正确的方法是使用for循环，generator也是可迭代的对象
#不信，你看
g = (x * x for x in range(10))
for n in g:
	print(n)
def fib(max):
	n, a, b = 0, 0, 1 #代码写出来真叫一个漂亮
	while n < max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'down'

#下面的函数调用可以输出斐波拉契数列的前N个数
fib(6)

#如果我们将fib函数变成generator，怎么办呢？
def fib_ex(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'
#如果哟个函数定义中包含了yield关键字，那么这个函数就再是一个普通函数，它是一个generator
f = fib(6)
print(f)

#generator和函数的执行流程不一样，函数是顺序执行，遇到return语句或者最后一行函数语句就返回，而变成了generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行的时候从上次返回的yield语句处继续执行

##一个简单的例子
def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield 3
	print('step 3')
	yield 5
o = odd()

print(next(o))
print(next(o))
print(next(o))

#练习题，输出杨辉三角
def triangles():
	P, C = [1], [1, 1] #开始的两个作为启动条件
	yield P
	yield C
	P = C
	while 1:
		index = 1
		size = len(P)
		while index < size:
			#print("index = ", index)
			C.insert(index, P[index - 1] + P[index])
			#print("C = ", C)
			index += 1;
		yield C
		P = C
		C = [1, 1]
		#print("P = ", P)

#然后调用函数
g = triangles()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
