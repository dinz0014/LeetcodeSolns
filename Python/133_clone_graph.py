'''
This file implements the solution to clone graph leetcode problem. The idea is simple.
1. BFS the graph and keep a map edgeMap. edgeMap[x] = a list of the values of neighbours that the node with value x is adjacent to. This step is O(V + E)
2. Initialise a nodeMap. nodeMap[x] = The copied node object that has the value x.
3. Go through all entries in edgeMap and create and put nodes into nodeMap, or if it already exists in nodeMap, update the neighbors attribute properly O(V + E)

Time Complexity: O(V + E)
Space Complexity: O(V)

Problem Link: https://leetcode.com/problems/clone-graph/
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import collections

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        # edgeMap maps node value to list of neighbour values
        edgeMap = {}
        q = collections.deque()
        q.append(node)
        visited = set()
        
        while q:
            x = q.popleft()

            # If has been visited already continue
            if x.val in visited:
                continue
                
            visited.add(x.val)
            
            # If no neighbors, create empty list
            if not x.neighbors:
                edgeMap[x.val] = []
                continue
                        
            for n in x.neighbors:
                if x.val in edgeMap:
                    edgeMap[x.val].append(n.val)
                else:
                    edgeMap[x.val] = [n.val]
                    
                if not n.val in visited:
                    q.append(n)

        # nodeMap maps node value to node object         
        nodeMap = {}
        for key in edgeMap:
            neighbors = []

            # Go through and initialise neighbours if they haven't been already
            for x in edgeMap[key]:
                if x not in nodeMap:
                    nodeMap[x] = Node(x)
                
                neighbors.append(nodeMap[x])
            
            # Initialise node if they haven't already. Otherwise, update neighbors
            if key in nodeMap:
                nodeMap[key].neighbors = neighbors
            else:
                nodeMap[key] = Node(key, neighbors)
        
        # Return copied version of the node that was given
        return nodeMap[node.val]