#!/usr/bin/env python3

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
        return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f)

print(f())

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
#运行的结果很令人吃惊，因为三个函数都返回了9
#原因在于返回的函数引用了变量i，但它并非立刻执行
#等到三个函数都返回的时候，它们所引用的变量已经变成了3，最终结果为9

def count_ex():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) #f(i)立刻被执行，因此i的当前值被传入f()
        return fs
k1, k2, k3 = count_ex()
print(f1())
print(f2())
print(f3())

