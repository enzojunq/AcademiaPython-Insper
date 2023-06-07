import re
def verifica_ganhador(frase, jogadores):
    frase_nova2 = re.sub(r'[^\w\s]', '', frase)
    restricoes=['.',',',':',';']
    frase_nova=frase.lower()
    for restricao in restricoes:
        frase_nova=frase_nova.replace(restricao,'')
        
    frase_nova = frase_nova.split(' ')
    pontos_jogadores={}
    for palavra in frase_nova:
        for jogador,palavras_jogador in jogadores.items():
            for palavra_jogador in palavras_jogador:
                if palavra == palavra_jogador:
                    pontos_jogadores.setdefault(jogador,0)
                    pontos_jogadores[jogador]+=1

    return pontos_jogadores

frase = 'Algum tempo hesitei se devia abrir estas memórias pelo princípio ou pelo fim, isto é, se poria em primeiro lugar o meu nascimento ou a minha morte. Suposto o uso vulgar seja começar pelo nascimento, duas considerações me levaram a adotar diferente método: a primeira é que eu não sou propriamente um autor defunto, mas um defunto autor, para quem a campa foi outro berço; a segunda é que o escrito ficaria assim mais galante e mais novo. Moysés, que tambem contou a sua morte, não a poz no introito, mas no cabo: diferença radical entre este livro e o Pentateuco.'


jogadores={'maria': ['me', 'a', 'minha', 'a']}

print(verifica_ganhador(frase,jogadores))