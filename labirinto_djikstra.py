# Labirinto representado como grafo com conexões válidas
labirinto = {
    4: [5, 9],
    5: [4, 6, 19],
    6: [5, 7],
    7: [6],
    9: [4, 10],
    10: [9, 11],
    11: [10, 12],
    12: [11, 13],
    13: [12],
    14: [13],
    15: [14, 21],
    16: [17, 22],
    17: [16, 18],
    18: [17, 19],
    19: [5, 18, 20],
    20: [19, 21, 27],
    21: [15, 20],
    22: [16, 23],
    23: [22, 24],
    24: [23, 25],
    25: [24, 26, 32],
    26: [25, 27, 40],
    27: [20, 26, 28],
    28: [27],
    29: [30],
    30: [29, 31],
    31: [30, 32],
    32: [31, 25, 33],
    33: [32, 34],
    34: [33, 35],
    35: [34],
    36: [29],
    37: [38],
    38: [37, 39],
    39: [38, 40, 43],
    40: [26, 39],
    41: [42],
    42: [41],
    43: [39, 44],
    44: [43, 49],
    45: [46],
    46: [45],
    47: [48],
    48: [47],
    49: [44, 50],
    50: [49],
    51: [52],
    52: [51, 53],
    53: [52],
    54: [55],
    55: [54, 56],
    56: [55],
    57: [58],
    58: [57],
    59: [60],
    60: [59, 61],
    61: [60, 62],
    62: [61, 63],
    63: [62]
}

inicio = 4
fim = 50

# Variáveis para registrar o progresso
caminho_correto = []
caminhos_errados = []

def dfs(atual, destino, visitado, caminho):
    visitado.add(atual)
    caminho.append(atual)

    if atual == destino:
        caminho_correto.extend(caminho)
        return True

    for vizinho in labirinto.get(atual, []):
        if vizinho not in visitado:
            if dfs(vizinho, destino, visitado, caminho):
                return True

    # Caminho sem saída
    caminhos_errados.append(list(caminho))
    caminho.pop()
    return False

# Executa DFS
dfs(inicio, fim, set(), [])

# --- Relatório Final ---
print("\nCaminhos errados testados:\n")
for i, caminho in enumerate(caminhos_errados, 1):
    print(f"Erro {i}: {' -> '.join(f'{n:02}' for n in caminho)}")

print("\nCaminho correto encontrado:\n")
print(" -> ".join(f"{n:02}" for n in caminho_correto) + " -> B")
