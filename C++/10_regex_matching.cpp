#include <vector>
#include <string>
using namespace std;

class Solution {
private:
    // Store the strings, their lengths and the lookup table in class for easy access because we are using recursion
    int sLen, pLen;
    string s0, p0;
    vector<vector<int>> lookUp;
public:   
    bool pMatch(int i, int j) {

        // If the subproblem has already been computed, just lookup value and return
        if (lookUp[i][j] != -1)
        {
            return lookUp[i][j];
        }
        
        // If both string and pattern are out of bounds we have found a match
        if (i >= sLen && j >= pLen)
        {
            return true;
        }
        
        // If pattern out of bounds but not string, they are not fully matching
        if (j >= pLen)
        {
            return false;
        }
        
        // See if the character at ith position of s matches character at jth position of p (under the given rules)
        bool match = (i < sLen) && (s0[i] == p0[j] || p0[j] == '.');

        // If there is wild card present, recurse with 2 choices; either use the letter once or use it zero times
        if (j + 1 < pLen && p0[j+1] == '*')
        {
            lookUp[i][j] = (match && pMatch(i+1, j)) || pMatch(i, j+2);
            return lookUp[i][j];
        }

        // If no wildcard present, check if current characters are valid and proceed to next 
        if (match)
        {
            lookUp[i][j] = pMatch(i+1, j+1);
            return lookUp[i][j];
        }
        
        // If everything else failed, they don't match
        lookUp[i][j] = false;
        return false;
    }
    
    bool isMatch(string s, string p) {
        // Initialise the variables for pMatch to use
        sLen = s.length();
        pLen = p.length();
        s0 = s;
        p0 = p;
        vector<int> z(pLen+1, -1);
        lookUp = vector<vector<int>>(sLen+1, z);
        
        return pMatch(0, 0);
    }
};