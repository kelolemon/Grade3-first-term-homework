#include <iostream>

int main() {
    int n, m;

    for (;scanf("%d %d", &n, &m) != EOF;) {
        int flag = false;
        for (int i = n; i <= m; i++) {
            int low = i % 10;
            int mid = (i / 10) % 10;
            int high = i / 100;
            if (low * low * low + mid * mid * mid + high * high * high == i) {
                flag = true;
                printf("%d ", i);
            }
        }
        if (flag) {
            printf("\n");
        } else {
            puts("no");
        }
    }
    return 0;
}#include <iostream>

int main() {
    int n, m;

    for (;scanf("%d %d", &n, &m) != EOF;) {
        int flag = false;
        for (int i = n; i <= m; i++) {
            int low = i % 10;
            int mid = (i / 10) % 10;
            int high = i / 100;
            if (low * low * low + mid * mid * mid + high * high * high == i) {
                flag = true;
                printf("%d ", i);
            }
        }
        if (flag) {
            printf("\n");
        } else {
            puts("no");
        }
    }
    return 0;
}
