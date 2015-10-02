#!usr/bin/env python3
#求绝对值的函数
abs(-10)

x = abs(20)

f = abs
#f现在是函数了
print(f)
#结论：函数本身也可以赋值给变量，即变量可以指向函数
print(f(-10))

abs = 10
#下面的函数无法调用，因为abs现在已经指向10了
abs(-10)

#传入函数
def add(x, y, f):
	return f(x) + f(y)

#x = -5
#y = 6
#f = abs
add(-5, 6, abs)

#总结：将函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式


