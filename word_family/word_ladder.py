# BFS word ladder O(n) = 26LN
from collections import deque
from typing import (
    Set,
    List
)

class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: An integer
    """
    def ladder_length(self, start: str, end: str, dict: Set[str]) -> int:
        # write your code here
        if not start or not end:
            return 0
        dict.add(start)
        dict.add(end)
        dist = {start: 1}
        q = deque()
        q.append(start)
        while len(q) > 0:
            current = q.popleft()
            if current == end:
                return dist[current]
            
            for word in self.get_next(current, dict):
                if word not in dist:
                    q.append(word)
                    dist[word] = dist.get(current) + 1
        return 0
    
    def get_next(self, word: str, dict: Set[str]) -> List[str]:
        result = []
        for idx in range(len(word)):
            rep = 'abcdefghijklmnopqrstuvwxyz'
            for c in rep:
                if word[idx] == c:
                    continue
                new_word = word[:idx] + c + word[idx + 1:]
                if new_word in dict:
                    result.append(new_word)
        return result


