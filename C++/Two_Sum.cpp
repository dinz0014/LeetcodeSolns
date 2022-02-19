#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> valMap;
        int N = nums.size();
        vector<int> result;
        
        for (int i = 0; i < N; i++)
        {
            if (valMap.find(target - nums[i]) != valMap.end())
            {
                result = {i, valMap[target - nums[i]]};
                break;
            }
            else
            {
                valMap[nums[i]] = i;   
            }
        }
        
        return result;
    }
};