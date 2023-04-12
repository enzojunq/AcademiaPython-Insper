def PiWallis(n):
    i=1
    p=1 
    num=2
    den=1
    while i<=n:
        p*=num/den
        if i%2==0:
            num+=2
        else:
            den+=2
        i+=1
    return 2*p
print(PiWallis(2))
        