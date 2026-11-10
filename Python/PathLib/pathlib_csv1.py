
"""
MÓDULO PATHLIB — RESUMO DE ESTUDOS
=================================

O pathlib faz parte da biblioteca padrão do Python e permite
manipular caminhos de arquivos e diretórios de forma orientada
a objetos, independentemente do sistema operacional.

IMPORTAÇÃO:
    from pathlib import Path

CAMINHOS:
    Path.cwd()       -> Retorna o diretório de trabalho atual.
    Path(__file__)   -> Representa o caminho do script atual.
    Path("dados")    -> Cria um objeto Path.
    caminho / "csv"  -> Constrói caminhos usando o operador /.

PROPRIEDADES:
    caminho.name     -> Nome do arquivo com extensão.
    caminho.stem     -> Nome sem a última extensão.
    caminho.suffix   -> Última extensão do arquivo.
    caminho.parent   -> Diretório pai.

MÉTODOS:
    caminho.exists()      -> Verifica se o caminho existe.
    caminho.is_file()     -> Verifica se é um arquivo.
    caminho.is_dir()      -> Verifica se é um diretório.
    caminho.is_absolute() -> Verifica se o caminho é absoluto.
    caminho.resolve()     -> Retorna o caminho absoluto resolvido.
    caminho.read_text()   -> Lê todo o conteúdo como string.
    caminho.open()        -> Abre o arquivo para leitura ou escrita.

CAMINHO RELATIVO X ABSOLUTO:
    Relativo -> Interpretado a partir do diretório de trabalho.
    Absoluto -> Identifica a localização a partir da raiz.

LEITURA DE ARQUIVOS:
    with caminho.open(encoding="utf-8") as arquivo:
        print(arquivo.read())

    O with garante o fechamento do arquivo ao sair do bloco.

OBSERVAÇÕES:
    - pathlib e os.path possuem funcionalidades semelhantes.
    - pathlib é mais expressivo para manipulação de caminhos.
    - read_text() carrega todo o conteúdo na memória.
    - pathlib não interpreta automaticamente a estrutura CSV.

DOCUMENTAÇÃO:
    https://docs.python.org/pt-br/3/library/pathlib.html
"""
from pathlib import Path
p = Path('dados')
print(f'Caminho: {p}')