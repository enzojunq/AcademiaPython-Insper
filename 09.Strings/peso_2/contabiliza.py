numeros='0123456789'
def contabiliza(lista_doacoes:dict):
    total={}
    for pessoas,itens in lista_doacoes.items():
        for item in itens:
            item=item.split(' ')
            nome_item=item[1:]
            nome_item=' '.join(nome_item)
            if nome_item not in total:
                total[nome_item]=int(item[0])
            else:
                total[nome_item]+=int(item[0])



    return total


pessoas={
    'joaquim': [
        '02 caixa de bananinha',
        '3 carrinho',
        '4 refrigerante'
    ],
    'joana': [
        '2 carrinho',
        '3 quebra-cabeça',
        '1 caixa de cocada'
    ],
    'sebastião': [
        '1 refrigerante',
        '1 quebra-cabeça'
    ],
}
print(contabiliza(pessoas))