#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int N = nums.size();
        vector<vector<int>> result;

        //Sort the array in-place
        sort(nums.begin(), nums.end());
        
        // Fix the first number in triplet
        for (int i = 0; i < N; i++)
        {
            // We initialise two pointers to search for the other two numbers 
            int p1 = i+1;
            int p2 = N-1;
            
            // If the first number was already seen before, skip it
            if (i > 0 && nums[i] == nums[i-1]){ continue; }
            

            // As long as the left is before right, continue search
            while (p1 < p2)
            {
                int s = nums[i] + nums[p1] + nums[p2];
                
                if (s == 0)
                {
                    // We found a triplet so record it and change indices
                    vector<int> triplet = {nums[i], nums[p1], nums[p2]};
                    result.push_back(triplet);
                    p1++;
                    p2--;
                    

                    // Change left and right pointers until duplicates are skipped
                    while (p1 < p2 && nums[p1] == nums[p1-1])
                    {
                        p1++;
                    }
                    
                    while (p1 < p2 && nums[p2] == nums[p2+1])
                    {
                        p2--;
                    }
                }
                else if (s < 0)
                {
                    p1++;
                }
                else
                {
                    p2--;
                }
            }
            
        }
        
        return result;
    }
};