import math

def distancia_projetil(v, ang, y):
    d = ((v**2)/(2*9.8)) * (1 + math.sqrt(1 + ((2*9.8*y) / (v**2)) * ((math.sin(ang))**2))) * math.sin(2*ang)
    return d

print(distancia_projetil(3.13,0.52,1))


def calcula_distancia_do_projetil2(velocidade, angulo, altura_inicial):
    gravidade = 9.8

    distancia = ((velocidade ** 2) / (2 * gravidade)) * (1 + math.sqrt(1 + (2 * gravidade * altura_inicial) / (velocidade ** 2 * (math.sin(angulo)**2)))) * math.sin(2 * angulo)

    return distancia

    
print(distancia_projetil(3.13,0.52,1))


def calcula_distancia_do_projetil3(vel,angulo,altura):
    vel=vel*vel
    g=2*9.8
    d = (vel / g) * (1 + math.sqrt(1 + ((g*altura/vel) * math.sin(angulo)*math.sin(angulo))))*math.sin(2*angulo)
    return d 
    
print(calcula_distancia_do_projetil3(0.13,0.52,1))