def tamanho_minimo(string,minimo):
    palavras = string.split(' ')
    palavras_minimo = []
    for palavra in palavras:
        if len(palavra) > minimo:
            palavras_minimo.append(palavra)
    return palavras_minimo