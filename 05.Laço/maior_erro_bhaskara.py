import math
angulo=1
diferenca=0
angulo_maior_erro=0

while (angulo<90):
    seno=math.sin(math.radians(angulo))
    seno2=(4*angulo*(180-angulo))/(40500-angulo*(180-angulo))
    
    if(diferenca<abs(seno-seno2)):  
        diferenca=abs(seno-seno2)
        angulo_maior_erro=angulo
    angulo+=1
print(angulo_maior_erro)