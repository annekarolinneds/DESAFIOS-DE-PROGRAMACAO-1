#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int a, b, c;
        cin >> a >> b >> c;

        int x = min({a, b, c});
        int z = max({a, b, c});
        int y = a + b + c - x - z;

        if (x + y == z || (x == y && z % 2 == 0) || (x == z && y % 2 == 0) || (y == z && x % 2 == 0)) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }

    return 0;
}
