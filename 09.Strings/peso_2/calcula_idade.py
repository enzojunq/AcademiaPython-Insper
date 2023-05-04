def calcula_idade(data_nasc,data_post):

    anos=0

    split_nasc=data_nasc.split('/')
    split_post=data_post.split('/')

    dia_nasc=split_nasc[0]
    mes_nasc=split_nasc[1]
    ano_nasc=split_nasc[2]

    dia_post=split_post[0]
    mes_post=split_post[1]
    ano_post=split_post[2]

    if int(mes_post)>int(mes_nasc):
        anos=int(ano_post)-int(ano_nasc)
    else:
        anos=int(ano_post)-int(ano_nasc)-1

    if int(mes_post)==int(mes_nasc):
        if int(dia_nasc)>int(dia_post):
            anos=int(ano_post)-int(ano_nasc) - 1
        else:
            anos=int(ano_post)-int(ano_nasc) 

    
    return anos


dta_nasc='14/02/1989'

dta_post='13/02/2021'

print(calcula_idade(dta_nasc,dta_post))