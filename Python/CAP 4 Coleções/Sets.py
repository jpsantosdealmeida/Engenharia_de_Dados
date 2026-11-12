# Set é um conjunto {} e ele armazena valores únicos

numeros = [1,1,2,3,4] # Repete o 1

set_numeros = set(numeros) # Retorna 1,2,3,4 ( 1 vez o 1 somente )

# Adicionar valores
set_numeros.add(10)


conj_1 = {1,2,3}
conj_2 = {1,4,5}

# Podemos fazer operações com os conjuntos

# Interseção o que tem em comum nos 2 sets
print(conj_1.intersection(conj_2))

# O que tem de diferente do conj 1 para o 2 [ 2, 3 ]
print(conj_1.difference(conj_2))
# O que tem de diferente do conj 2 para o 1 [ 2, 3 ]
print(conj_2.difference(conj_1))
# Unir 2 conjuntos: Resultado [1,2,3,4,5]
print(conj_1.union(conj_2))
