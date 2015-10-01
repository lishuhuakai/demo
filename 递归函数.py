#!/usr/bin/env python3

#定义阶乘的运算
def fact(n):
	if n==1:
		return 1
	return n * fact(n - 1)

print(fact(100))

#下面采用尾递归的方式来处理递归
def fact_ex(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num -1, num * product)
print(fact_ex(1000))
