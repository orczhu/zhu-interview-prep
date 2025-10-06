"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head:
            return None
        # key is old node, value is new one
        node_map = {None: None}
        dummy = head
        # create new node
        while dummy:
            node_map[dummy] = RandomListNode(dummy.label)
            dummy = dummy.next
        # connect
        dummy = head
        while dummy:
            node_map[dummy].next = node_map[dummy.next]
            node_map[dummy].random = node_map[dummy.random]
            dummy = dummy.next
        
        return node_map[head]

###
What I learned dict can have {None: None} to prevent key error


        