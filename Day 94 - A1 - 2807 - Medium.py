# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a

        current = head
        while current.next:
            a, b = current.val, current.next.val
            current.next = ListNode(gcd(a, b), current.next)
            current = current.next.next

        return head