from concurrent.futures.process import _WorkItem
from ctypes import pointer


https://www.lintcode.com/problem/1261/note

 Longest Substring with At Least K Repeating Characters
 looks like slow and fast pointer, but both can move and does not work
 I have to use divde and conquer
 Idea to find every break point and split and left and right and find the max
 

 class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: return an integer
    """
    def longest_substring(self, s: str, k: int) -> int:
        # write your code here
        # divide and conquer
        # always split the s into two parts and final the longest_substring
        if not s or len(s) < k:
            return 0
        dict_s = {}
        for item in s:
            dict_s[item] = dict_s.get(item, 0) + 1
        # split
        for i, ch in enumerate(s):
            if dict_s[ch] < k:
                left = self.longest_substring(s[:i], k)
                right = self.longest_substring(s[i + 1:], k)
                return max(left, right)
        return len(s)
