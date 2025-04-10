#include <iostream>
#include <algorithm> 
using namespace std;

int main() {
    long a, b;

    while (cin >> a >> b) {
        cout << a << " " << b << " ";

        long inicio = a;
        long fim = b;

        // Garantir que a <= b
        if (inicio > fim) {
            swap(inicio, fim);
        }

        long max_cycle = 0;

        for (long i = inicio; i <= fim; ++i) {
            long n = i;
            long cycle = 1;

            while (n != 1) {
                if (n % 2 == 0) {
                    n = n / 2;
                } else {
                    n = 3 * n + 1;
                }
                ++cycle;
            }

            if (cycle > max_cycle) {
                max_cycle = cycle;
            }
        }

        cout << max_cycle << endl;
    }

    return 0;
}
