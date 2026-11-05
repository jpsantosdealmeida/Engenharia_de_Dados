lista = [2,10,50,4,8,1,0,441,71,8,7,9]
# a lista fica de trás para frete
lista.reverse()

# a lista fica ordenada crescente
lista.sort()
# a lista fica ordenada decrescente
lista.sort(reverse=True)

# from itertools import zip_longest
# para iterar em listas cujo o número de objetos sejam diferentes

# utizamos zip para iterar em 2 listas

## DESAFIO 1
'''
Usando as listas abaixo:

produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']

precos = ['R$500,00', 'R$1500,00', 'R$2700,00', 'R$5000,00']

Estamos extraindo preços de um site de produtos e queremos armazenar as informações encontradas, porém a pesquisa foi encontrada em momentos diferentes, assim acabamos com duas listas diferentes, favor criar uma mensagem que diz o nome e valor produto, como as mensagens abaixo:

Produto: Produto 1 encontrado no valor de R$500,00

Produto: Produto 2 encontrado no valor de R$1500,00

Produto: Produto 3 encontrado no valor de R$2700,00

Produto: Produto 4 encontrado no valor de R$5000,00

Produto: Produto 5 encontrado no valor de None   '''

from itertools import zip_longest

produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']

precos = ['R$500,00', 'R$1500,00', 'R$2700,00', 'R$5000,00']

for produto,preco in zip_longest(produtos,precos):
    print(f'Produto: Produto {produto} encontrado no valor de R$ {preco}')