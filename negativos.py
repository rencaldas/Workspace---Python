N: int

N = int(input("Quantos números você vai digitar? "))
vet: [int] = [0 for x in range (N)]

for i in range (0, N):
    vet[i] = int(input("Digite um número: "))

print()

soma = 0
cont = 0
print("VALORES: ", end=" ")

for i in range (0, N):
    print(f"{vet[i]:.1f} ", end=" ")
    soma += vet[i]
    cont += 1

media = soma / cont
print()
print(f"Soma: {soma:.2f}")
print(f"Média: {media:.2f}")