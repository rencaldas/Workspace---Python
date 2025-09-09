# Dicionário para armazenar as faixas
faixas = {
    "Abaixo do peso normal": 0,
    "Peso normal": 0,
    "Excesso de peso": 0,
    "Obesidade classe I": 0,
    "Obesidade classe II": 0,
    "Obesidade classe III": 0
}

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso normal"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Excesso de peso"
    elif imc < 35:
        return "Obesidade classe I"
    elif imc < 40:
        return "Obesidade classe II"
    else:
        return "Obesidade classe III"

# Entrada do número de pessoas
n = int(input("Quantas pessoas você deseja analisar? "))

# Loop para ler os dados e calcular IMC
for i in range(n):
    print(f"\nPessoa {i+1}")
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    imc = peso / (altura ** 2)
    classificacao = classificar_imc(imc)
    faixas[classificacao] += 1
    print(f"IMC: {imc:.2f} - Classificação: {classificacao}")

# Exibição dos resultados
print("\n--- Estatísticas Finais ---")
for faixa, quantidade in faixas.items():
    percentual = (quantidade / n) * 100
    print(f"{faixa}: {quantidade} pessoa(s) ({percentual:.2f}%)")
