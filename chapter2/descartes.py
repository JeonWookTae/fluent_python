colors = ['red', 'blue']
sizes = ['s', 'm', 'xl']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

symbols = '$&@%*'
print(tuple(ord(symbol) for symbol in symbols))

import array
print(array.array('I', (ord(symbol) for symbol in symbols)))

for tshirts in ('%s %s'%(c,s) for c in colors for s in sizes):
    print(tshirts)