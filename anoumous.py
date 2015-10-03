#!/usr/bin/env python3
#当我们在传入函数的时候，不需要显式地定义函数，直接传入匿名函数集客

#python提供了对匿名函数的有限支持
list(map(lambda x : x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
#lambda就是匿名函数，这可真令人吃惊啊
#这样看来，匿名函数lambda x : x * x实际上就是
def f(x):
    return x * x
#关键字lambda表示匿名函数，冒号前面的x表示函数参数
#匿名函数有一个限制，就是只能有一个表达式，不用写return
#此外匿名函数也是一个函数对象也可以将匿名函数赋值给一个变量，再利用变量来调用该函数

j = lambda x : x * x
print(j)
print(j(5))
#同样的，也可以将匿名函数作为返回值返回，如：
def build(x, y):
    return lambda: x * x + y * y

