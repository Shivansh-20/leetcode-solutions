# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode()
        dummy.next = head
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        current , count = dummy, 0
        while count < length - n:
            current = current.next
            count += 1
        current.next = current.next.next
        return dummy.next



        