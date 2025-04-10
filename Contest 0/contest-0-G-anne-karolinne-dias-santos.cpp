#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;

    while (n--) {
        string palavra;
        cin >> palavra;

        if (palavra.length() > 10) {
            cout << palavra[0] << palavra.length() - 2 << palavra.back() << endl;
        } else {
            cout << palavra << endl;
        }
    }

    return 0;
}
