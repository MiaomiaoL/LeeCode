#!/usr/bin/python3
#-*-coding:utf-8 -*-

'''
题目：10、正则表达式匹配  isMatch
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: '*' 代表可匹配零个或多个前面的元素, 即可以匹配 'a' 。因此, 重复 'a' 一次, 字符串可变为 "aa"。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个('*')任意字符('.')。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 'c' 可以不被重复, 'a' 可以被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
'''

class Solution:
	def isMatch(self,s,p):
		"""
		:param s: str
		:param p: str
		:return: bool
		"""
		print(s,p)
		if p == '':
			print(1)
			return s == ''
		if len(p) > 1 and p[1] == '*':
			print(2)
			return self.isMatch(s,p[2:]) or (s != '' and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:],p))
		else:
			print(3)
			return s !='' and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:],p[1:])

if __name__ == '__main__':
	s = Solution()

	# print(s.isMatch("aa", "a"))  # false
	# print(s.isMatch("aa", "aa"))  # true
	# print(s.isMatch("aaa", "aa"))  # false
	# print(s.isMatch("aa", "a*"))  # true
	# print(s.isMatch("aa", ".*"))  # true
	# print(s.isMatch("ab", ".*"))  # true
	# print(s.isMatch("aab", "c*a*b"))  # true
	print(s.isMatch("aa", ".*c"))