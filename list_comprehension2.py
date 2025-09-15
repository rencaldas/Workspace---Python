# Funções
def gerar_lista(qtd, mult):
    # Gera a lista usando list comprehension
    return [n * mult for n in range(qtd)]

def mostrar_resultados(lista, mult):
    print("\n--- RESULTADOS ---")
    [print(f"{i} * {mult} = {valor}") for i, valor in enumerate(lista)]

def mostrar_pares(lista):
    pares = [n for n in lista if n % 2 == 0]
    print(f"\nNúmeros pares: {pares}")

def mostrar_impares(lista):
    impares = [n for n in lista if n % 2 != 0]
    print(f"\nNúmeros ímpares: {impares}")

def estatisticas(lista):
    maior = max(lista)
    menor = min(lista)
    soma = sum(lista)
    print("\n--- ESTATÍSTICAS ---")
    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
    print(f"Soma total: {soma}")

# Programa principal
numeros = int(input("Quantos números você quer criar? "))
multiplicar = int(input("Por quanto deseja multiplicar? "))

lista = gerar_lista(numeros, multiplicar)

mostrar_resultados(lista, multiplicar)
mostrar_pares(lista)
mostrar_impares(lista)
estatisticas(lista)