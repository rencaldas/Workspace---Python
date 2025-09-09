import os

def media_alunos():
    alunos = []
    soma_medias = 0
    aprovados = 0
    reprovados = 0

    os.system('cls')    
    x = int(input("Quantos alunos há na turma? "))

    for i in range(x):
        print(f"\nAluno {i + 1}:")
        nome = input("Nome: ")
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        media = (nota1 + nota2) / 2

        situacao = "Aprovado" if media >= 6 else "Reprovado"
        print(f"Média: {media:.2f} - Situação: {situacao}")

        alunos.append({'nome': nome, 'media': media})
        soma_medias += media

        if situacao == "Aprovado":
            aprovados += 1
        else:
            reprovados += 1

    media_turma = soma_medias / x

    maior_media = max(alunos, key=lambda aluno: aluno['media'])
    menor_media = min(alunos, key=lambda aluno: aluno['media'])

    print("\n--- Resultado Final ---")
    print(f"Média da turma: {media_turma:.2f}")
    print(f"Maior média: {maior_media['nome']} com média {maior_media['media']:.2f}")
    print(f"Menor média: {menor_media['nome']} com média {menor_media['media']:.2f}")
    print(f"Alunos aprovados: {aprovados}")
    print(f"Alunos reprovados: {reprovados}")
    escolha = input("Você deseja (repetir) ou (voltar) ao menu? ")
    if escolha.lower() == 'voltar':
        return main
    else:
        media_alunos()

def multiplos():
    cont = 0

    os.system('cls') 
    print("Este programa verifica se os números inseridos são crescentes ou decrescentes!")
    while True: 
        print("\nCaso queira sair, digite números idênticos.")
        print()
        if cont == 0:
            numero1 = int(input("Digite dois números: "))
            numero2 = int(input("Digite dois números: "))
            if numero1 == numero2:
             print("Números são iguais. Programa encerrado. ")
             break
            else:
                if numero1 > numero2:
                    print("Decrescente!")
                    cont += 1
                else:
                    print("Crescente!")
                    cont += 1
        else:
            numero1 = int(input("Digite outros dois números: "))
            numero2 = int(input("Digite outros dois números: "))
            if numero1 == numero2:
             print("Números são iguais. Programa encerrado. ")
             break
            else:
                if numero1 > numero2:
                    print("Decrescente!")
                    cont += 1
                else:
                    print("Crescente!")
                    cont += 1
            cont += 1

def calculadora_simples():
    while True:
        numero1 = float(input("Insira o primeiro número: "))
        numero2 = float(input("Insira o segundo número: "))

        print("O que quer fazer com esses números?")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")

        escolha = int(input("Calcular: "))

        if escolha == 1:
            resultado = numero1 + numero2
        elif escolha == 2:
            resultado = numero1 - numero2
        elif escolha == 3:
            resultado = numero1 * numero2
        elif escolha == 4:
            if numero2 == 0:
                resultado = "Erro: Divisão por zero!"
            else:
                resultado = numero1 / numero2
        else:
            resultado = "Opção inválida"

        print(f"Resultado: {resultado}")

        sair = input("Deseja voltar ao menu? [continuar] [voltar]: ").strip().lower()
        if sair == "voltar":
            print("Programa encerrado.")
            return mostrar_menu
        else:
            return calculadora_simples()
        
def menu_listas():
    import os
    os.system('cls')
    class FileStorage:
        def __init__(self, filename="storage.txt"):
            self.filename = filename
            if not os.path.exists(self.filename):
                with open(self.filename, "w") as f:
                    pass
        
        def add(self, item):
            with open(self.filename, "a") as f:
                f.write(item + "\n")
            print(f"'{item}' adicionado ao armazenamento.")
        
        def list_items(self):
            if os.stat(self.filename).st_size == 0:
                print("Armazenamento vazio.")
                return
            
            with open(self.filename, "r") as f:
                items = f.readlines()
            print("Itens armazenados:")
            for i, item in enumerate(items, 1):
                print(f"{i}. {item.strip()}")
        
        def search(self, query):
            with open(self.filename, "r") as f:
                items = f.readlines()
            
            results = [item.strip() for item in items if query in item]
            
            if results:
                print("Resultados da busca:")
                for result in results:
                    print(f"- {result}")
            else:
                print("Nenhum resultado encontrado.")
        
        def remove(self, query):
            with open(self.filename, "r") as f:
                items = f.readlines()
            
            new_items = [item for item in items if query not in item]
            
            if len(new_items) == len(items):
                print("Nenhum item removido.")
                return
            
            with open(self.filename, "w") as f:
                f.writelines(new_items)
            print(f"Itens contendo '{query}' foram removidos.")

    # Exemplo de uso
    def main():
        storage = FileStorage()
        while True:
            print("\n1. Adicionar item\n2. Listar itens\n3. Buscar item\n4. Remover item\n5. Entrada contínua de dados\n6. Voltar ao menu de exercícios")
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                item = input("Digite o item para adicionar: ")
                storage.add(item)
            elif opcao == "2":
                storage.list_items()
            elif opcao == "3":
                query = input("Digite o termo de busca: ")
                storage.search(query)
            elif opcao == "4":
                query = input("Digite o termo para remoção: ")
                storage.remove(query)
            elif opcao == "5":
                print("Modo de entrada contínua. Digite 'sair' para parar.")
                while True:
                    item = input("Digite algo: ")
                    if item.lower() == "sair":
                        break
                    storage.add(item)
            elif opcao == "6":
                print("Saindo...")
                break
            else:
                print("Opção inválida.")

    if __name__ == "__main__":
        main()

def labirinto():
    import heapq

    # Cidades (índices iguais ao da matriz)
    cidades = [
        "V. Castelo", "Leixões", "Aveiro", "F. da Foz", "Coimbra", "Leiria", "Lisboa",
        "Setubal", "Sesimbra", "Sines", "Baleal", "Lagos", "Portimão", "Vilamoura",
        "C. Sta Maria", "Tavira", "VRS António"
    ]

    # Matriz de distâncias simplificada (só valores principais da tabela)
    # Cada linha é uma cidade, valores 0 onde não há ligação direta
    matriz = [
        [0, 12, 61, 97, 121, 155, 313, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [12, 0, 43, 81, 105, 141, 305, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [61, 43, 0, 31, 51, 85, 241, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [97, 81, 31, 0, 26, 56, 205, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [121, 105, 51, 26, 0, 35, 177, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [155, 141, 85, 56, 35, 0, 147, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [313, 305, 241, 205, 177, 147, 0, 50, 66, 88, 147, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 50, 0, 23, 66, 141, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 66, 23, 0, 88, 112, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 88, 66, 88, 0, 63, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 147, 141, 112, 63, 0, 63, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 63, 0, 20, 26, 56, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 15, 46, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 15, 0, 31, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 56, 46, 31, 0, 16, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 11],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0]
    ]

    # Função de Dijkstra
    def dijkstra(matriz, inicio, fim):
        n = len(matriz)
        distancias = [float('inf')] * n
        distancias[inicio] = 0
        anterior = [None] * n
        fila = [(0, inicio)]

        while fila:
            dist, atual = heapq.heappop(fila)
            if atual == fim:
                break
            for vizinho, peso in enumerate(matriz[atual]):
                if peso > 0:
                    nova_dist = dist + peso
                    if nova_dist < distancias[vizinho]:
                        distancias[vizinho] = nova_dist
                        anterior[vizinho] = atual
                        heapq.heappush(fila, (nova_dist, vizinho))
        
        # Reconstruir caminho
        caminho = []
        atual = fim
        while atual is not None:
            caminho.append(cidades[atual])
            atual = anterior[atual]
        caminho.reverse()
        return caminho, distancias[fim]

    # Executar
    inicio = cidades.index("Leixões")
    fim = cidades.index("Tavira")
    caminho, distancia_total = dijkstra(matriz, inicio, fim)

    print("Melhor caminho:", " -> ".join(caminho))
    print("Distância total:", distancia_total, "km")

#COMENTÁRIO PARA SEPARAÇÃO E ORGANIZAÇÃO#

def opcao_vazia(numero):
    print(f"Opção {numero} ainda não implementada.")


menu_funcoes = {
    1: media_alunos,
    2: multiplos,
    3: calculadora_simples,
    4: menu_listas,
    5: labirinto
}

for i in range(6, 28):
    menu_funcoes[i] = lambda i=i: opcao_vazia(i)


def mostrar_menu():
    print("=== Menu de Exercícios (rencaldas) ===")
    print("1. media_alunos")
    print("2. multiplos")
    print("3. calculadora_simples")
    print("4. menu_listas")
    print("5. labirinto")
    for i in range(6, 28):
        print(f"{i}. Opção {i}")


def main():

    while True:
        os.system('cls')
        mostrar_menu()
        escolha = input("Escolha um número (ou '0' para sair): ")
        if escolha == '0':
            print("Saindo do menu...")
            break
        elif escolha.isdigit() and 1 <= int(escolha) <= 27:
            numero = int(escolha)
            menu_funcoes[numero]()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
