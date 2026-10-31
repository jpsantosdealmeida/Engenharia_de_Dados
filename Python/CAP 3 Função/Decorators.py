def decorador(funcao):
    print('Preparando decorator')

    def wrapper():
        print('Início')
        funcao()
        print('Fim')

    return wrapper()

'''
@ decorador é a mesma coisa de fazer
def executar():
    print('Executando tarefa')

Estou passando executar como arg em decorador 
'''
@decorador
def executar():
    print('Executando tarefa')


print('Programa iniciado')
executar()