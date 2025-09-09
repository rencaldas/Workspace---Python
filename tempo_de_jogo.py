# Entrada de dados
hora_inicial = int(input("Hora inicial do jogo: "))
hora_final = int(input("Hora final do jogo: "))

# Verifica se a entrada está dentro do intervalo válido (0 a 23)
if 0 <= hora_inicial <= 23 and 0 <= hora_final <= 23:
    # Calcula a duração
    if hora_inicial < hora_final:
        duracao = hora_final - hora_inicial
    else:
        duracao = (24 - hora_inicial) + hora_final

    # Exibe o resultado
    print(f"O JOGO DUROU {duracao} HORA(S)")
else:
    print("Erro: Insira horas válidas entre 0 e 23.")
