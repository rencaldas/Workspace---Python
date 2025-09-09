import os

lista = []

def adicionar():
    print("Digite 0 para sair: ")
    while True:
        numero = int(input("Digite os números que queira adicionar: "))
        if numero != 0:
            lista.append(numero)
            print(f"\nNúmero {numero} adicinado! Digite 0 caso queira sair.")
        else:
            os.system('cls')
            return escolha

def remover():
    while True:
        remover = int(input("Qual posição deseja remover? "))
        lista.remove(remover)
        escolha = input(print(f"Elemento {remover} removido! Deseja remover mais algum número? (S)im (N)ão: "))
        if escolha.lower() == 'sim':
            continue
        else:
            os.system('cls')
            return escolha

def listar():
    if lista == []:
        print('Lista atual: Vazia')
    else:
        print('Lista atual: ', *lista, '\n')

    return escolha

while True:
    escolha = int(input("0- Sair\n1- Adicionar número\n2- Remover número\n3- Listar número\nDigite o que deseja fazer: "))
    if escolha == 1:
        os.system('cls')
        adicionar()
    elif escolha == 2:
        os.system('cls')
        remover()
    elif escolha == 3:
        os.system('cls')
        listar()
    else:
        print("Você decidiu sair.")
        break
