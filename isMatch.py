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

题目：44、通配符匹配  is_Match
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输入: false
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

	def is_Match(self, s: str, p: str) -> bool:
		l = []
		for i in range(len(p) + 1):
			l.append([0] * (len(s) + 1))
		l[0][0] = 1
		for a in range(1, len(p) + 1):
			if p[a - 1] == '*': l[a][0] = l[a - 1][0]
			for b in range(1, len(s) + 1):
				if p[a - 1] == '*':

					l[a][b] = l[a - 1][b] or l[a][b - 1]
				elif p[a - 1] == '?' or p[a - 1] == s[b - 1]:
					l[a][b] = l[a - 1][b - 1]
				else:
					l[a][b] = 0
		return l[-1][-1] != 0

if __name__ == '__main__':
	s = Solution()

	# print(s.isMatch("aa", "a"))  # false
	# print(s.isMatch("aa", "aa"))  # true
	# print(s.isMatch("aaa", "aa"))  # false
	# print(s.isMatch("aa", "a*"))  # true
	# print(s.isMatch("aa", ".*"))  # true
	# print(s.isMatch("ab", ".*"))  # true
	# print(s.isMatch("aab", "c*a*b"))  # true
	print(s.is_Match("aa", ".*c"))