#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int w, d, h;
        int a, b, f, g;

        cin >> w >> d >> h;
        cin >> a >> b >> f >> g;

        int rota_inferior = b + abs(a - f) + g;             
        int rota_esquerda = a + abs(b - g) + f;             
        int rota_superior = (d - b) + abs(a - f) + (d - g); 
        int rota_direita  = (w - a) + abs(b - g) + (w - f); 

        int menor_distancia = min({rota_inferior, rota_esquerda, rota_superior, rota_direita});

        int distancia_total = menor_distancia + h;

        cout << distancia_total << endl;
    }

    return 0;
}
