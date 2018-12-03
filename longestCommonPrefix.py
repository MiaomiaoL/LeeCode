#!/usr/bin/python3
#-*-coding:utf-8 -*-

'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
'''

class Solution:
	def LongestCommonPreFix(self,strs):
		"""
		:param strs:  List[str]
		:return: str
		"""
		# #解法一：
		# if not strs:
		# 	return ""
		# if len(strs) == 1:
		# 	return strs[0]
		# minl = min([len(x) for x in strs])
		# end = 0
		# while end < minl:
		# 	for i in range(1,len(strs)):
		# 		if strs[i][end] != strs[i-1][end]:
		# 			return strs[0][:end]
		# 	end += 1
		# return strs[0][:end]

		#解法二：
		res = ""
		# if len(strs) == 0:
		# 	return ""
		for each in zip(*strs):
			if len(set(each)) == 1:
				res += each[0]
			else:
				return res
		return res

if __name__ == '__main__':
	s = Solution()

	print(s.LongestCommonPreFix([]))

