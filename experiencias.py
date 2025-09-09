C = 0; R = 0; S = 0

N = int(input("Quantos casos de teste serão digitados? "))

for i in range(N):
    qtdCobaias = int(input("Quantidade de cobaias: "))
    tipoCobaias = input("Tipo de cobaia (C para coelho, R para rato, S para sapo): ").upper()

    if tipoCobaias == 'C':  
        C += qtdCobaias
    elif tipoCobaias == 'R': 
        R += qtdCobaias
    elif tipoCobaias == 'S': 
        S += qtdCobaias
    else:
        print("Você inseriu um tipo de cobaia inválido. Tente novamente.")
        break

total = C + R + S
print("\nRelatório final:")
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {C}")
print(f"Total de ratos: {R}")
print(f"Total de sapos: {S}")

if total > 0:
    print(f"Percentual de coelhos: {C / total * 100:.2f}%")
    print(f"Percentual de ratos: {R / total * 100:.2f}%")
    print(f"Percentual de sapos: {S / total * 100:.2f}%")
