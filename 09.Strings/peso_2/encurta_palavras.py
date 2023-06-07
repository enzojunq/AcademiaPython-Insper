def encurta_palavra(palavra, vogais):
    for letra in vogais:
        palavra = palavra.replace(letra, '')
    return palavra

vogais = ['a', 'e', 'i', 'o', 'u']

x = True
while x:
    palavra = input()
    if palavra == 'fim':
        print('Até a próxima')
        x = False
    else:
        print(encurta_palavra(palavra, vogais))
