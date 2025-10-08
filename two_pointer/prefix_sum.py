length = float('inf') # max
length = float('-inf') # min

https://www.lintcode.com/problem/406/

from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimum_size(self, nums: List[int], s: int) -> int:
        # write your code here
        # prefix sum
        # array -> 1 2 3 4  5
        # prefix 0 1 3 6 10 15
        # prefix 0 1 2 3 4  5
    
        
        prefix = self.get_prefix_sum(nums)
        size = float('inf')
        n = len(nums)
        for start in range(n):
            for end in range(start,n):
                if prefix[end + 1] - prefix[start] >= s:
                    size = min(size, end - start + 1)
        if size == float('inf'):
            return -1
        return size

    def get_prefix_sum(self, nums: List[int]) -> List[int]:
        prefix = [0]
        idx = 1
        for item in nums:
            prefix.append(prefix[-1] + item)
            idx += 1
        return prefix
# Using prefix sum, but it is O(n^2)
# opti to O(n) 