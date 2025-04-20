import sys
from collections import Counter

def tenta_candidato(fragments, candidato):

    cnt = Counter(fragments)

    for f in sorted(fragments, key=len, reverse=True):
        if cnt[f] == 0:
            continue
        cnt[f] -= 1
  
        if candidato.startswith(f):
            g = candidato[len(f):]
        elif candidato.endswith(f):
            g = candidato[:len(candidato) - len(f)]
        else:
            return False
        if cnt[g] == 0:
            return False
        cnt[g] -= 1
    return True

def reconstrui(fragments):
   
   
    ordenados = sorted(fragments, key=len, reverse=True)
    maior = ordenados[0]
   
    for f2 in ordenados[1:]:
   
        for cand in (maior + f2, f2 + maior):
            if tenta_candidato(fragments, cand):
                return cand
    return None  

def main():
    data = sys.stdin.read().splitlines()
    idx = 0
    T = int(data[idx].strip()); idx += 1
   
    while idx < len(data) and data[idx].strip() == "":
        idx += 1

    out = []
    for caso in range(T):
        fragments = []
  
        while idx < len(data) and data[idx].strip() != "":
            fragments.append(data[idx].strip())
            idx += 1
       
        while idx < len(data) and data[idx].strip() == "":
            idx += 1

        sol = reconstrui(fragments)
        out.append(sol if sol is not None else "")

        if caso != T-1:
            out.append("")  

    print("\n".join(out))

if __name__ == "__main__":
    main()
