

# Monte o seguinte cenário usando condicionais

# Você está montando um sistema para um salão de beleza para calcular o preço do corte de cabelos grandes que irá seguir as seguinte regras

# Disclaimer the haircut values are completely ficticious, I have no ideia of actual prices

'''

Se seu cabelo estiver com ou abaixo de 20cm você paga o valor de R$50,00

Se seu cabelo estiver entre 21cm a 30cm você paga o valor de R$70,00

Se seu cabelo estiver entre 31cm a 50cm você paga o valor de R$100,00

Acima de 50cm Favor consultar na recepção

# Declare uma variável que represente o tamanho atual do cabelo

# Apenas imprima na tela a mensagem apropriada, nada além disso é necesário

'''
tamanho_cabelo = int(input('Insira o tamanho do cabelo (cm): '))

if tamanho_cabelo <= 20:
    print(f'Valor do corte R$ 50,00')
elif tamanho_cabelo >= 21 and tamanho_cabelo <= 30:
    print(f'Valor do corte R$ 70,00')
elif tamanho_cabelo >= 31 and tamanho_cabelo <= 50:
    print(f'Valor do corte R$ 100,00')
else:
    print(f'Favor,consultar na recepção.')
