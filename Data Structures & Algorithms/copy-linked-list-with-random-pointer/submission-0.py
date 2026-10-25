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
        if head is None:
            return None
        old_id_to_new_node = {}
        node = head
        last = Node(0,None,None)
        first_new = last        
        while node:
            new_node = Node(node.val, None, None)
            old_id_to_new_node[id(node)] = new_node        
            last.next = new_node
            last = new_node
            node = node.next
        node = head
        while node:
            new = old_id_to_new_node[id(node)]
            if node.random is None:
                randomed_new = None
            else:
                randomed_new = old_id_to_new_node[id(node.random)]
            new.random = randomed_new
            node = node.next
        return first_new.next
