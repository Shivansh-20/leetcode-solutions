# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        tail = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1  else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            digit = total % 10 #(remiander)
            carry = total // 10
            tail.next = ListNode(digit) #(new node addition after dummy)
            tail = tail.next # (moving refernce to new node)
            if l1:
                l1 = l1.next #l1.next only accesses the next node; l1 = l1.next actually moves the pointer.
            if l2:
               l2 =  l2.next
        return dummy.next