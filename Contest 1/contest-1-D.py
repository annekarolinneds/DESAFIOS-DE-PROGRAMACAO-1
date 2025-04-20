import sys

KEY = "the quick brown fox jumps over the lazy dog"

def tenta_mapeamento(linha):
   
    if len(linha) != len(KEY):
        return None
    
    for c1, c2 in zip(linha, KEY):
        if (c1 == ' ') != (c2 == ' '):
            return None

    mapeia = {}
    usado = {}
    
    for c_cif, c_claro in zip(linha, KEY):
        if c_cif == ' ':
            continue
    
        if c_cif in mapeia and mapeia[c_cif] != c_claro:
            return None
    
        if c_claro in usado and usado[c_claro] != c_cif:
            return None
        mapeia[c_cif] = c_claro
        usado[c_claro] = c_cif

    
    if len(mapeia) < 26:
        return None

    return mapeia

def decifra(linhas, mapeia):
    
    resultado = []
    for linha in linhas:
        dec = []
        for ch in linha:
            if ch == ' ':
                dec.append(' ')
            else:
                dec.append(mapeia.get(ch, '?'))
        resultado.append("".join(dec))
    return resultado

def main():
    data = sys.stdin.read().splitlines()
    idx = 0
    T = int(data[idx].strip()); idx += 1
    
    while idx < len(data) and data[idx].strip() == "":
        idx += 1

    out = []
    for caso in range(T):
      
        cifradas = []
        while idx < len(data) and data[idx] != "":
            cifradas.append(data[idx].rstrip('\n'))
            idx += 1
      
        while idx < len(data) and data[idx].strip() == "":
            idx += 1

      
        mapeamento = None
        for linha in cifradas:
            tentativa = tenta_mapeamento(linha)
            if tentativa is not None:
                mapeamento = tentativa
                break

        if mapeamento is None:
            out.append("No solution.")
        else:
            out.extend(decifra(cifradas, mapeamento))

        if caso != T-1:
            out.append("") 

    print("\n".join(out))

if __name__ == "__main__":
    main()
