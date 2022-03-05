/*
This is the two pointer solution. The trick is to notice that the end blocks cannot trap water, and that we can shift left or right based on the lower maximum boundary.
The bottleneck for rainwater trapping is always the smaller of the two boundaries, so this method works. 

Time Complexity : O(n)
Space Complexity : O(1)
*/

#include <vector>
using namespace std;

class Solution {
    public:
        int trap(vector<int>& height) {
            int N = height.size();
            int blocks = 0;
            int maxL = height[0];
            int maxR = height[N-1];
            int l = 0;
            int r = N-1;
            
            // Keep shifting left (if left boundary lower) or right (if right boundary lower)
            while (l < r)
            {
                if (maxL <= maxR)
                {
                    // Shift and calculate water blocks
                    l++;
                    blocks = blocks + max(0, maxL - height[l]);
                    
                    // Update maximum boundary
                    if (height[l] > maxL)
                    {
                        maxL = height[l];
                    }
                }
                else
                {
                    // Shift and calculate water blocks
                    r--;
                    blocks = blocks + max(0, maxR - height[r]);
                    
                    // Update maximum boundary
                    if (height[r] > maxR)
                    {
                        maxR = height[r];
                    }
                }
            }
            
            return blocks; 
        }
};