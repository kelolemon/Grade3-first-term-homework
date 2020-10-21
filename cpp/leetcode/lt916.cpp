//
// Created by Kelo Deng on 2020/10/21.
//

# include <cstring>
# include <string>
# include <vector>
using namespace std;

class Solution {
public:
    vector<string> wordSubsets(vector<string>& A, vector<string>& B) {
        int HashB[26];
        memset(HashB, 0, sizeof(HashB));
        for (auto b : B) {
            int TmpHash[26];
            memset(TmpHash, 0 ,sizeof(TmpHash));
            for (auto ch : b) {
                TmpHash[ch - 'a'] ++;
            }
            for (int i = 0; i < 26; i++) {
                HashB[i] = max(HashB[i], TmpHash[i]);
            }
        }
        for (auto & a : A) {
            int HashA[26];
            memset(HashA, 0, sizeof(HashA));
            for (auto ch : a) {
                HashA[ch - 'a'] ++;
            }
            for (int i = 0; i < 26; i++) {
                if (HashB[i] > HashA[i]) {
                    a = "WrongAns";
                    break;
                }
            }
        }
        auto NewEnd = remove(A.begin(), A.end(), "WrongAns");
        return vector<string>(A.begin(), NewEnd);
    }
};