def usuarios_por_pais(emails,enderecos):
    end_por_paises={}
    for email in emails:
        provedor=email.split('@')
        for endereco,pais in enderecos.items():
            if endereco in provedor[1]:
                if pais not in end_por_paises:
                    end_por_paises[pais]=[provedor[0]]
                else:
                    end_por_paises[pais].append(provedor[0])

    return end_por_paises

emails= ['usuario1@insper.edu.br', 'usuario2@uma.pt', 'usuario3@kth.se', 'usuario4@usp.br']
enderecos= {
    'pt': 'Portugal',
    'br': 'Brasil',
    'se': 'Suécia'
}

print(usuarios_por_pais(emails,enderecos))