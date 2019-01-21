#!/usr/bin/python3
#-*-coding:utf-8 -*-

'''
题目：21、合并两个有序链表  mergeTwoLists
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4


题目：23、合并K个排序链表  mergeKLists
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6


题目：24、两两交换链表中的节点  swapPairs
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
说明:

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        first = head
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
        if l1 == None:
            head.next = l2
        elif l2 == None:
            head.next = l1
        return first.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = []
        for i in lists:
            while i :
                res.append(i.val)
                i  = i.next
        if res == []:
            return []
        res.sort()
        l =  ListNode(0)
        first = l
        while res:
            l.next = ListNode(res.pop(0))
            l = l.next
        return first.next

    def swapPairs(self,head):
        """
        :param head: ListNode
        :return: ListNode
        """
        h = ListNode(0)
        h.next = head
        pre = h
        while pre.next != None and pre.next.next != None:
            node1 = pre.next
            node2 = node1.next
            lat = node2.next

            pre.next = node2
            node2.next = node1
            node1.next = lat

            pre = node1
        return h.next
