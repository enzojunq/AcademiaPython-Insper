def maior_abobora(especie,fazendeiros):
    maior=0
    indice=-1
    if len(fazendeiros)==1 and len(fazendeiros[0])==0:
        return -1
    for i in range(len(fazendeiros)):
        for aboboras in fazendeiros[i]:
            if aboboras[1]==especie:
                if aboboras[0]>maior:
                    maior=aboboras[0]
                    indice=i

    return indice
    
especie='japonesa'
fazendeiros=[
  [[2.3, 'kabotia']],
  [[6.2, 'kabotia'], [5.5, 'moranga'], [2.5, 'japonesa'], [1.4, 'moranga']],
  [[4.2, 'moranga'], [9.2, 'moranga'], [14.2, 'moranga']],
  [[5.6, 'kabotia'], [16.2, 'kabotia']],
  [[5.5, 'japonesa'], [12.2, 'japonesa'], [12.3, 'japonesa']],
  [[1.2, 'moranga'], [9.2, 'japonesa'], [8.5, 'japonesa']],
]

print(maior_abobora(especie,fazendeiros))