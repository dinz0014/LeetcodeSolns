#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> A = nums1;
        vector<int> B = nums2;
        int low = -pow(10, 6) - 1;
        int high = pow(10, 6) + 1;
        
        // Let A be the smaller array
        if (B.size() < A.size())
        {
            vector<int> temp = A;
            A = B;
            B = temp;
        }
        
        
        int total = nums1.size() + nums2.size();
        int half = total/2;
        int l = 0;
        int r = A.size() - 1;
        int m, n, Aleft, Bleft, Aright, Bright;
        
        while (true)
        {
            // Binary search finding middle (modified to mimic pythonic integer division)
            if (l >= 0 && r >= 0)
            {
                m = l + (r-l)/2;
            }
            else
            {
                m = r - (r-l)/2;
            }
            
            // Find the left partition of the bigger array
            n = half - m - 2;
            
            Aleft = (m < 0) ? low : A[m];
            Aright = ((m + 1) < A.size()) ? A[m + 1] : high;
            Bleft = (n < 0) ? low : B[n];
            Bright = ((n + 1) < B.size()) ? B[n + 1] : high;
            
            if (Aleft <= Bright && Bleft <= Aright)
            {
                // odd length
                if (total%2)
                {
                    return min(Aright, Bright);
                }
                // even length
                else
                {
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2.0;
                }
            }
            else if (Aleft > Bright)
            {
                r = m-1;
            }
            else
            {
                l = m+1;
            }
        }
    }
};