#include <iostream>
#include <vector>
using namespace std;

void encontrar_indices() {
    int n;
    cin >> n;
    vector<int> p(n);
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
    }

    for (int j = 1; j < n - 1; ++j) {
        if (p[j] > p[j - 1] && p[j] > p[j + 1]) {
            cout << "YES" << endl;
            cout << j << " " << j + 1 << " " << j + 2 << endl;
            return;
        }
    }
    cout << "NO" << endl;
}

int main() {
    int T;
    cin >> T;
    while (T--) {
        encontrar_indices();
    }
    return 0;
}
