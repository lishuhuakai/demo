#!/usr/bin/env python3
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

#上面的数组对应的dict如下
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])

#change the value of d['Bob']
d['Bob'] = 92
print(d['Bob'])

if 'Tracy' in d:
	print(d['Tracy'])
#delete the key bob
d.pop('Bob')
print(d)


