from operator import index

"""
two sum
Although it is simple problem, I want to use two pointer
I need to record original index
use enumerate to get idx and value, and then put into array as : tuple
and sort by value
"""

from typing import (
    List,
)

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        # write your code here
        
        array = []
        for idx,ch in enumerate(numbers):
            array.append((ch, idx))
        array.sort(key = lambda x: x[0])
        left = 0
        right = len(array) - 1
        # if == it will point to the same element
        while left < right:
            current = array[left][0] + array[right][0]
            if current == target:
                return sorted([array[left][1], array[right][1]])
            elif current < target:
                left += 1
            else:
                right -= 1
        
        return []
#### hasmap solution ####
    def two_sum(self, a: List[int], target: int) -> List[int]:
        # write your code here
        # using dict 
        a_dict = {} # key is number value is index
        for idx, val in enumerate(a):
            want = target - val
            if want in a_dict:
                return [a_dict.get(want), idx]
            else:
                a_dict[val] = idx
        
        return []