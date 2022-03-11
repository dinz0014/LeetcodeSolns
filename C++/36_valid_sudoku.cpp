/*
The solution to Valid Sudoku problem of leetcode. This is a brute force check of each square in the sudoku board.

Time Complexity: O(9^2) = O(1)
Space Complexity: O(9^2) = O(1)

Technically constant time and space because sudoku board size does not change
*/

#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Vectors to check if a certain number exists in row, column and mini 3x3 box
        vector<vector<int>> rows, cols;
        vector<vector<vector<int>>> miniBoxes;
        
        // Fill rows and cols with 0s
        for (int i=0; i < 9; i++)
        {
            vector<int> o(9,0);
            rows.push_back(o);
            cols.push_back(o);
        }
        
        // Fill all the miniboxes with 0s
        for (int i=0; i < 3; i++)
        {
            vector<vector<int>> boxes;
            for (int j=0; j < 3; j++)
            {
                vector<int> o(9,0);
                boxes.push_back(o);
            }
            miniBoxes.push_back(boxes);
        }
        
        // Go through entire board
        for (int i=0; i < 9; i++)
        {
            for (int j=0; j < 9; j++)
            {
                // If nothing at this location, skip
                if (board[i][j] == '.')
                {
                    continue;
                }
                
                // Get the integer at board[i][j] and decrement to turn it into index
                int lookUp = board[i][j] - '0';
                lookUp--;

                // If not valid placement immediately return false
                if (rows[i][lookUp] || cols[j][lookUp] || miniBoxes[i/3][j/3][lookUp])
                {
                    return false;
                }
                
                // Otherwise, update each flag and proceed
                rows[i][lookUp] = 1;
                cols[j][lookUp] = 1;
                miniBoxes[i/3][j/3][lookUp] = 1;
            }
        }
        
        // If all entries are valid, return true
        return true;
    }
};