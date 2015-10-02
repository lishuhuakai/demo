#!/usr/bin/env python3
from collections import Iterable
isinstance([], Iterable)
isinstance({}, Iterable)
isinstance('abc', Iterable)
isinstance((x for x in range(10)), Iterable)
isinstance(100, Iterable)

#生成器都是Iterator，但是list，dict，str虽然是Iterable，却不是Iterator
#可以使用iter()函数将list，dict，str等Iterable变成Iterator
isinstance(iter([]), Iterable)
isinstance(iter('abc')， Iterable)

#总结：凡事可以作用于for循环的对象都是Iterable类型
#凡是可以作用与next()函数的对象都是Iterator类型，他们表示一个惰性计算的序列
#集合数据类型如list，dict，str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
for x in [1, 2, 3, 4, 5]:
    pass
#等价于
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        #获得下一个值
        x = next(it)
    except StopIteration:
        #遇到StopIteration就退出循环
        break
