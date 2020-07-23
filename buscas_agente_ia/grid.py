from pprint import pprint

########################
# add node
########################
def add(adj_list, a, b):
    adj_list.setdefault(a, []).append(b)
    adj_list.setdefault(b, []).append(a)

########################
# lista de adjc.
########################
def create_adj_list(matrix):
    #print("create_adj_list")
    #pprint(matrix)
    
    # percorrendo a matriz e criando uma lista de adj
    adj_list = {}
    for i in range(len(matrix)): # linhas
        for j in range(len(matrix[i])): #colunas
            if j < len(matrix[i])-1:
                add(adj_list, (i,j), (i, j+1))
            if i < len(matrix[i])-1:
                add(adj_list, (i,j), (i + 1, j))

    # removendo todas as celulas com valor 1 (bloqueio)
    adj_list_filt = {}
    #for id, value in adj_list.items():
    #    if matrix[id[0]][id[1]]!=1:
    #        print("vai remover", id,"->", id[0],id[1])
    #        adj_list_filt[id] = [(coord[0], coord[1]) for coord in value if matrix[coord[0]][coord[1]] != 1]
    #return adj_list_filt

    # eliminando os caminhos possiveis que sejam 1
    for id, value in adj_list.items():
        adj_list_filt[id] = [(coord[0], coord[1]) for coord in value if matrix[coord[0]][coord[1]] != 1]

    # eliminando os nos que sejam 1

    adj_list_final = {id: value for id, value in adj_list_filt.items() if matrix[id[0]][id[1]] != 1}

    #for id, value in adj_list_filt.items():
    #    if matrix[id[0]][id[1]] == 1:
    #        print("vai remover:", id)
    #        adj_list_filt.pop(id)
    #return adj_list_filt
    
    #pprint(adj_list_final)
    #print("FIM create_adj_list")
    return adj_list_final
