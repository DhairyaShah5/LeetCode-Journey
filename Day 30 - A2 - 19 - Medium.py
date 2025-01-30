# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

# Approach:
# 1. Reverse the List
# 2. Find the nth element from beginning and remove it
# 3. Reverse the List again and return the head

# Step 1:
        previous, current = None, head
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        head = previous
# Step 2:
        current = head
        previous = None
        for i in range(n - 1):  # move to the nth node
            previous = current
            current = current.next
        
        # If the nth node is the first node
        if previous is None:
            head = current.next  # remove it by pointing head to the next node
        else:
            previous.next = current.next
# Step 3:
        previous, current = None, head
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous