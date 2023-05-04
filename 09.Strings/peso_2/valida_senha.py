especiais=['?', '!', '@', '#', '$', '%', '&', '*']
def valida_senha(senha):
    car_esp=[]
    car_rep=[]
    if len(senha)<8:
        return False
    else:
        for i in senha:
            if i in especiais:
                if i not in car_esp:
                    car_esp.append(i)
        if len(car_esp)<2:
            return False
        else:
            for i in range(len(senha)):
                if senha[i] == senha[i+1]:
                    return False
            else:
                return True
                
senha='abcdef?!' 
senha='?abcdeef!'
print(valida_senha(senha))
