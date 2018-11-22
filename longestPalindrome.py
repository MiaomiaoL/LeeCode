#!/usr/bin/python3
#-*-coding:utf-8 -*-

'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''

class Solution:
	def longestPalindrome(self,s):
		"""
		:param s: str
		:return: str
		"""
		'''
		#解法一
		l = len(s)
		max_length = 0
		palindromic = ''
		if l <= 1:
			return s
		for i in range(l):
			for j in range(i + 1,l):
				is_palindromic = True
				for k in range(i,int((i + j) / 2) + 1):
					if s[k] != s[j - k + i]:
						is_palindromic = False
						break
				if is_palindromic and (j - i + 1) > max_length:
					max_length = j - i + 1
					palindromic = s[i:j + 1]
		if palindromic == '':
			palindromic = s[0]
		return palindromic
		
		#解法二
		l = len(s)
		if l <= 1:
			return s
		max_length = 0
		palindromic = ''
		for i in range(l):
			x = 1 # 奇数长度回文字串
			while (i - x) >= 0 and (i + x) < l:
				if s[i + x] == s[i - x]:
					x += 1
				else:
					break
			x -= 1
			if 2 * x + 1 > max_length:
				max_length = 2 * x + 1
				palindromic = s[i - x: i + x + 1]
			x = 0 # 偶数长度回文子串
			if (i + 1) < l:
				while (i - x) >= 0 and (i + 1 + x) < l:
					if s[i + 1 + x] == s[i - x]:
						x += 1
					else:
						break
			x -= 1
			if 2 * x + 2 > max_length:
				max_length = 2 * x + 2
				palindromic = s[i - x: i + x + 2]
		if palindromic == '':
			palindromic = s[0]
		return palindromic
		'''
		#解法三
		str = '#' + '#'.join(s) + '#'
		l = len(str)
		f = []
		maxj = 0
		maxl = 0
		maxd = 0
		for i in range(l):
			if maxl > i:
				count = min(maxl-i,int(f[2*maxj-i]/2+1))
			else:
				count = 1
			while i-count >= 0 and i+count < l and str[i-count] == str[i+count]:
				count += 1
			if (i-1+count) > maxl:
				maxl,maxj = i-1+count,i
			f.append(count*2-1)
			maxd = max(maxd,f[i])
		return int((maxd+1)/2)-1


if __name__ == '__main__':
	s = 'abba'
	solution = Solution()

	palindromic = solution.longestPalindrome(s)
	print(palindromic)
