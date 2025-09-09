def ler_matriz_csv(arquivo):
    matriz = []
    with open(arquivo, 'r') as f:
        for linha in f:
            valores = linha.strip().split(',')
            matriz.append([float(v) for v in valores])
    return matriz

def prim_mst(graph):
    num_vertices = len(graph)
    selected = [False] * num_vertices
    selected[0] = True
    mst_edges = []
    
    while len(mst_edges) < num_vertices - 1:
        min_edge = (None, None, float('inf'))
        for i in range(num_vertices):
            if selected[i]:
                for j in range(num_vertices):
                    if not selected[j] and graph[i][j] != 0 and graph[i][j] < min_edge[2]:
                        min_edge = (i, j, graph[i][j])
        if min_edge[0] is not None:
            mst_edges.append(min_edge)
            selected[min_edge[1]] = True
        else:
            print("Grafo desconexo! Não é possível formar uma árvore geradora mínima completa.")
            break
    return mst_edges

# Lendo a matriz do arquivo CSV
arquivo = 'C:/Users/Pichau/Desktop/Progamer/Workspace - Python/grafo.csv'  #substitua pelo seu arquivo
matriz = ler_matriz_csv(arquivo)

# Rodando o Prim
mst = prim_mst(matriz)
for edge in mst:
    print(f"Aresta {edge[0]} - {edge[1]} com peso {edge[2]}")
