#!/usr/bin/python3
#-*-coding:utf-8 -*-

'''
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''


class Solution:
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		'''
		#解法一：
		n = len(nums)

		for x in range(n):
			for y in range(x+1,n):
				if nums[y] == target - nums[x]:
					return x,y
				else:
					continue


		#解法二：
		n = len(nums)
		for x in range(n):
			tmp = target - nums[x]

			if tmp in nums:
				y = nums.index(tmp)
				if x == y:
					continue
				else:
					return x,y
			else:
				continue
		'''

		# 解法三：
		n = len(nums)
		d = {}
		for x in range(n):
			a = target - nums[x]
			if nums[x] in d:
				return d[nums[x]], x
			else:
				d[a] = x

if __name__ == '__main__':
	nums = [5,1,4,8,3]
	target = 9
	solution = Solution()
	x,y = solution.twoSum(nums,target)
	print("x：{0} \t y：{1}".format(x,y))
