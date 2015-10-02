#!/usr/bin/env python3
print(list(range(1, 11)))
#生成[1*1, 2*2,...,10*10],怎么办？
L = []
for x in range(1, 11):
	L.append(x * x)
print(L)
#更好的方法
print([x * x for x in range(1, 11)])
#上面即是所谓的列表生成式
#下面是更近一步的例子，for循环后面可以添加if判断，筛选出仅偶数的平方
print([x * x for x in range(1, 11) if x % 2 == 0])
#还可以使用两层循环，生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])

#运用列表生成式可以写出非常简介的代码
#下面是列出当前目录下所有的文件和文件名
import os
print([d for d in os.listdir('.')])

#for循环其实可以同时使用两个甚至多个变量，比如dict的itetms可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
	print(k, '=', v)
#列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v, in d.items()])

#最后将一个list中所有的字符串变为小写
L = ['Hello', "world", 'IBM', 'Apple']
print([s.lower() for s in L])

#最后是一道练习题目
L = ['Hello', "world", 10, 'IBM', 'Apple']
print([s.lower() for s in L if isinstance(s, str)])


