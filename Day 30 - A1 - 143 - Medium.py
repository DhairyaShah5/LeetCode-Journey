# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
# It's a combination of Slow-Fast Pointers, Reverse a List, and Merge Two Sorted Lists Problems.

# Approach:
# 1. Using Slow-Fast Pointers Technique, find the middle of the list
# 2. Reverse the list starting from the middle upto the end, so that we have the pointers facing the correct decision
# 3. Merge the two lists, first half from starting and second half from ending.

# Step 1:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondHalfOfList = slow.next
        slow.next = None
# Step 2:
        previous = None
        while secondHalfOfList:
            temp = secondHalfOfList.next
            secondHalfOfList.next = previous
            previous = secondHalfOfList
            secondHalfOfList = temp
# Step 3:
        first, secondHalfOfList = head, previous

        while secondHalfOfList:
            temp1, temp2 = first.next, secondHalfOfList.next
            first.next = secondHalfOfList
            secondHalfOfList.next = temp1
            first = temp1
            secondHalfOfList = temp2