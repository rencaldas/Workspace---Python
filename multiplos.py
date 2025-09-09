
cont = 0

while True:
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
