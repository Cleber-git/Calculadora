import math
def miniMax(arr):
    somamin = arr[1:].sum()
    somamax = arr[:-2].sum()
    print(f'{somamin} {somamax}')

# miniMax([1, 2, 3, 4, 5])
maximo = []
minimo = []
lista = [1, 2, 3, 4, 5]
minimo.append(min(lista))
for c in range(1,4):
    minimo.append(min(lista[c:]))

for c in range(1, 5):
    maximo.append(max(lista[-1:c]))

print(maximo)
print(minimo)

