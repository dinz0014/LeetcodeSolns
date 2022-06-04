'''
This file implements the solution to the Minimum cost to connect points problem. The idea is simple. Run prim's algorithm on the graph made by connecting
all points with edge weights as Manhattan distance.

Time Complexity: O(|V|^2) worst case
Storage Complexity: O(V)
'''


from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhatDist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        N = len(points)       
        T = set()
        ans = 0
        V = [(0, (0,0))]
        
        while len(T) < N:
            # Get minimum weight edge
            w, (u,v) = heapq.heappop(V)
            
            # If the destination is in T, skip this
            if v in T: continue
            
            # Update MST weight and add destination to visited
            ans += w
            T.add(v)
            
            # Add all outgoing edges to non-MST vertices to heap
            for i in range(N):
                if i not in T:
                    heapq.heappush(V, (manhatDist(points[i], points[v]), (v,i)))
        
        return ans