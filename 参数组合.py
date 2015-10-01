#!/usr/bin/env python3
def f1(a, b, c=0, *args, **kw):
	print('a = ', a, 'b = ', b, 'c = ', c, 'args = ', args, 'kw = ', kw)
def f2(a, b, c=0, * d, **kw):
	print('a = ', a, 'b = ', b, 'c = ', c, 'd = ', d,'kw = ', kw)

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, 3, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d':99, 'x':'#'}
f1(*args, **kw)

kw = {'d':88, 'x':'#'}
f2(*args, **kw)
