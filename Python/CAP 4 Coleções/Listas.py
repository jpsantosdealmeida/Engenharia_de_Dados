preco_1 = 10
preco_2 = 20
preco_3 = 30

# Listas
precos = [10, 20, 30, 40, 50, 60, 100, 250, 230, 560, 23, 74]
print(precos[0])  # Índice
print(precos[precos.index(100)])

# Listas no Python são dinâmicas (aceitam qualquer tipo de dado)
itens = [1, 3, 6, 'Olá', 'Café', True, 10.6]
print(itens[4])

# Maneiras diferentes de gerar uma lista

# Multiplicação de valores (repetição)
lista_de_noves = [9] * 10
lista_de_testes = ['Teste'] * 10

print(lista_de_noves)
print(lista_de_testes)

# Usando gerador Range (Sequência)
# 1 até 29
faixa_de_numeros = list(range(30))
print(faixa_de_numeros)

# Gerar a partir de strings
print(list('Bem-vindo ao treinamento'))

# Lista de lista (matriz)
matriz_de_nomes = [['Carol', 30], ['Marcus', 50]]

print(matriz_de_nomes[0])
print(matriz_de_nomes[0][0])
print(matriz_de_nomes[1][0])



''' 

Desafio #1 Crie uma lista que tenha os nomes dos 3 objetos que você mais usa durante o dia e imprima ele na tela

Desafio #2 Usando apenas uma linha de código, crie uma lista de 10 a 131

Desafio #3 Imprima na tela o resultado da combinação da lista do desafio 1 e desafio 2

Desafio #4 Crie uma lista de listas(matriz) que tenha os nomes dos 3 objetos

 que você mais usa durante o dia, mas agora dentro de cada item você vai colocar 

uma informação extra, coloque o valor em reais desse objeto também e imprima ele 

na tela  '''

#1
objetos = ['papel','caneta','celular']
print(objetos)
#2
l = list(range(10,131))
print(l)
#3
l.extend(objetos)
print(l)
#4
matriz = [['papel',1],['caneta',2],['celular',3]]