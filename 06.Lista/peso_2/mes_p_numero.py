meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
nome=input()
for i in range(len(meses)):
    if nome == meses[i]:
        print(i+1)
