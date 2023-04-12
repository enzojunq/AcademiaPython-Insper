def eh_identidade(matriz):
    if len(matriz) == len(matriz[0]):
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] == 1 and j != i:
                    return False
                elif 1 not in matriz[i] or matriz[i][j] < 0:
                    return False

        return True

    return False