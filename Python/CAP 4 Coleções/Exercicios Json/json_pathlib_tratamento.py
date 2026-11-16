
from pathlib import Path
import json

# ============================================================
# 1. PATHLIB — CAMINHOS E DIRETÓRIOS
# ============================================================

# Caminho completo do arquivo Python em execução (json_pathlib_tratamento.py)
arquivo_atual = Path(__file__).resolve()

# Diretório onde o arquivo Python está localizado
dir_parente = arquivo_atual.parent

print(f"Arquivo atual: {arquivo_atual}")
print(f"Diretório pai: {dir_parente}")
print(30 * "=-")


# ============================================================
# 2. PATHLIB — CRIANDO E REMOVENDO PASTAS
# ============================================================

# Define o caminho de uma pasta chamada Fotos
dir_fotos = dir_parente / "Fotos"

# Cria a pasta, caso não exista
dir_fotos.mkdir(exist_ok=True)

# Remove a pasta somente se estiver vazia
# dir_fotos.rmdir()


# ============================================================
# 3. PATHLIB — CRIANDO, LENDO E REMOVENDO ARQUIVOS
# ============================================================

arquivo_json_user_1 = dir_parente / "user1.json"

# Cria o arquivo caso não exista
arquivo_json_user_1.touch(exist_ok=True)

# Escreve uma string JSON diretamente no arquivo
arquivo_json_user_1.write_text(
    '{"usuario": "Joao Paulo", "idade": 25, "profissao": "Engenheiro de Dados"}',
    encoding="utf-8"
)

# Lê o conteúdo do arquivo como string
conteudo = arquivo_json_user_1.read_text(encoding="utf-8")

print(f"Conteúdo do arquivo: {conteudo}")
print(f"Tipo: {type(conteudo)}")

# Remove o arquivo (deixe comentado para continuar praticando)
# arquivo_json_user_1.unlink()

print(30 * "=-")


# ============================================================
# 4. JSON.LOADS() — STRING JSON PARA OBJETO PYTHON
# ============================================================

usuario = '''
{
    "nome": "Carola",
    "telefone": "47-99224-8852"
}
'''

# Converte a string JSON em um dicionário Python
data = json.loads(usuario)

print(f"Nome: {data['nome']}")
print(f"Tipo original: {type(usuario)}")
print(f"Tipo convertido: {type(data)}")

print(30 * "=-")


# ============================================================
# 5. JSON.DUMPS() — OBJETO PYTHON PARA STRING JSON
# ============================================================

# Converte o dicionário Python em uma string JSON
usuario_string_json = json.dumps(
    data,
    indent=4,
    ensure_ascii=False
)

print(usuario_string_json)
print(f"Tipo: {type(usuario_string_json)}")

print(30 * "=-")


# ============================================================
# 6. JSON.DUMP() — OBJETO PYTHON PARA ARQUIVO JSON
# ============================================================

arquivo_usuario = dir_parente / "usuario_arquivo.json"

# Grava o dicionário Python em um arquivo JSON
with open(arquivo_usuario, "w", encoding="utf-8") as arquivo:
    json.dump(data, arquivo, indent=4, ensure_ascii=False)

print(f"Arquivo JSON criado: {arquivo_usuario}")

print(30 * "=-")


# ============================================================
# 7. JSON.LOAD() — ARQUIVO JSON PARA OBJETO PYTHON
# ============================================================

# Lê o arquivo JSON e converte seu conteúdo em objeto Python
with open(arquivo_usuario, "r", encoding="utf-8") as arquivo:
    dados_usuario = json.load(arquivo)

print(f"Dados carregados: {dados_usuario}")
print(f"Nome: {dados_usuario['nome']}")
print(f"Tipo: {type(dados_usuario)}")

print(30 * "=-")


# ============================================================
# 8. JSON.LOAD() — LENDO O ARQUIVO USER1.JSON
# ============================================================

with open(arquivo_json_user_1, "r", encoding="utf-8") as arquivo:
    dados_user_1 = json.load(arquivo)

for chave, valor in dados_user_1.items():
    print(f"Chave: {chave} -> Valor: {valor}")
