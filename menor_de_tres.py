# Problema "dardo"

# Entrada dos valores
instancia1 = float(input("Digite a primeira distância: "))
instancia2 = float(input("Digite a segunda distância: "))
instancia3 = float(input("Digite a terceira distância: "))

# Verificar qual é a maior distância
if instancia1 > instancia2 and instancia1 > instancia3:
    maiorDistancia = instancia1
elif instancia2 > instancia1 and instancia2 > instancia3:
    maiorDistancia = instancia2
else:
    maiorDistancia = instancia3

# Exibir o resultado
print("MAIOR DISTÂNCIA = " + str(maiorDistancia))
