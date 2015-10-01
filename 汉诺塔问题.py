#!/usr/bin/env python3
def move(n, a, b, c):
#n表示a中含有的盘子的数目，我们的目的是借助盘子c将a中的盘子移动到b
#要求采用递归的算法来解决这个问题
#参数n，表示3个柱子a、b、c中第1个柱子a的盘子数量，然后打印出把所有盘子从a借助b移动到c的方法
	if n == 1:#递归终止条件
		print(a, '-->', c)
	else:
	#将a的前面的n-1个盘子借助c移动到b
		move(n - 1, a, c, b)
	#将最后一个盘子从a移动到c
		move(1, a, b, c)
	#将n-1个圆盘从b借助a移动c
		move(n - 1, b, a, c)
n = input('请输入A柱子上的圆盘的数目:')
move(int(n), 'A', 'B', 'C')

