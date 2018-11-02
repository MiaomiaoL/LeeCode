#!/usr/bin/python3
#-*-coding:utf-8 -*-

'''

给定一个字符串，找出不含有重复字符的最长子串的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 无重复字符的最长子串是 "abc"，其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 无重复字符的最长子串是 "b"，其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 无重复字符的最长子串是 "wke"，其长度为 3。
     请注意，答案必须是一个子串，"pwke" 是一个子序列 而不是子串。

思路：

'''

class Solution:
	def lengthOfLongestSubstring(self,s):
		"""
		:param s: str
		:return: int
		"""
		d = {}
		l = 0
		start = 0

		for i in range(len(s)):
			cur = s[i]
			if cur not in d:
				d[cur] = i
			else:
				if d[cur] + 1 > start:
					start = d[cur] + 1
				d[cur] = i
			if i - start + 1 > l:
				l = i - start + 1
		print(start,l)
		return l
	def findLongestNoRepeatSubstr(self,s):
		import operator
		res_list = []
		length = len(s)
		for i in range(length):
			tmp = s[i]
			for j in range(i+1,length):
				if s[j] not in tmp:
					tmp += s[j]
				else:
					break
			res_list.append(tmp)
		res_list.sort(key = lambda x:(len(x)))
		return res_list[-1]

if __name__ == '__main__':
	str = 'abdfkjkgdok'
	solution = Solution()
	maxlen = solution.lengthOfLongestSubstring(str)
	maxstr = solution.findLongestNoRepeatSubstr(str)
	print('长度：{0},最长字串：{1}'.format(maxlen,maxstr))