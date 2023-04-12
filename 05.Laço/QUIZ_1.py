import math
def altura_do_predio(comprim,angulo):
    angulo=math.radians(angulo)
    tangente=math.tan(angulo)
    altura=tangente*comprim
    return altura
print(altura_do_predio(100,30))