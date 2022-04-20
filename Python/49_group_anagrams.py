'''
This file implements the solution to leetcode problem grouping anagrams given a list of strings. The idea is to sort all the strings themselves, then map the sorted versions
using a hashmap.

Time Complexity: O(N * Mlog(M)) where N is the length of "strs" and M is the maximum length of a string in "strs"
Storage Complexity: O(N*M) to store in the hashmap

Problem Link: https://leetcode.com/problems/group-anagrams/submissions/
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedToUnSorted = {}
        n = len(strs)
        
        for i in range(n):
            s = tuple(sorted(strs[i]))
            
            if s in sortedToUnSorted:
                sortedToUnSorted[s].append(strs[i])
            else:
                sortedToUnSorted[s] = [strs[i]]
        
        return sortedToUnSorted.values()