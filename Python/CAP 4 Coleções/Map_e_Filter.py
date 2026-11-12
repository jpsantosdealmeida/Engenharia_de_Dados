'''

Usando a lista abaixo, filtre apenas as vagas com salário acima de R$2500

'''

vagas = [

    ['vaga 1', 1200],

    ['vaga 2', 2550],

    ['vaga 3', 5000]

]

def filtragem(colecao):
    if colecao[1] > 2500:
        return True
    else:
        return False
# Map retorna todos itens , mas retorna o Treu para quem passar na validação            
print(list(map(filtragem,vagas)))

# Filter só retorna os que passaram na validação
print(list(filter(filtragem,vagas)))