port2eng = {'couve': 'kale', 'repolho': 'cabbage', 'brocolis': 'broccoli'}
for port in port2eng:
    eng = port2eng[port]
    print('{0} é {1}'.format(port, eng))

port2eng = {'couve': 'kale', 'repolho': 'cabbage', 'brocolis': 'broccoli'}
for port in port2eng.keys():
    eng = port2eng[port]
    print('{0} é {1}'.format(port, eng))

port2eng = {'couve': 'kale', 'repolho': 'cabbage', 'brocolis': 'broccoli'}
for eng in port2eng.values():
    print(eng)

port2eng = {'couve': 'kale', 'repolho': 'cabbage', 'brocolis': 'broccoli'}
for port, eng in port2eng.items():
    print('{0} é {1}'.format(port, eng))