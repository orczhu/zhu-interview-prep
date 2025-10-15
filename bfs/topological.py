# https://www.lintcode.com/problem/127/
from collections import deque
"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return []
        indegree = {}
        for node in graph:
            indegree[node] = 0
        # get indegree count
        for node in graph:
            for next_node in node.neighbors:
                indegree[next_node] += 1
        
        # Find start point
        q = deque()
        vist = set()
        result = []
        for node in indegree:
            if indegree[node] == 0:
                q.append(node)
                vist.add(node)
        
        while len(q) > 0:
            curr = q.popleft()
            result.append(curr)
            for next_node in curr.neighbors:
                indegree[next_node] -= 1
                if indegree[next_node] == 0 and next_node not in vist:
                    q.append(next_node)
                    vist.add(next_node)
        

        return result

        
        
        
#=====
Similar for course schedule
from collections import deque
from typing import (
    List,
)

class Solution:
    """
    @param num_courses: a total of n courses
    @param prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # write your code here
        if not num_courses:
            return False
        indegree = {}
        edge = {}
        for i in range(num_courses):
            indegree[i] = 0
            edge[i] = []
        # Build edge
        for ele in prerequisites:
            from_edge = ele[1]
            to_edge = ele[0]
            indegree[to_edge] += 1
            edge[from_edge].append(to_edge)
        result = []
        q = deque()
        vist = set()
        # Find start 
        for ele in indegree:
            if indegree[ele] == 0:
                q.append(ele)
                vist.add(ele)
        
        while len(q) > 0:
            curr = q.popleft()
            result.append(curr)
            # update indegree
            for next_edge in edge[curr]:
                indegree[next_edge] -= 1
                if indegree[next_edge] == 0 and next_edge not in vist:
                    q.append(next_edge)
                    vist.add(next_edge)
            
        return len(result) == num_courses