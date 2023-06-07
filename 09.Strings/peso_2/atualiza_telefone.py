def atualiza_telefone(numero):
    nove='9'
    if len(numero)==10 and '-' in numero:
        return numero
    elif len(numero)==9 and '-' not in numero:
        return numero
    elif len(numero)==9 and '-' in numero:
        novo_numero=nove+numero
        return novo_numero
    else:
        novo_numero=nove+numero
        return novo_numero



