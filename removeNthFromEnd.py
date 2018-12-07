#!/usr/bin/python3
#-*-coding:utf-8 -*-

'''
题目：删除链表倒数第n个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
复制代码说明：
给定的 n 保证是有效的。
进阶：
你能尝试使用一趟扫描实现吗？
题目解析：
如果不考虑进阶的要求的话，是一道很简单的题目。只需要找出要删除的节点的位置，然后进行删除操作就可以了。
需要做题者熟悉链表结构和链表的遍历。
思路
思路一：
不考虑进阶中的只遍历一次的要求，很简单。先完整遍历一次链表，得出链表长度，然后根据题目给出的n，就可以知道需要删除的节点的位置。再次从头遍历链表就可以进行操作得出结果。
思路二：
快慢指针。快指针一次走两步，慢指针一次走一步。两个指针同时出发，当快指针走到表尾时，慢指针刚好走到中间的位置（链表长度奇数的话慢指针刚好在中间，偶数的话在中间往后一个位置）。此时可以根据链表的长度和题目给出的n得出要删除的节点的位置。如果在慢指针之前，则从头开始遍历。如果在慢指针之后，则从慢指针位置向后遍历。这样可以实现一次扫描得出结果。
思路三（推荐）：
使用前后指针。前指针先走n步。然后前指针和后指针同时走，当前指针走到表尾时，后指针刚好走到要删除的元素的位置。这样可以实现一次扫描得出结果，而且比思路二简单。
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		frontPtr = head
		behindPtr = head

		for i in range(n):
			frontPtr = frontPtr.next

		if frontPtr == None:
			return head.next
		while frontPtr.next:
			frontPtr = frontPtr.next
			behindPtr = behindPtr.next

		behindPtr.next = behindPtr.next.next
		return head

