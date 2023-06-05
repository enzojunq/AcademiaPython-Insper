def analisar_pilhas(modelos, pilhas):
    saida = []
    for pilha in pilhas:
        if pilha[0] not in modelos:
            saida.append('E')
            continue
        marca = pilha[0]
        tipo = pilha[1]
        volts_pilha = pilha[2]
        
        if marca in modelos and tipo in modelos[marca]:
            info = modelos[marca][tipo]
            limite_volts = info['volts'] - (info['limite'] * info['volts'])
            if volts_pilha > limite_volts:
                saida.append('N')
            elif volts_pilha < limite_volts and info['recarregavel']:
                saida.append('R')
            elif volts_pilha < limite_volts and not info['recarregavel']:
                saida.append('D')
        else:
            saida.append('E')
    
    return saida


modelos = {'elgin': {'htrkexzs': {'capacidade': '2486 mah', 'volts': 23.416279939976683, 'limite': 0.05714898854289095, 'recarregavel': True}, 'samgwxkh': {'capacidade': '4227 mah', 'volts': 16.418392707359796, 'limite': 0.22471893755679234, 'recarregavel': False}}}

pilhas = [['elgin', 'samgwxkh', 13.434630243020768], ['elgin', 'samgwxkh', 0.6117927804077891], ['elgin', 'samgwxkh', 13.305141431752569]]

print(analisar_pilhas(modelos, pilhas))
