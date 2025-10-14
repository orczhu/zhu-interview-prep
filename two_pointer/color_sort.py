#https://www.lintcode.com/problem/148/description
# 3 pointers left mid right
# remember swap mid and right, mid cannot simply move forward because it might need to swap with left
from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sort_colors(self, nums: List[int]):
        # write your code here
        if not nums:
            return 
        left = 0
        right = len(nums) - 1
        mid = left
        while mid <= right:
            if nums[mid] == 0:
                # swap with left
                self.swap(nums, left, mid)
                mid += 1
                left += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                self.swap(nums, right, mid)
                # mid += 1 if might need to swap with left
                right -= 1
    def swap(self, nums, left, right):
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp

# sort_colors II using divide and conquer
from typing import (
    List,
)

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sort_colors2(self, colors: List[int], k: int):
        # write your code here
        if not colors: 
            return 
        self.c_sort(colors, 1, k, 0, len(colors) - 1)
    
    def c_sort(self, colors: List[int], color_from: int, color_to: int, index_from: int, index_to: int):
        if index_from >= index_to or color_from >= color_to:
            return
        color_mid = (color_from + color_to) // 2
        left = index_from
        right = index_to
        while left <= right:
            while left <= right and colors[left] <= color_mid:
                left += 1
            while left <= right and colors[right] > color_mid:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
        self.c_sort(colors, color_from, color_mid, index_from, right)
        self.c_sort(colors, color_mid + 1, color_to, left, index_to)

