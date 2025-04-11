#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    const int target = 1500;
    vector<long long> feios;
    feios.push_back(1);

    int i2 = 0, i3 = 0, i5 = 0;

    while (feios.size() < target) {
        long long proximo = min({feios[i2] * 2, feios[i3] * 3, feios[i5] * 5});
        feios.push_back(proximo);

        if (proximo == feios[i2] * 2) i2++;
        if (proximo == feios[i3] * 3) i3++;
        if (proximo == feios[i5] * 5) i5++;
    }

    cout << "The 1500'th ugly number is " << feios.back() << "." << endl;
    return 0;
}
