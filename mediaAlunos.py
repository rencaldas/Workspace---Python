alunos = []
soma_medias = 0
aprovados = 0
reprovados = 0

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
