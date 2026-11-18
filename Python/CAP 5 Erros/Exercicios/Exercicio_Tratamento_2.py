import json
from pathlib import Path

caminho_pasta = Path(__file__).parent

# Criando pasta dados
dir_dados = caminho_pasta / 'dados'
Path.mkdir(dir_dados,exist_ok=True)

# Criando json produtos
caminho_json_produtos = dir_dados / 'produtos.json'
caminho_json_produtos.touch(exist_ok=True)

# Criando json produtos corrompidos
caminho_json_produtos_corrompido = dir_dados / 'produtos_corrompidos.json'
caminho_json_produtos_corrompido.touch(exist_ok=True)

# Caminho json inexistente
caminho_json_produtos_corrompido2 = dir_dados / 'produtos_corrompidos2.json'


# função

def carregar_json(caminho):
    try:
        with open(file=caminho,mode='r',encoding='utf-8') as file:
            leitura_json = json.load(file)    
    except json.decoder.JSONDecodeError as e:
        return None
    except FileNotFoundError as e:
        return None
    else:
        print("Arquivo carregado com sucesso")
    finally:
        print("Tentativa finalizada")
    return leitura_json

produtos = carregar_json(caminho_json_produtos)
produtos_corrompidos = carregar_json(caminho_json_produtos_corrompido)
produtos_corrompidos = carregar_json(caminho_json_produtos_corrompido2)



