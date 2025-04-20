import sys

def classifica(sol_padrao, sol_time):
   
    if sol_padrao == sol_time:
        return "Accepted"
   
    nums_padrao = "".join(ch for line in sol_padrao for ch in line if ch.isdigit())
    nums_time   = "".join(ch for line in sol_time   for ch in line if ch.isdigit())
    if nums_padrao == nums_time:
        return "Presentation Error"
    return "Wrong Answer"

def main():
    dados = sys.stdin.read().splitlines()
    idx = 0
    run = 1

    while True:
        if idx >= len(dados):
            break
        n = int(dados[idx].strip()); idx += 1
        if n == 0:
            break

        sol_padrao = []
        for _ in range(n):
            sol_padrao.append(dados[idx])
            idx += 1

        m = int(dados[idx].strip()); idx += 1
        sol_time = []
        for _ in range(m):
            sol_time.append(dados[idx])
            idx += 1

        resultado = classifica(sol_padrao, sol_time)
        print(f"Run #{run}: {resultado}")
        run += 1

if __name__ == "__main__":
    main()
