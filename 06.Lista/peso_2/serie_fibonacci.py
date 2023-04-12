def calcula_fibonacci(n):
    n+=1
    fibonacci=[0,1]
    for i in range(2,n):
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
    del fibonacci[0]
    return fibonacci
print(calcula_fibonacci(4))