#include <vector>
#include <string>
#include <unordered_set>
using namespace std;

class Solution {
public:
    // Storage for all the flag checks, results and size of board
    int N;
    unordered_set<int> cols, pdiag, ndiag; //pdiag holds the 45 deg diagonal checks whilst ndiag holds the 135 deg diagonal checks
    vector<vector<string>> result;
    
    vector<vector<string>> solveNQueens(int n) {
        N = n;
        
        // Constructing empty board (note: '.' means empty square and 'Q' means square with a queen)
        vector<vector<char>> s;
        for (int i=0; i < n; i++)
        {
            vector<char> c;
            
            for (int j=0; j < n; j++)
            {
                c.push_back('.');
            }
            
            s.push_back(c);
        }
        
        // Start backtracking
        backtrack(0, s);
        return result;
    }
    
    void backtrack(int r, vector<vector<char>> soln) {
            // Reached end of board, so add solution to results and return
            if (r == N)
            {
                vector<string> board;
                for (auto row: soln)
                {
                    string boardRow(row.begin(), row.end());
                    board.push_back(boardRow);
                }
                result.push_back(board);
                return;
            }
            
            for (int c=0; c < N; c++)
            {
                // Check if placing queen at row r column c is valid
                if (cols.count(c) || ndiag.count(c-r) || pdiag.count(r+c))
                {
                    continue; // skip iteration otherwise
                }
                
                // Place queen and update flags
                cols.insert(c);
                pdiag.insert(r+c);
                ndiag.insert(c-r);
                soln[r][c] = 'Q';
                
                // Place next queen
                backtrack(r+1, soln);
                
                // Take queen away, reset flags
                cols.erase(c);
                pdiag.erase(r+c);
                ndiag.erase(c-r);
                soln[r][c] = '.';
            }
        }
};