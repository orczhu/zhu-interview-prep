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
    
### Even simple two sum function, you need to think about the case like e.g 8, you have 4, make 
# sure at least two 4, otherwise it will return false
class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.sum_dict = {}
    def add(self, number):
        # write your code here
        self.sum_dict[number] = self.sum_dict.get(number, 0) + 1
        return

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for key in self.sum_dict:
            if value - key in self.sum_dict:
                if key == (value - key):
                    if self.sum_dict[key] > 1:
                        return True
                    else:
                        return False
                return True

        return False
    
3sum do not forget to deduplicate

from typing import (
    List,
)

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """
    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        # write your code here
        if not numbers or len(numbers) < 3:
            return []
        result = []
        numbers.sort()
        # dedup
        left = 0
        for left in range(len(numbers) - 2):
            # two sum
            if left > 0 and numbers[left] == numbers[left - 1]:
                continue
            mid = left + 1
            right = len(numbers) - 1
            while mid < right:
                want = -numbers[left]
                if numbers[mid] + numbers[right] == want:
                    result.append([numbers[left], numbers[mid], numbers[right]])
                    mid += 1
                    right -= 1
                    while mid < right and numbers[mid] == numbers[mid - 1]:
                        mid += 1
                    while right > mid and numbers[right] == numbers[right + 1]:
                        right -= 1

                elif numbers[mid] + numbers[right] < want:
                    mid += 1
                else:
                    right -= 1
        return result

# triangle
from typing import (
    List,
)

class Solution:
    """
    @param s: A list of integers
    @return: An integer
    """
    def triangle_count(self, s: List[int]) -> int:
        # write your code here
        if not s or len(s) < 3:
            return 0
        s.sort()
        count = 0
        # reverse (start, stop, step)
        for right in range(len(s) - 1, 1, -1):
            left = 0
            mid = right - 1
            while left < mid:
                if s[left] + s[mid] > s[right]:
                    count += (mid - left)
                    mid -= 1
                else:
                    left += 1
        
        return count


reverse e.g for i in range(len(s) - 1, 0, -1)