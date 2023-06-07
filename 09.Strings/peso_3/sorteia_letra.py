from random import choice


def sorteia_letra(palavra: str, restriction: list) -> str:
    restriction+=['.', ',', '-', ';', ' ']
    saida=''
    for letra in palavra.lower():
        if letra not in restriction:
            saida+=letra
    return '' if not saida else choice(saida)

lista = ['a', 'r']

palavra= 'atirei o pau no gato'

print(sorteia_letra(palavra,lista))
