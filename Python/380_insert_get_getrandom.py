'''
This file implements a RandomizedSet datastructure that inserts, removes, and gets a random element all in O(1) time. The trick is to combine the functionality
of an array and a hashmap

Leetcode Link: https://leetcode.com/problems/insert-delete-getrandom-o1/
'''
from random import randint

class RandomizedSet:

    def __init__(self):
        self.iMap = {} # maps value to index in array
        self.array = [] # stores value in a order (for O(1) get random)
        self.length = 0 # variable to track size of set (for O(1) size checking)
        
    def insert(self, val: int) -> bool:
        # Immediately return false if the value is in the map
        if val in self.iMap:
            return False
        
        # Add new elements to end of list
        self.iMap[val] = self.length
        self.array.append(val)
        self.length += 1
        return True

    def remove(self, val: int) -> bool:
        # Immediately return false if the value is not in the map
        if val not in self.iMap:
            return False
        
        # Copy item at end of list to index of item being removed
        rmIdx = self.iMap[val]
        self.array[rmIdx] = self.array[-1]
        self.iMap[self.array[-1]] = rmIdx

        # Delete item from array and map, decrement length too
        del self.iMap[val]
        self.array.pop()
        self.length -= 1
        return True

    def getRandom(self) -> int:
        # Get random index and return element at this index
        randomIdx = randint(0, self.length - 1)
        return self.array[randomIdx]
