import sys

DIRECOES = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
]

def encontra_palavra(grid, m, n, word):
    w = word.lower()
    L = len(w)

    for i in range(m):
        for j in range(n):
            if grid[i][j] != w[0]:
                continue
            
            for dx, dy in DIRECOES:
                ii, jj = i, j
                k = 0
               
                while k < L and 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == w[k]:
                    ii += dx
                    jj += dy
                    k += 1
                if k == L:
               
                    return (i+1, j+1)
    return None

def main():
    data = sys.stdin.read().splitlines()
    idx = 0
    T = int(data[idx].strip()); idx += 1
    
    while idx < len(data) and data[idx].strip() == "":
        idx += 1

    out_lines = []
    for case in range(T):
       
        m, n = map(int, data[idx].split()); idx += 1
       
        grid = [data[idx + i].strip().lower() for i in range(m)]
        idx += m

       
        k = int(data[idx].strip()); idx += 1
        
        for _ in range(k):
            word = data[idx].strip(); idx += 1
            linha, coluna = encontra_palavra(grid, m, n, word)
            out_lines.append(f"{linha} {coluna}")

        if case != T-1:
            out_lines.append("")

        while idx < len(data) and data[idx].strip() == "":
            idx += 1

    print("\n".join(out_lines))

if __name__ == "__main__":
    main()
