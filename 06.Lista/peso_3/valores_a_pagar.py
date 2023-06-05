def valores_a_pagar(franquias, despachadas):
    valores = [0] * len(franquias)

    for i in range(len(despachadas)):
        index = despachadas[i][0]
        n_malas = franquias[index][0]
        peso_mala = franquias[index][1]
        malas_extra = len(despachadas[i][1:]) - n_malas

        for j in despachadas[i][1:]:
            quilo_extra = j - peso_mala
            if quilo_extra > 0:
                valores[index] += 50 * quilo_extra

        if malas_extra > 0:
            valores[index] += 300 * malas_extra

    return valores

franquias = [ [2, 23] , [1, 32], [1, 10], [3, 23] ]
despachadas = [ [2, 10], [0, 21, 24], [1, 30, 33], [3, 22, 23] ]
print(valores_a_pagar(franquias,despachadas))