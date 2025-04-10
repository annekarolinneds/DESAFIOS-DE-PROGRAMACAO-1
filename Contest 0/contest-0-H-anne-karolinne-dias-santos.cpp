#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, m, k;
    while (cin >> n >> m >> k) {
        int a[1000];
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        sort(a, a + n); 
        int ans = m * k; 
        for (int i = 0; i < n - m; i++) {
            ans += a[i]; 
        }
        cout << ans << endl;
    }
    return 0;
}
