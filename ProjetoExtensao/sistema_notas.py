alunos = {}

def cadastrar_aluno(nome, matricula):
    if matricula in alunos:
        return "Erro: Matrícula já cadastrada."
    alunos[matricula] = {"nome": nome, "notas": []}
    return "Aluno cadastrado com sucesso."

def adicionar_nota(matricula, nota):
    if matricula not in alunos:
        return "Erro: Matrícula não encontrada."
    if nota < 0 or nota > 10:
        return "Erro: Nota inválida."
    
    alunos[matricula]["notas"].append(nota)
    return "Nota adicionada com sucesso."

def calcular_media(matricula):
    if matricula not in alunos:
        return "Erro: Matrícula não encontrada."
    notas = alunos[matricula]["notas"]
    if len(notas) == 0:
        return "Erro: Nenhuma nota registrada."
    #    Bug proposital: média incorreta se só houver 1 nota
    if len(notas) == 1:
        media = notas[0]
    else:
        media = sum(notas) / len(notas)
    status = "Aprovado" if media >= 7 else "Reprovado"
    return f"Média: {media:.2f} - {status}"

def listar_alunos():
    if not alunos:
        return "Nenhum aluno cadastrado."
    resultado = ""
    for m, info in alunos.items():
        resultado += f"{info['nome']} ({m}) - Notas: {info['notas']}\n"
    return resultado

# Interface
if __name__ == "__main__":
    while True:
        print("\n=== Sistema de Notas ===")
        print("1. Cadastrar aluno")
        print("2. Adicionar nota")
        print("3. Calcular média")
        print("4. Listar alunos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            matricula = input("Matrícula: ")
            print(cadastrar_aluno(nome, matricula))
        elif opcao == "2":
            matricula = input("Matrícula: ")
            nota = float(input("Nota: "))
            print(adicionar_nota(matricula, nota))
        elif opcao == "3":
            matricula = input("Matrícula: ")
            print(calcular_media(matricula))
        elif opcao == "4":
            print(listar_alunos())
        elif opcao == "5":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")
