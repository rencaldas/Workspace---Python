from datetime import datetime

def CalcularIdade(nome, dataNasc, genero):
    ano_atual = datetime.now().year
    idade = ano_atual - dataNasc

    print(f"\nOlá, {nome}!")
    print(f"Você tem {idade} anos.")

    if genero == "masculino":
        if idade >= 18:
            print("Você é maior de idade.")
        else:
            print("Você é menor de idade.")
    elif genero == "feminino":
        if idade >= 20:
            print("Você é maior de idade.")
        else:
            print("Você é menor de idade.")
    else:
        print("Gênero não reconhecido.")
        
#main
print("Siga as orientações abaixo:")
nome = input("Digite seu nome: ")
genero = input("Qual seu gênero? (Masculino/Feminino): ").lower()
dataNasc = int(input("Digite seu ano de nascimento: "))

CalcularIdade(nome, dataNasc, genero)
