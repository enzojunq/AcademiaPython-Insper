def verifica_preco(livro_desejado,livros,cores):
    if livro_desejado in livros:
        cor=livros[livro_desejado]
        preco=cores[cor]
        return preco
    else:
        return 0 