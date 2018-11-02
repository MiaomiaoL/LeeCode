#!/usr/bin/python3
#-*-coding:utf-8 -*-

'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。

请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

你可以假设 nums1 和 nums2 不同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5
'''

class Solution:
	def findMedianSortedArray(self,nums1,nums2):
		"""
		:param nums1: List[int]
		:param nums2: List[int]
		:return: float
		"""
		nums = []
		while len(nums1) != 0 and len(nums2) != 0:
			if nums1[0] < nums2[0]:
				nums.append(nums1.pop(0))
			else:
				nums.append(nums2.pop(0))
		if len(nums1) != 0:
			nums += nums1
		else:
			nums += nums2

		if len(nums) % 2 == 0:
			tmp = len(nums) // 2
			res = (nums[tmp] + nums[tmp -1]) / 2
		else:
			res = nums[len(nums) // 2]
		return float(res)

if __name__ == '__main__':
	nums1 = [1,2]
	nums2 = [3,4]
	solution = Solution()
	print(nums1,nums2)
	res = solution.findMedianSortedArray(nums1,nums2)
	print(nums1,nums2,res)  # python 传递参数肯定是传'对象引用'的方式