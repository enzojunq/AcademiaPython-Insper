resultado=0
n=0
'''while n < 100:
    resultado+=1/(2**n)
    n=n+1'''
for n in range(100):
    resultado+=1/(2**n)
print(resultado)