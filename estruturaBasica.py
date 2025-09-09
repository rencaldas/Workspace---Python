lista = []

def CadastrarPet():
    while True:
        nomePet = input("Insira o nome do Pet que quer adicionar: ")
        lista.append(nomePet)
        print(f"Pet {nomePet} adicionado!")
        resposta = input("Deseja continuar? (sim/nao): ").lower()
        if resposta != "sim":
            break

def ListarPet():
    print("\nPets cadastrados:")
    for nomePet in lista:
        print(f"- {nomePet}")

def EditarPet():
    if not lista:
        print("A lista está vazia. Não há pets para editar.")
        return
    print("Pets cadastrados:")
    for i, pets in enumerate(lista):
        print(f"{i + 1} - {pets}")
    try:
        escolha = int(input("Digite o número do pet que deseja editar: "))
        if escolha < 1 or escolha > len(lista):
            print("Número inválido.")
            return
    except ValueError:
        print("Por favor, digite um número válido.")
        return
    novo_nome = input("Digite o novo nome do pet: ")
    lista[escolha - 1] = novo_nome
    print("Pet atualizado com sucesso!")

def RemoverPet():
    if not lista:
        print("A lista está vazia. Não há pets para remover.")
        return
    print("Pets cadastrados:")
    for i, pets in enumerate(lista):
        print(f"{i + 1} - {pets}")
    try:
        numeroLista = int(input("Digite o número do pet que deseja remover: "))
        if numeroLista < 1 or numeroLista > len(lista):
            print("Número inválido.")
            return
    except ValueError:
        print("Por favor, digite um número válido.")
        return
    removido = lista.pop(numeroLista - 1)  # <- Correção aqui
    print(f"\nPet '{removido}' removido com sucesso!")

while True:
    print("\nMenu:"); print("1 - Cadastrar Pet"); print("2 - Listar Pet"); print("3 - Editar Pet"); print("4 - Remover Pet"); print("5 - Sair")
    try:
        opcao = int(input("\nO que deseja fazer? "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if opcao == 1:
        CadastrarPet()
    elif opcao == 2:
        ListarPet()
    elif opcao == 3:
        EditarPet()
    elif opcao == 4:
        RemoverPet()
    elif opcao == 5:
        print("Saindo...")
        break
    else:
        print("Opção ainda não implementada.")
