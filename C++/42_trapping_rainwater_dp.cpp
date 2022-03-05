/*
This is the solution using Dynamic Programming. We keep track of the max left height and max right height for each block and use this information to calculate water height.

Time Complexity: O(n)
Space Complexity: O(1)
*/

#include <vector>
using namespace std;

class Solution {
    public:
        int trap(vector<int>& height) {
            int N = height.size();
            vector<int> maxLeft(N);
            vector<int> maxRight(N);
            int blocks = 0;
            int minLR;
            
            // Can't trap water at the ends so set height as 0
            maxLeft[0] = 0;
            maxRight[N-1] = 0;
            
            // Update max left and right boundaries at each index i
            for (int i=1; i < N; i++)
            {
                maxLeft[i] = max(maxLeft[i-1], height[i-1]);
                maxRight[N-i-1] = max(maxRight[N-i], height[N-i]);
            }
            
            // Calculate the blocks of water being trapped
            for (int i=0; i < N; i++)
            {
                minLR = min(maxLeft[i], maxRight[i]);
                
                if (minLR - height[i] > 0)
                {
                    blocks = blocks + minLR - height[i];
                }
            }
            
            return blocks;
        }
};