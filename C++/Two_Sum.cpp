#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> valMap; // Maps numbers in nums to the corresponding index
        int N = nums.size();
        vector<int> result; 
        
        for (int i = 0; i < N; i++)
        {
            // If the required number is in the map, we have seen it before so we have found the answer
            if (valMap.find(target - nums[i]) != valMap.end())
            {
                result = {i, valMap[target - nums[i]]};
                break;
            }
            else
            {
                // Otherwise, add the current number and index to map
                valMap[nums[i]] = i;   
            }
        }
        
        return result;
    }
};