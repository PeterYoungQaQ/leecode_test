# coding=utf-8
"""
给定两个非空链表来表示两个非负整数。
位数按照逆序方式存储，它们的每个节点只存储单个数字。
将两数相加返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。
"""

# Definition for singly-linked list.
import numpy as np


class Solution:
    def addTwoNumbers(self):
        list1 = input()
        list2 = input()

        num1 = 0
        num2 = 0
        list1 = [v for v in list1 if str(v).isdigit()]
        list2 = [v for v in list2 if str(v).isdigit()]
        list1 = list(map(int, list1))
        list2 = list(map(int, list2))
        l1 = len(list1)
        l2 = len(list2)
        for i in range(l1):
            num1 += list1[i] * (10 ** (l1 - i - 1))
        for i in range(l2):
            num2 += list2[i] * (10 ** (l1 - i - 1))
        total = num1 + num2
        l3 = len(str(total))
        list3=np.zeros(l3)
        for i in range(l3):
            t = total % 10
            list3[i] = t
            total = total // 10
        list3 = list(map(int, list3))
        print(list3)

    addTwoNumbers(0)
