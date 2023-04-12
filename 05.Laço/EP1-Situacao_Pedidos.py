def meta_atingida (lim_reclam, lim_just, prop_reclam, prop_just):
    if prop_reclam < lim_reclam and prop_just < lim_just:
        return True
    else:
        return False
    
def classifica_pedido(valor,dias,tamanho,avarias,capital):
    if valor<=1000:
        if dias<=1:
            if valor<=150:
                if avarias=='n' or avarias=='N':
                    return 'normal'
                else:
                    return 'reclamacao'
            else:
                return 'reclamacao'
        else:
            return 'reclamacao'
    else:
        if dias<=10:
            if avarias=='n' or avarias=='N':
                if valor<=10000:
                    if valor<=5000:
                        if capital=='n' or capital=='N':
                            return 'normal'
                        elif tamanho=='p' or tamanho=='P':
                            return 'reclamacao'
                        else:
                            return 'normal'
                    else:
                        return 'reclamacao'
                else:
                    return 'justica'
            else:
                return 'justica'
        else:
            return 'justica'
        
soma_reclamacao=0
soma_normal=0
soma_justica=0
total=0

limite_reclamacao=float(input("Qual o limite máximo de reclamações? "))
limite_justica=float(input("Qual o limite máximo de pedidos? "))
novo_pedido=input("Deseja informar novo pedido? ")
if novo_pedido=='s' or novo_pedido=='S':    
    while novo_pedido=='S'or novo_pedido=='s':
        valor_pedido=float(input("Qual o valor do pedido? "))
        atraso_pedido=float(input("Quantos dias de atraso? "))
        tamanho_pedido=input("Qual tamanho [p/P/g/G]? ")
        avaria_pedido=input("Tem avaria [s/S/n/N]? ")
        entrega_capital=input("Entrega em capital [s/S/n/N]? ")
        if classifica_pedido(valor_pedido,atraso_pedido,tamanho_pedido,avaria_pedido,entrega_capital)=='reclamacao':
            soma_reclamacao+=1
            total+=1
        elif classifica_pedido(valor_pedido,atraso_pedido,tamanho_pedido,avaria_pedido,entrega_capital)=='normal':
            soma_normal+=1
            total+=1
        else:
            soma_justica+=1
            total+=1
        print(f'Pedido classificado como {classifica_pedido(valor_pedido,atraso_pedido,tamanho_pedido,avaria_pedido,entrega_capital)}')
        novo_pedido=input("Deseja informar novo pedido? ")
    print(f'Pedidos por classificação: {soma_reclamacao:02d} reclamacao, {soma_normal:02d} normal, {soma_justica:02d} justica')
    if soma_reclamacao == 0:
        classifica_reclamacao=0
    else:
        classifica_reclamacao=soma_reclamacao*100/total

    if soma_normal == 0:
        classifica_normal=0
    else:
        classifica_normal=soma_normal*100/total
    if soma_justica == 0:
        classifica_justica=0
    else:
        classifica_justica=soma_justica*100/total
    print(f'Pedidos por classificação: {classifica_reclamacao:0>5.2f}% reclamacao, {classifica_normal:0>5.2f}% normal, {classifica_justica:0>5.2f}% justica')
    

    if meta_atingida(limite_reclamacao,limite_justica,classifica_reclamacao/100,classifica_justica/100): 
        print("Meta atingida!")
    else:
        print("Meta nao atingida!")
        
    

