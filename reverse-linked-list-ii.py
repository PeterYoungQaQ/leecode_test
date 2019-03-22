

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dumpy = ListNode(0)
        dumpy.next = head
        prev = dumpy
        for i in range(m-1):
            prev = prev.next
        
        cur = prev.next
        post = cur.next

        for i in range(n-m):
            cur.next = post.next
            post.next = prev.next
            prev.next = post
            post = cur.next
        
        return dumpy.next

print(Solution().reverseBetween([1,2,3,4,5],2,4))