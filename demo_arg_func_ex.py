#!/usr/bin/env python3
def mypower(x):
	return x * x

print(mypower(9))

def mypower(x, n):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s


print(mypower(9, 6))
#在这边调用mypower(6)的话会出现错误
#print(mypower(6))

def add_end(L=None):
	if L is None:
		L = []
	L.append("END")
	return L

print(add_end())
print(add_end())

#下面使用的是可变参数
def calc(numbers):
	sum = 0
	for n in numbers:
		sum += n * n
	return sum

print(calc([1, 2, 3, 4, 5]))
print(calc((1, 2, 3, 4, 5)))

def calc_ex(a, b, c):
	return a + b + c

nums = [1, 2, 3]

print(calc_ex(*nums))

