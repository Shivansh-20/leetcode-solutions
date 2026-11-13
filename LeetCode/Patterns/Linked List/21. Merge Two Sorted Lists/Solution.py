# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1) #what is -1 actually here?
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1 #do not use val here? 
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next #move tail too
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next
        

        