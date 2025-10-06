"""
inhouse dedup is kind of ticky
"""
from lintcode import (
    ListNode,
)

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of the linked list
    """
    def delete_duplicates(self, head: ListNode) -> ListNode:
        # write your code here
        if not head:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        head = dummy
        while head.next and head.next.next:
            if head.next.val == head.next.next.val:
                val = head.next.val
                while head.next and head.next.val == val:
                    head.next = head.next.next
            else:
                head = head.next
        
        return dummy.next
