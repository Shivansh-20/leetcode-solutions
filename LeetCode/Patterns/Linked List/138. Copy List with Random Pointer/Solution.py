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
        from copy import deepcopy
        return deepcopy(head)
        print(head)
        return copy_list(head)
        
        
def copy_list(list_ref:list):
    new_list = []
    for x in new_list:
        if isinstance(x, list):
            x = copy_list(x)
        new_list.append(x)
    return new_list
            

        