def eh_fibonacci(list):
    
    fibonacci=[]
    for i in range(len(list)-2):
        if list[i]+list[i+1]==list[i+2]:
            fibonacci.append(list[i])
    if len(list)==2 or len(list)==1 or len(list)==0:
        return False
    elif len(fibonacci)==len(list)-2:
        return True
    else: 
        return False