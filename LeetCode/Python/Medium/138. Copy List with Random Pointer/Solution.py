"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        current = head
        d = {}
        while current:
            copy = Node(current.val)
            d[current] = copy
            current = current.next
        current = head
        while current:
            copied = d[current]
            copied.next = d[current.next] if current.next else None
            copied.random = d[current.random] if current.random else None
            #dict has pairs of copy and orignal(key), we want to have info from orignal we can use d[current] 
            current = current.next
        return d[head]
        
            
            
        