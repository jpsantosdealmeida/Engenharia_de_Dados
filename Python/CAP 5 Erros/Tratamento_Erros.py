# Exceções
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     # except IndexError: Não funciona essa exceção pois o erro no caso não é esse
#     except ValueError as erro: # Podemos dar um nome para o erro a fim de colocar no logging
#         print("Oops!  That was no valid number.  Try again...")
#     else:
#         print('Obrigado!')
#     # Sempre executa independente se cair na exceção ou não
    
def dividir(numerador,denominador):
    try:
        resultado = numerador / denominador 
    except ZeroDivisionError as ErroDivisaoPorZero:
        print(f'Erro de divisão por zero.')
    except TypeError:
        print(f'Erro, de tipo')
    else:
        print(f'O resultado da divisão é {resultado}')
    finally:
        print(f'Bloco finalmente sendo executado!')

        '''
        Bloco	Quando executa
        try	Tenta executar o código
        except	Quando ocorre uma exceção correspondente
        else	Quando o try termina sem exceção
        finally	Ao sair da estrutura, mesmo que ocorra uma exceção
        '''

dividir(2,1)
# Executa sem problemas 
dividir(2,0)
# Cai no erro de divisão por zero
dividir('2','1')
# Cai no Erro de tipagem

