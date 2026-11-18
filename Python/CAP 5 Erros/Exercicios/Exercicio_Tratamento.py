# Conversão segura de valores

valores = [
    "150",
    "250.50",
    "abc",
    "",
    None,
    300,
    "75.25",
    "1O0"
]

def converter_valores(valores):
    # exc = ExceptionGroup("Ocorreram vários erros",[ValueError("Valor inválido"), TypeError("Tipo errado")])
    dicio_valores = {'validos':[],
                     'invalidos':[]}
    for valor in valores:
        try:
            conversao = float(valor)
            dicio_valores['validos'].append(conversao)
        except (ValueError,TypeError) as erro:
            dicio_valores['invalidos'].append(valor)
            dicio_valores['valor'] = valor
            dicio_valores['tipo_erro'] = type(erro).__name__
            dicio_valores['mensagem'] = str(erro)
        
    return dicio_valores
    
resultado = converter_valores(valores)
print(30 * '=-')
print(f"Válidos:{resultado['validos']}")
print(f"Inválidos:{resultado['invalidos']}")


