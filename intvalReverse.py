#!/usr/bin/python3
#-*-coding:utf-8 -*-

'''
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
'''

class Solution:
	def reverse(self,x):
		"""
		:type x: int
		:rtype: int
		"""
		'''
		#解法一：负数不满足
		rev = 0
		while x:
			pop = x % 10
			x = x // 10
			rev = rev * 10 + pop
		return rev
		'''

		#解法二
		if -10 < x < 10:
			return x
		str_x = str(x)
		if str_x[0] != '-':
			str_x = str_x[::-1]
			x = int(str_x)
		else:
			str_x = str_x[1:][::-1]
			x = int(str_x)
			x = -x
		return x if -2147483648 < x < 2147483647 else 0



if __name__ == '__main__':
	x = -123
	solution = Solution()
	rev = solution.reverse(x)
	print(rev)