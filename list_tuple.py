#!/usr/bin/env python3
L = [
	['Apple', 'Google', 'Microsoft'],
	['Java', 'Python', 'Ruby', 'PHP'],
	['Adam', 'Bart', 'Lisa']
    ]
print(L)
# 打印Apple:

print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

#下面是条件判断的代码
age = 6
if age >= 18:
	print('Your age is', age)
	print('adult')
elif age >= 6:
	print('teenager')
else:
	print('Kid')

birth = int(input('bith:'))
if birth < 2000:
	print('00前')
else:
	print('00后')
