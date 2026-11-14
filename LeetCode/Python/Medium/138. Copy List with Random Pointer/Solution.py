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
        
        
        import copy 
        return copy.deepcopy(head)
        current = head
        d = {}
        while current:
            copy_current = Node(current.val)
            d[current] = copy_current
            current = current.next
        

            

        