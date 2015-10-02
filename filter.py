#filter用于过滤序列
#filter函数的主要作用是根据函数判断一个序列中的元素是否留下
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', ' ', 'B', None, 'C', ' '])))

#filter求素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x : x % n > 0
#定义一个生成器，不断返回下一个素数:
def primes():
    yield 2
    it = _odd_iter() #初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break

def is_palindrome(n):
    #关键在于判断一个数是不是回数
    s = str(n)
    #print('s = ', s)
    mid = len(s) // 2
    #print('mid = ', mid)
    s1 = s[:mid]
    #print('s1 = ',s1)
    s2 = s[-1:-mid-1:-1]
    #print('s2 = ', s2)
    return s1 == s2
output = filter(is_palindrome, range(1, 1000))
print(list(output))


        
