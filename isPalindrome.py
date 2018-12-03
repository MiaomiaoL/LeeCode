#!/usr/bin/python3
#-*-coding:utf-8 -*-

class Solution:
	def isPalindrome(self,x):
		"""
		:param x: int
		:return: bool
		"""

		if str(x) == str(x)[::-1]:
			return True
		else:
			return False

if __name__ == "__main__":
	x = 121
	solution = Solution()
	ispalindrome = solution.isPalindrome(x)
	print(ispalindrome)