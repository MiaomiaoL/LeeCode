#!/usr/bin/python3
#-*-coding:utf-8 -*-

'''
题目：16、最接近的三数之和  threeSumClosest
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mindiff = 10000
        nums.sort()
        res = 0
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                diff = abs(target - sum)
                if diff < mindiff:
                    mindiff = diff
                    res = sum
                if target == sum:
                    return sum
                elif sum < target:
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1,2,1,-4],1))