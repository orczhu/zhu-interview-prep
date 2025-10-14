# practice to use heapq

https://www.lintcode.com/problem/612/description?showListFe=true&page=1&problemTypeId=2&tagIds=386&pageSize=50
from typing import (
    List,
)
from lintcode import (
    Point,
)
import heapq

"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def k_closest(self, points: List[Point], origin: Point, k: int) -> List[Point]:
        # write your code here
        if not points:
            return []
        heap = []
        for point in points:
            dist = self.get_dis(point, origin)
            # max heap
            heapq.heappush(heap, (-dist, -point.x, -point.y))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        while len(heap) > 0:
            item = heapq.heappop(heap)
            result.append(Point(-item[1], -item[2]))
        result.reverse()
        return result
    def get_dis(self, a: Point, b: Point):
        return (a.x - b.x) ** 2 + (a.y - b.y) ** 2
