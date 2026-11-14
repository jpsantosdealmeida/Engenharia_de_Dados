from pathlib import Path
import json

# Aqui estou até o arquivo a.py
dir_atual = Path(__file__)


# Agora vou pegar o partente do a.py que seria a pasta python que está no desktop
dir_parente = dir_atual.parent

print(f'diretório atual: {dir_atual}')
print(30 * '=-')
print(f'diretório Parente (Anterior): {dir_parente}')

# Criando umas pasta chamada fotos na pasta python

# Com o caminho raiz da pasta eu fiz uma nova pasta
dir_fotos = dir_parente / 'Fotos'

# Criando a pasta ( make dir ) ( Cria pasta não arquivos)
dir_fotos.mkdir(exist_ok=True)

# Para remover é rmdir
dir_fotos.rmdir()

# Criando arquivos ( Exemplo um json )
arquivo_json_user_1 = dir_parente / 'user1.json'

# Criando de fato o arquivo
arquivo_json_user_1.touch()

# # Removendo o arquivo
# arquivo_json_user_1.unlink()

# # Escrevendo no arquivo craidno
arquivo_json_user_1.write_text('{"usuario":"Joao Paulo","idade":25,"Profissao":"Engenheiro de Dados"}')

# Lendo o que está dentro do arquivo
print(f'Leitura pelo pathlib: {arquivo_json_user_1.read_text()}')

with open(arquivo_json_user_1,'r') as file:
    convertendo_json_em_string = json.load(file)

    for chave,valor in convertendo_json_em_string.items():
        print(f'Chave: {chave} -> {valor}')

    