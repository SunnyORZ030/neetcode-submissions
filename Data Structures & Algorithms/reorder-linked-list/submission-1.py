# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next      
        second = slow.next
        slow.next = None
        first = head

        pre = None
        cur = second
        while cur:
            tempNext = cur.next
            cur.next = pre
            pre = cur
            cur = tempNext

        second = pre
        while second:
            tempNextFirst = first.next
            tempNextSecond = second.next
            first.next = second
            second.next = tempNextFirst
            first = tempNextFirst
            second = tempNextSecond