#下面是第一道练习题目
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def transfer(s):
	buf = s[0].upper()
	for c in s[1:]:
		buf += c.lower()
	return buf
#str = 'JACK'
#print(transfer(str))
		
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(transfer, L1))
print(L2)

#下面是第二道练习题目
#Python提供的sum()函数可以接受一个list并求和
#请编写一个prod()函数，可以接受一个list并利用reduce()求积
from functools import reduce
def prod(L):
    def mul(x, y):
        return x * y
    return reduce(mul, L)

L = [3, 5, 7, 9]
print('3 * 5 * 7 * 9 = ', prod(L))

#下面是第三道习题
#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456

#from functools import reduce
def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    def multipy(x, y):
        return x * 10 + y
    s0 = s.split('.') #按照分隔符将s分隔开来
    s1 = s0[0]
    s2 = s0[1]
    length = len(s2)
    return reduce(multipy, map(char2num, s1)) + reduce(multipy, map(char2num, s2))/ (10**length)
print('str2float(\'123.456\') =', str2float('123.456'))

    
