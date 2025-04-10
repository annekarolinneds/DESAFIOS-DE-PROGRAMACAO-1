#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> ler_vetor(int n) {
    vector<int> a(n);
    for (int& x : a) cin >> x;
    return a;
}

int calcular_maior_altura(vector<int>& a) {
    sort(a.begin(), a.end(), greater<int>());
    int res = 0;
    for (int i = 0; i < a.size(); ++i) {
        if (a[i] >= i + 1) {
            res = i + 1;
        }
    }
    return res;
}

int main() {
    int k;
    cin >> k;
    while (k--) {
        int n;
        cin >> n;

        vector<int> a = ler_vetor(n);
        int resultado = calcular_maior_altura(a);

        cout << resultado << '\n';
    }
    return 0;
}
