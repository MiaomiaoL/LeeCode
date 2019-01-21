#!/usr/bin/python3
#-*-coding:utf-8 -*-

'''
题目：6、Z字形变换  convert
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
'''

class Solution:
	def convert(self,s,numRows):
		"""
		:param s: str
		:param numRows: int
		:return: str
		"""
		if numRows == 1:
			return s
		ans = ''
		interval = 2 * numRows - 2
		ans += s[::interval]
		for i in range(1,numRows-1):
			innergap = interval - 2 * i
			j = i
			while j < len(s) - interval:
				ans += (s[j] + s[j + innergap])
				j += interval
			if j < len(s):
				ans += s[j]
			if j + innergap < len(s):
				ans += s[j + innergap]
		ans += s[numRows-1::interval]
		return ans


if __name__ == '__main__':
	s = '123456789'
	numRows = 3
	solution = Solution()

	ans = solution.convert(s,numRows)
	print(ans)