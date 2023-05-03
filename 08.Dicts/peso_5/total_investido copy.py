investidores={}
    

def repassa_investimentos(empresas: dict, investidores: dict, associado: str, valor_de_mercado: float, valor_porcentagem: float):
    repasse = valor_de_mercado * valor_porcentagem / 100
    for associado, valor_porcentagem in empresas[associado]['associados'].items():
        if associado not in empresas:
            if associado not in investidores:
                investidores[associado] = repasse * valor_porcentagem / 100
            else:
                investidores[associado] += repasse * valor_porcentagem / 100
        else:
            repassa_investimentos(empresas, investidores,
                                  associado, repasse, valor_porcentagem)




def soma_investimento(empresas:dict):
    for empresa,dados in empresas.items():
        valor_de_mercado=dados['valor de mercado']
        associados = dados['associados']
        for associado,valor in associados.items():
            if associado not in empresas:
                if associado not in investidores:
                    investidores[associado]=valor*valor_de_mercado/100
                else:
                    investidores[associado]+=valor*valor_de_mercado/100
            else:
                repassa_investimentos(empresas, investidores, associado, valor_de_mercado,valor)

    return investidores


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
print(soma_investimento(empresas))