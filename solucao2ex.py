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

    sair = input("Quer sair? [s]sim [n]não ").strip().lower()
    if sair == "s":
        print("Programa encerrado.")
        break
