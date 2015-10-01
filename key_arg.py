#!/usr/bin/env python3
def person(name, age, **kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	print('name', name, 'age', age, 'other', kw)

person('Mick', 30)
person('Jack', 40, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
extra = {'city':'上海', 'job':'程序猿'}
person('Tiger', 29, **extra)
person('Rose', 90, city='NewYork', addr='天堂', zipcode=12345)

def person(name, age, *, city, job):
	print(name, age, city, job)

person("jack", 24, city='Beijing', job="assistance")
