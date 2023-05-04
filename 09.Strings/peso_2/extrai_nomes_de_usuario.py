def extrai_nomes_de_usuarios(lista_emails:list):
    nomes=[]
    for emails in lista_emails:
        usuario=emails.split('@')
        nomes.append(usuario[0])
    return nomes

lista=['fulano123@email.com.br', 'sicrano@outromail.com', 'beltrano.silva@mail.com.pt']
print(extrai_nomes_de_usuarios(lista))