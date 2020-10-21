//
// Created by Kelo Deng on 2020/10/21.
//

# include <vector>
using namespace std;


class Solution {
public:
    bool validMountainArray(vector<int>& A) {
        if (A.size() < 2) {
            return false;
        }
        int step = 0;
        for (int i = 0; i < A.size() - 1; i++) {
            if (A[i] == A[i + 1]) {
                return false;
            }
            if (step == 0 && A[i] < A[i + 1]) {
                continue;
            }
            if (step == 0 && A[i] > A[i + 1]) {
                if (i == 0) {
                    return false;
                }
                step = 1;
                continue;
            }
            if (step == 1 && A[i] > A[i + 1]) {
                continue;
            }
            if (step == 1 && A[i] < A[i + 1]) {
                return false;
            }
        }
        return step == 1;
    }
};