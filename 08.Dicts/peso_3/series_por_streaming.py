def series_por_streaming(plataformas,atores,titulos):
    dict={}
    for i in range(len(plataformas)):
        if plataformas[i] not in dict:
            dict[plataformas[i]]=[{'performer':atores[i],'title':titulos[i]}]
        else:
            dict[plataformas[i]].append({'performer':atores[i],'title':titulos[i]})
    return dict


plataformas=['Disney+', 'Netflix', 'Prime Video', 'Disney+', 'Netflix']
atores = ['Pedro Pascal', 'Jenna Ortega', 'Laura Bailey', 'Tatiana Maslany', 'Gaten Matarazzo']
titulos = ['The Mandalorian', 'Wandinha', 'The Legend of Vox Machina', "She-Hulk", 'Stranger Things']
print(series_por_streaming(plataformas,atores,titulos))