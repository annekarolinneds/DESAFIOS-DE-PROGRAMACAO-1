import sys
from collections import Counter

def intersecao_ordenada(a: str, b: str) -> str:
    
    ca = Counter(a)
    cb = Counter(b)
    
    comum = []
    for letra in map(chr, range(ord('a'), ord('z')+1)):
        vezes = min(ca[letra], cb[letra])
        if vezes > 0:
            comum.append(letra * vezes)
    
    return ''.join(comum)

def main():
    linhas = sys.stdin.read().splitlines()
    
    for i in range(0, len(linhas), 2):
        a = linhas[i].strip()
        b = linhas[i+1].strip() if i+1 < len(linhas) else ""
        resultado = intersecao_ordenada(a, b)
        print(resultado)

if __name__ == "__main__":
    main()
