def calcular_frete(peso,distancia):
    valor_frete = (peso * 2.5) + (distancia * 0.75)
    return valor_frete

frete1 = calcular_frete(10,100)
frete2 = calcular_frete(25,200)
frete3 = calcular_frete(50,150)

# Funcionando

def classificar_pedido(status):
    status = status.strip().lower()

    if status == 'entregue':
        return 'Finalizado'
    elif status == 'pendente':
        return 'Em andamento'
    elif status == 'cancelado':
        return 'Cancelado'
    else:
        return 'Status inválido'
    

classificacao = classificar_pedido('    cancelado   ')

# Funcionando

def validar_valor(valor):
    
    try:
        valor = float(valor)
        if type(valor) == float and valor > 0 :
            return True
        else:
            return False
    except:
        return False

valores = ["350.00", "0", "-150.00", "abc", "890.50"]        
resultado = validar_valor("-150.00")


# funcionando

def registrar_entrega(pedido,cidade,status='pendente'): 
    return f'O pedido {pedido} passou pela cidade {cidade} e seu status é {status}'

re1 = registrar_entrega(pedido='PED-001',cidade='Campinas')
re2 = registrar_entrega(pedido="PED-001",cidade='Campinas',status='Pendente')
re3 = registrar_entrega('PED-001','Jacareí','entregue')
print(re1)
print(re2)
print(re3)
def somar_fretes(*valor_frete):
    vl_frete = sum(valor_frete)
    return vl_frete

sf1 = somar_fretes(100, 200, 50)
sf2 = somar_fretes(75, 125)
sf3 = somar_fretes()
print(sf1)
print(sf2)
print(sf3)

pedidos = [
    "PED-001;ENTREGUE;350.00",
    "PED-002;PENDENTE;780.50",
    "PED-003;ENTREGUE;120.00",
    "PED-004;CANCELADO;500.00",
    "PED-005;ENTREGUE;abc",
    "PED-006;ENTREGUE;-100.00"
]