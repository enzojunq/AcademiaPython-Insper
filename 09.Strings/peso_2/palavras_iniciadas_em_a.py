palavras=[]
p=input()
while p!='fim':
    palavras.append(p)
    p=input()
for palavra in palavras:
    if palavra[0]=='a':
        print(palavra)
