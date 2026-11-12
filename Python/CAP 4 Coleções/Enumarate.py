# Enumarate devolve o indice da iteração, podemos informar qual valor o index inicia

numeros = [1,2,3,4,5]

for numero in numeros:
    print(f'Número: {numero}')

print(30 * '-=')
for index,numero in enumerate(numeros,0): 
    print(f'Número: {numero} | Index: {index}')