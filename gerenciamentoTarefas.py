import os

tarefas = []

def AdicionarTarefa():
    while True:
        adicionar = input("Insira a tarefa que deseja adicionar: ")

        #Comando para Sair
        if adicionar.lower() == 'sair':
            break
        
        #Caso True = Concluída, contrário False
        nova_tarefa = {"titulo": adicionar, "concluida": False}
        tarefas.append(nova_tarefa)
        os.system('cls') #Limpeza
        #Criação de Pendência
        #print(f"Tarefa {nova_tarefa["titulo"]} adicionada como Pendente!")
        print("\nDigite (Sair) caso queira sair.")

def ListarTarefa():
    for i, tarefa in enumerate(tarefas, start=1):
        pendencia = "Concluída" if tarefa["concluída"] else "Pendente"

def MarcarTarefa():
    ...

def RemoverTarefa():
    ...

os.system('cls')
print("(1) - Adicionar Tarefa \n(2) - Listar Tarefa\n(3) - Marcar Tarefa\n(4) - Remover Tarefa\n(5) - Sair")
print("\n")
while True:
    entrada = int(input("O que você deseja fazer? "))
    if entrada == 1:
        os.system('cls')
        AdicionarTarefa()
    elif entrada == 2:
        os.system('cls')
        ListarTarefa()
    elif entrada == 3:
        os.system('cls')
        MarcarTarefa()
    elif entrada == 4:
        os.system('cls')
        RemoverTarefa()
    elif entrada == 5:
        print("Você decidiu sair.")
        break
    