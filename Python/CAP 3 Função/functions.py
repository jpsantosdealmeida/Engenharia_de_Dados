def a(valor):             # Obrigatório
    print(valor)

def b(valor=15):          # Valor padrão
    print(valor)

def c(*args):             # Posicionais variáveis
    print(args)

def d(**kwargs):          # Nomeados variáveis
    print(kwargs)

def gerar_nome_completo(nome,sobrenome):
    print(f'Boas-Vindo {nome} {sobrenome}')

gerar_nome_completo('Joao Paulo','Santos')

def calcular_valores(preco,quantidade=1):
    preco = preco * quantidade
    print(f'O preço é {preco}')

calcular_valores(10)

# Parametros x Argumentos

"""
Parametros  o que passamos na definição da função
ou seja na criação def ... 

Já quando chamamosa função passamos argumentos

Processar x Retornar

# Funções que processam 
print('Olá') só processa

# Funções que retornam
input('Qual o seu nome?: ')

ela retorna e devemos guardar o resultado em uma var 

qual utilizar?

Vai precisar utilizar o resultado para algo depois? return
se não pode fazer o que tem que ser feito na func
"""

# a função abaixo o primeiro arg é posicional e o que vem depois é nomeados
def gerar_objeto_personalizado(cor,*,altura,formato ):
    print(f'O objeto foi gerado com sucesso!')
    print(f'Cor: {cor} | Altura: {altura} | Formato: {formato}')

gerar_objeto_personalizado('Azul',altura=1.2,formato='Circular')