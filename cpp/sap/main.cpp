#include <iostream>
# include <cstring>
using namespace std;


int main() {
    int n, k;
    string str;
    cin >> n >> k;
    cin >> str;
    int l = 0, r = 0;
    int ans = 0;
    if (str.length() == 0) {
        puts("0");
        return 0;
    }
    int tot = 0;
    if (str[0] == 'A') ans++;
    for (;l <= r && r < str.length();) {
        if (ans == k) {
            int left_ans = 0;
            int right_ans = 0;
            for (;str[l] == 'B';) {
                l++;
                left_ans++;
            }
            for (;str[r+1] == 'B';) {
                r++;
                right_ans++;
            }
            tot += (left_ans + 1) * (right_ans + 1);
            r++;
            ans++;
        } else {
            if (ans > k) {
                if (l < str.length() && str[l] == 'A') {
                    ans--;
                    l++;
                } else {
                    l++;
                }
            } else {
                r++;
                if (r < str.length() && str[r] == 'A') {
                    ans ++;
                }
            }
        }
    }
    printf("%d\n", tot);
}
