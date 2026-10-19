# Guia de desenvolvimento

Orientação para o autor e para colaboradores. Quem estuda pelo livro segue o `README.md` e executa os programas diretamente com o Python.

## Versão de referência

A referência provisória é Python 3.13, com o patch registrado em `.python-version`. A integração contínua usa essa mesma versão.

Confira o interpretador local:

```bash
python3 --version
```

O Python global do sistema não deve ser substituído por este repositório. O ambiente do autor fica isolado em `.venv/`.

## Ambiente virtual

Na raiz do repositório, com o Python 3.13 disponível:

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r ferramentas/requirements-desenvolvimento.txt
```

No Windows, a ativação é `.venv\Scripts\activate`.

A pasta `.venv/` não entra no versionamento. Ela contém apenas ferramentas do autor. Os exemplos do livro não dependem dela.

## Verificações do autor

Execute os três comandos na raiz do repositório, com o ambiente virtual ativado.

Sintaxe, com `compileall` da biblioteca padrão:

```bash
python -m compileall -q capitulos ferramentas testes
```

Testes existentes, com `unittest` por meio do executor central:

```bash
python ferramentas/executar_testes.py
```

O executor procura `teste_*.py` em `capitulos/capitulo-NN/testes/` e em `testes/`. Sem arquivos de teste, a saída é `Nenhum teste foi encontrado.` e o comando termina sem declarar aprovação.

Qualidade com o Ruff, na versão fixada em `ferramentas/requirements-desenvolvimento.txt`:

```bash
python -m ruff check .
```

O `pyproject.toml` usa Python 3.13 como referência e seleciona somente as regras `E4`, `E7`, `E9` e `F`: erros de importação, de comando, de execução e falhas como nome indefinido ou importação sem uso. Comprimento de linha, tipagem, docstrings e avisos de estilo ficam de fora.

A formatação também está configurada, para uso do autor, e atua somente sobre arquivos Python:

```bash
python -m ruff format --check .
python -m ruff format .
```

O primeiro comando apenas informa divergências. O segundo reescreve os arquivos. A formatação não entra na integração contínua. Um exemplo do livro permanece como foi escrito para a leitura quando a forma automática prejudicar a compreensão.

Quem estuda executa os programas com o Python da própria máquina. Ruff, GitHub Actions e o ambiente virtual não fazem parte dessa execução.

## Integração contínua

O arquivo `.github/workflows/validacao.yml` roda em push e pull request. Ele executa `compileall`, `ferramentas/executar_testes.py` e `ruff check`. Não usa segredos, não publica pacote e não cria release.

Enquanto não houver testes, a etapa correspondente informa que nenhum teste foi encontrado.

## Editor

Use VS Code, Cursor, PyCharm ou outro editor com suporte a Python. Aponte o interpretador do projeto para `.venv/bin/python` se quiser as verificações do autor dentro do editor.

Não há pasta de configuração obrigatória. Uma configuração de workspace, se for útil no futuro, deve ser opcional e descrita em `convencoes-de-codigo.md`.

## Ao começar um capítulo

1. Leia o `LEIA-ME.md` do capítulo e o sumário aprovado.
2. Crie somente as pastas internas necessárias ao material da vez.
3. Mantenha cada exemplo executável com a biblioteca padrão, salvo justificativa pedagógica.
4. Acrescente testes do autor quando o exemplo passar a ter comportamento que precise permanecer estável.
5. Atualize o estado no `LEIA-ME.md` quando o material deixar de estar aguardando desenvolvimento.

O Capítulo 21 continua sem estrutura interna até a solução do projeto integrador ser aprovada.

## O que não faz parte deste ambiente

O desenvolvimento local usa o interpretador Python, o módulo `venv` da biblioteca padrão e o GitHub Actions para a validação remota. Não há imagem de contêiner, orquestração local nem pacote instalável do livro.
