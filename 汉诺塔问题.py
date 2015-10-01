#!/usr/bin/env python3
def move(n, a, b, c):
#n表示A中含有的盘子的数目，我们的目的是借助盘子C将A中的盘子移动到B
#要求采用递归的算法来解决这个问题
#参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，
#我自己来尝试写一下递归的算法
	if n == 1:
		print(a, '-->', c)
	#将a的前面的n-1个盘子借助c移动到b
	else:
		move(n - 1, a, c, b)
		move(1, a, b, c)
		move(n - 1, b, a, c)
	#将最后一个盘子从a移动到c

move(3, 'A', 'B', 'C')

