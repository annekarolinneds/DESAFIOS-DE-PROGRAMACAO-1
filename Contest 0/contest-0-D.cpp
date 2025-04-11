#include <iostream>
#include <cmath>
using namespace std;

bool eh_primo(int num) {
    if (num <= 1) return false;
    int raiz = sqrt(num);
    for (int i = 2; i <= raiz; ++i) {
        if (num % i == 0) return false;
    }
    return true;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int m, n;
        cin >> m >> n;

        for (int i = m; i <= n; ++i) {
            if (eh_primo(i)) {
                cout << i << '\n';
            }
        }
        cout << '\n'; 
    }

    return 0;
}
