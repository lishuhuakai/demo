#!/usr/bin/env python3
print(sorted([36, 5, -12, 9, -21]))
print(sorted([35, 5, -12, 9, -21], key = abs))
#key指定的函数将会按照keys进行排序，并按照对应关系返回list相应的元素
#list = [36, 5, -12, 9, -21]
#keys = [36, 5, 12, 9, 21]

print(sorted(['bob', 'about', 'zoo', 'Credit'], key = str.lower))

print(sorted(['bob', 'about', 'zoo', 'Credit'], key = str.upper, reverse = True))

#练习题目
#假设我们用一组tuple表示学生名字和成绩：
#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def com(x):
    return x[0]
    
print(sorted(L, key = com))
def by_score(t):
    return t[1]
print(sorted(L, key = by_score))


