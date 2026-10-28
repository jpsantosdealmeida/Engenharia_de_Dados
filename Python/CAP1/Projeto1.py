from datetime import datetime
import random


## Objetivo de projeto

# * Estamos criando um módulo de login do nosso aplicativo, e você deve obter as seguintes informações do funcionário.

## Módulo 1 - Gerar registro do funcionário

### Funcionalidades do módulo 1
'''

1. Obtenha o nome do usuário

2. Obtenha a idade do usuário

3. Registre de forma automática a data do cadastro do usuário, usando a data do registro como data de registro

4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:
'''

'''
5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)
'''
nome = input('Insira seu nome: ')
idade = int(input('Insira sua idade: '))
aniversario = input('Insira sua data de aniversário no formato (dd/mm/aaaa): ')
data_cadastro = datetime.now()
cartoes = ['R$50,00','R$250,00','R$120,00']
sorteio = random.choice(cartoes)
(data_cadastro,'%d/%m/%Y')
print(f'Olá {nome}, seu registro foi concluído com sucesso no dia {datetime.strftime(data_cadastro,'%d/%m/%Y')}')
print(f'Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {sorteio}')

## Módulo 2 - Gerar apresentação do usuário

### Funcionalidades do módulo 2 - Mensagem de boas vindas!
'''
Usando os dados obtidos no módulo 1, exiba as seguintes informações:

1. Olá (nome do usuário), seu registro foi concluído com sucesso no dia(data de cadastro no formato dd/mm/aaaa).

Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de (valor sorteado).
'''