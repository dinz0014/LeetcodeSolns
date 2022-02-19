from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        result = []
        nums.sort() # Sort the array in-place
        
        # Fix the first number in triplet
        for i in range(N):
            # We initialise two pointers to search for the other two numbers 
            p1 = i+1
            p2 = N-1

            # If the first number was already seen before, skip it
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # As long as the left is before right, continue search
            while p1 < p2:
                
                s = nums[i] + nums[p1] + nums[p2]
    
                if s == 0:
                    # We found a triplet so record it and change indices
                    result.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1
                    
                    # Change left and right pointers until duplicates are skipped
                    while p1 < p2 and nums[p1] == nums[p1-1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2+1]:
                        p2 -= 1
                    
                elif s < 0:
                    p1 += 1
                else:
                    p2 -= 1
                
        return result