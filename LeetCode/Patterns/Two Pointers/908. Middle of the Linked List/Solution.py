# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next #slow pointer now moves one node
            fast = fast.next.next
        return slow

            

         


        