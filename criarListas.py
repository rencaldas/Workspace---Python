lista = []

print("Lista de Compras: Opções\n")

def inserir_produto():
    while True:
        item = input("Insira o produto para a lista ou digite 'sair': ")
        if item.lower() == 'sair':
            return
        lista.append(item)
        print(f"Item adicionado: {item}")

def apagar_produto():
    while True:
        if not lista:
            print("A lista está vazia. ")
            return
        
        print("\nItens na lista: ")
        for i, item in enumerate(lista, start=1):
            print(f"{i} - {item}")

        apagarProduto = input("Insira o ID do produto que deseja apagar (ou 'sair' para voltar): ")

        if apagarProduto.lower() == 'sair':
            return

        if apagarProduto.isdigit():
            indice = int(apagarProduto) - 1
            if 0 <= indice < len(lista):
                removido = lista.pop(indice)
                print(f"Produto '{removido}' removido com sucesso!")
            else:
                print("ID inválido!")
        else:
            print("Digite um número válido ou 'sair'.")

def listar_valores():
    if not lista:
        print("A lista está vazia.")
    else:
        print("\nItens na lista:")
        for i, item in enumerate(lista, start=1):
            print(f"{i} - {item}")

while True:
    try:
        resposta = int(input("\n1 - Inserir\n2 - Apagar\n3 - Listar\n4 - Sair\n\nO que deseja fazer na lista? "))
    except ValueError:
        print("Digite um número válido!")
        continue

    if resposta == 1:
        inserir_produto()
    elif resposta == 2:
        apagar_produto()
    elif resposta == 3:
        listar_valores()
    elif resposta == 4:
        print("Você escolheu sair.")
        break
    else:
        print("Você não inseriu um valor válido!")
