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
