#!/usr/bin/env python3

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('参数的类型错误')
	if x >= 0:
		return x
	else:
		return -x

def nop():
	pass

import math

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny
print(my_abs(-10))
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

#下面的例子说明了一个问题，那就是返回的值是一个tuple
#返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple
#按照位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但是写起来更加方便
r = move(100, 100, 60, math.pi / 6)
print(r)

#下面是本节的一个练习题目
#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

##ax2 + bx + c = 0

##的两个解。
def quadratic(a, b, c):
	if not isinstance(a, (int, float)):
		return
	if not isinstance(b, (int, float)):
		return
	if not isinstance(c, (int, float)):
		return
	n1 = b * b - 4 * a * c
	if n1 < 0:
		return
	else:
		n1 = math.sqrt(n1)
	r1 = (-b + n1) / (2 * a)
	r2 = (-b - n1) / (2 * a)
	return r1, r2

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
