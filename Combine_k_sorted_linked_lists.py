# coding=utf-8 
# @Time :2019/2/14 11:28

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = []
        for i in lists:
            while i:
                res.append(i.val)
                i = i.next
        if not res:
            return []
        res.sort()
        l = ListNode(0)
        first = l
        while res:
            l.next = ListNode(res.pop(0))
            l = l.next
        return first.next
