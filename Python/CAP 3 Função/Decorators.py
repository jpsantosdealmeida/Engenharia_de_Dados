# def func(funcao):
#     print('Preparando decorator')

#     def wrapper():
#         print('Início')
#         funcao()
#         print('Fim')

#     return wrapper()

# '''
# @ decorador é a mesma coisa de fazer
# def executar():
#     print('Executando tarefa')

# Estou passando executar como arg em decorador 
# '''
# @func
# def executar():
#     print('Executando tarefa')


# executar()

from datetime import datetime
from time import sleep

def decorador(funcao):
    data_atual = datetime.now().date().strftime('%d/%m/%Y')

    def embalagem():
        print(f'Horário antes da execucação: {data_atual}')
        sleep(5)
        funcao()
        sleep(5)
        print(f'Horário após a finalização da execucação: {data_atual}')

    return embalagem

@decorador
def saudacao():
    print('Aplicação está em execucação! ')

saudacao()