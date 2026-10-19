"""Descobre e executa os testes automatizados deste repositório.

O utilitário percorre os diretórios de teste dos capítulos e o diretório
geral de testes. Quando não existe nenhum teste, a execução termina com
sucesso e informa a ausência. Testes inexistentes não são declarados
como aprovados.
"""

import importlib.util
import sys
import unittest
from pathlib import Path


RAIZ = Path(__file__).resolve().parent.parent
PADRAO_ARQUIVO = "teste_*.py"


def diretorios_de_testes() -> list[Path]:
    """Localiza os diretórios em que os testes podem ser colocados."""
    diretorios: list[Path] = []
    capitulos = RAIZ / "capitulos"
    if capitulos.is_dir():
        encontrados = capitulos.glob("capitulo-*/testes")
        diretorios.extend(sorted(caminho for caminho in encontrados if caminho.is_dir()))

    testes_gerais = RAIZ / "testes"
    if testes_gerais.is_dir():
        diretorios.append(testes_gerais)

    return diretorios


def arquivos_de_teste() -> list[Path]:
    """Reúne os arquivos de teste já escritos, em ordem estável."""
    arquivos: list[Path] = []
    for diretorio in diretorios_de_testes():
        arquivos.extend(sorted(diretorio.glob(PADRAO_ARQUIVO)))
    return arquivos


def nome_do_modulo(caminho: Path) -> str:
    """Cria um nome de módulo único a partir do caminho do arquivo."""
    relativo = caminho.relative_to(RAIZ).with_suffix("")
    return "teste_descoberto_" + "_".join(relativo.parts)


def carregar_modulo(caminho: Path):
    """Carrega um arquivo de teste sem transformá-lo em pacote instalável."""
    nome = nome_do_modulo(caminho)
    especificacao = importlib.util.spec_from_file_location(nome, caminho)
    if especificacao is None or especificacao.loader is None:
        mensagem = f"Não foi possível carregar o teste: {caminho}"
        raise ImportError(mensagem)

    modulo = importlib.util.module_from_spec(especificacao)
    sys.modules[nome] = modulo
    especificacao.loader.exec_module(modulo)
    return modulo


def montar_suite(arquivos: list[Path]) -> unittest.TestSuite:
    """Monta uma suíte com os casos definidos nos arquivos informados."""
    carregador = unittest.TestLoader()
    suite = unittest.TestSuite()
    for caminho in arquivos:
        modulo = carregar_modulo(caminho)
        suite.addTests(carregador.loadTestsFromModule(modulo))
    return suite


def informar_ausencia() -> int:
    """Informa que não há testes, sem tratá-los como aprovados."""
    print("Nenhum teste foi encontrado.")
    return 0


def main() -> int:
    """Executa os testes existentes ou informa que nenhum foi encontrado."""
    arquivos = arquivos_de_teste()
    if not arquivos:
        return informar_ausencia()

    try:
        suite = montar_suite(arquivos)
    except Exception as erro:
        # Uma falha ao importar o arquivo impede tratar a suíte como aprovada.
        print(f"Falha ao carregar testes: {erro}")
        return 1

    if suite.countTestCases() == 0:
        print("Arquivos de teste foram encontrados, mas nenhum caso foi identificado.")
        print("Esses arquivos não foram declarados como aprovados.")
        return 1

    executor = unittest.TextTestRunner(verbosity=2)
    resultado = executor.run(suite)
    if resultado.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
