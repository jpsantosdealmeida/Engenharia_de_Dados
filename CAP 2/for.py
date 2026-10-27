# for x in range (10) vai imprimeir de 0 a 9 pois não inclui o 10
# in range (inicio,fim,passos)

for valor in range(18,111):
    print(f'Estamos em {valor}, onde {valor} é um valor iniciado em 18 e finalizando em 110')

for passo in range (1,11):
    print(f'Realizando passo {passo}')

celulares = ['Asus', 'Samsung', 'Sony', 'IPhone']

versoes = ['Plus', 'Premium Plus', 'Premium Deluxe', 'Plus Premium Ultra']

for cel in celulares:
    for vers in versoes:
        print(f'celular: {cel} | versao: {vers}')