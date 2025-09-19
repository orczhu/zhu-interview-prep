from typing import (
    List,
)
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
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        # write your code here
        rest = []
        if root is None:
            return rest
        self._helper(root, rest)
        return rest        
    
    def _helper(self, root: TreeNode, rest: List[int]) -> None:
        if root is None:
            return
        self._helper(root.left, rest)
        rest.append(root.val)
        self._helper(root.right, rest)

        """
        iterative
        """
        
        from typing import (
    List,
)
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
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorder_traversal(self, root: TreeNode) -> List[int]:
        # write your code here
        result = []
        if root is None:
            return result
        stack = [] # stack
        curr = root
        while curr is not None or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        
        return result
