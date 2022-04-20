'''
This file implements the solution to leetcode problem grouping anagrams given a list of strings. The idea is to sort all the strings themselves, then map the sorted versions
using a hashmap.

Time Complexity: O(N * Mlog(M)) where N is the length of "strs" and M is the maximum length of a string in "strs"
Storage Complexity: O(N*M) to store in the hashmap

Problem Link: https://leetcode.com/problems/group-anagrams/submissions/
'''

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedToUnSorted = {} # Maps sorted string to a list of original strings that take the same sorted form
        
        for w in strs:
            # Turn the list into a tuple for hashing
            s = tuple(sorted(w))
            
            if s in sortedToUnSorted:
                sortedToUnSorted[s].append(w)
            else:
                sortedToUnSorted[s] = [w]
        
        return sortedToUnSorted.values()