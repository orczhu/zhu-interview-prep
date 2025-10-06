"""
merge k sorted lists
"""
from typing import List

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        # using merge sort mindset
        if not lists:
            return None
        return self.dfs(lists, 0, len(lists) - 1)
    
    def dfs(self, lists: List[ListNode], start: int , end: int) -> ListNode:
        if start == end:
            return lists[start]
        mid = (end + start) // 2
        left = self.dfs(lists, start, mid)
        right = self.dfs(lists, mid + 1, end)
        return self.mergeTwo(left, right)
    
    def mergeTwo(self, left:ListNode, right:ListNode) -> ListNode:
        dummy = ListNode(-1)
        head = dummy
        while left and right:
            if left.val < right.val:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next
            head = head.next
        head.next = left if left else right
        return dummy.next
        

##### Using heapq #####
import heapq
from typing import List
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
ListNode.__lt__= lambda x, y: x.val < y.val
class Solution:
   
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists:List[ListNode]):
        # write your code here
        if not lists:
            return None
        heap = []
        for item in lists:
            if item:
                heapq.heappush(heap, item)
        dummy = ListNode(-1)
        head = dummy
        while heap:
            curr = heapq.heappop(heap)
            head.next = curr
            if curr.next:
                heapq.heappush(heap, curr.next)
            head = head.next
        return dummy.next
        
        

