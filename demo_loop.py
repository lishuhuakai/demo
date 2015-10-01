#!/usr/bin/env python3
names = ['Michael', 'Bob', 'Tracy']
for name in names:
	print(name)

#下面的代码用来计算1-10之间的整数的和
print('下面是for循环的演示')
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	sum = sum + x
print(sum)

list(range(5))

#利用range函数产生0 -- 100的序列
print("下面是range函数的演示")
sum = 0
for x in range(101):
	sum = sum + x
print(sum)

#while循环
print("下面while的演示")
sum = 0
n = 99
while n > 0:
	sum += n
	n = n -2
print(sum)

#请利用循环依次对list中的每个名字打印出 hello，xxx
L = ['Bart', 'Lisa', 'Adam']
for name in L:
	print('hello,', name)
