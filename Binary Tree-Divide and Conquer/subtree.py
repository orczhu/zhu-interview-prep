两个dfs 嵌套
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param t1: The roots of binary tree T1.
    @param t2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """
    def is_subtree(self, t1: TreeNode, t2: TreeNode) -> bool:
        # write your code here
        if not t2:
            return True
        if not t1:
            return False # means t2 not null, but t1 null
        if self.equal(t1, t2):
            return True
        return self.is_subtree(t1.left, t2) or self.is_subtree(t1.right, t2)
    
    def equal(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 or not t2:
            return t1 == t2
        if t1.val != t2.val:
            return False
        return self.equal(t1.left, t2.left) and self.equal(t1.right, t2.right)

# Op2 using preorder, but need to consider null node, otherwise you can determine
"""
  3  or  3
 /        \           4
4          4
"""
from typing import List
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param t1: The roots of binary tree T1.
    @param t2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """
    def is_subtree(self, t1: TreeNode, t2: TreeNode) -> bool:
        # write your code here
        
        t1_pre = [] 
        self.get(t1, t1_pre)
        print(t1_pre)
        t1_pre = ','.join(t1_pre)
        t2_pre = [] 
        self.get(t2, t2_pre)
        t2_pre = ','.join(t2_pre)
        return t1_pre.find(t2_pre) != -1
    
    def get(self, t: TreeNode, t_list:List[int]):
        if not t:
            t_list.append('#')
            return
        t_list.append(str(t.val))
        self.get(t.left, t_list)
        self.get(t.right, t_list)

