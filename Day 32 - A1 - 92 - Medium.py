# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        leftPrevious, current = dummy, head
        for i in range(left - 1):
            leftPrevious, current = current, current.next

        previous = None
        for i in range(right - left + 1):
            tempNext = current.next
            current.next = previous
            previous, current = current, tempNext

        leftPrevious.next.next = current
        leftPrevious.next = previous

        return dummy.next