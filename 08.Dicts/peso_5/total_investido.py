investidores={}
    

# def repassa_investimentos(empresas: dict, investidores: dict, associado: str, valor_de_mercado: float, valor_porcentagem: float):
#     repasse = valor_de_mercado * valor_porcentagem / 100
#     for associado, valor_porcentagem in empresas[associado]['associados'].items():
#         if associado not in empresas:
#             if associado not in investidores:
#                 investidores[associado] = repasse * valor_porcentagem / 100
#             else:
#                 investidores[associado] += repasse * valor_porcentagem / 100
#         else:
#             repassa_investimentos(empresas, investidores,
#                                   associado, repasse, valor_porcentagem)

# def repassa_investimentos(valor,associados)


def soma_investimento(empresas:dict):
    for empresa,dados in empresas.items():
        valor_de_mercado=dados['valor de mercado']
        associados = dados['associados']
        for associado,valor in associados.items():
            # if associado not in empresas:
            if associado not in investidores:
                investidores[associado]=valor*valor_de_mercado/100
            else:
                investidores[associado]+=valor*valor_de_mercado/100
            # else:
            #     repassa_investimentos(valor,associados)

    empresas_socias={}
    pessoas_fisicas={}
    for socio, valor in investidores.items():
        if socio in empresas:
            empresas_socias[socio]=0
   
    for socio, valor in investidores.items():
        if socio not in empresas:
            pessoas_fisicas[socio]=valor 

    socios_por_empresa={}
    for nome_empresa, dados_empresa in empresas.items():
        for nome_socio, participacao in dados_empresa['associados'].items():     
            if nome_empresa not in socios_por_empresa:
                socios_por_empresa[nome_empresa]=[[nome_socio,participacao]]
            else:
                socios_por_empresa[nome_empresa].append([nome_socio,participacao])
    
    # print(socios_por_empresa)
    # print(investidores)

    i=0 
    while i != len(empresas_socias):
        for empresa in empresas_socias:
            for socio,dados in socios_por_empresa.items():
                return 0

        
        
    







    print( pessoas_fisicas,empresas_socias)     




empresas={
    'acme corporation inc': {
        'valor de mercado': 4560000.00,
        'associados': {
            'joao silva matoso': 30,   # 30% da empresa
            'maria santana alves': 70  # 70% da empresa
        }
    },
    'insper solid investiment': {
        'valor de mercado': 8950000.00,
        'associados': {
            'maciel fina pessoa': 10,  # 10% da empresa
            'insper junior ltda': 80,  # 80% da empresa
            'marcio massado': 5,       # 5% da empresa
            'jair designa broncado': 5 # 5% da empresa
        }
    },
    'insper junior ltda':  {
        'valor de mercado': 40200100.00,
        'associados': {
            'maciel fina pessoa': 20, # 20% da empresa
            'joao silva matoso': 30,  # 30% da empresa
            'dario finado': 40,       # 40% da empresa
            'acme corporation inc': 10 # 10% da empresa
        }
    }
}
soma_investimento(empresas)