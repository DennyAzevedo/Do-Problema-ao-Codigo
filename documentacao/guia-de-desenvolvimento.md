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

Sintaxe de todos os arquivos Python acompanhados:

```bash
python -m compileall -q capitulos ferramentas testes
```

Testes existentes:

```bash
python ferramentas/executar_testes.py
```

Qualidade com Ruff, na versão fixada em `ferramentas/requirements-desenvolvimento.txt`:

```bash
python -m ruff check .
```

A formatação do Ruff é opcional:

```bash
python -m ruff format .
```

O Ruff está configurado em `pyproject.toml` com as famílias E, F e W. Tipagem obrigatória, docstrings obrigatórias e reescritas automáticas para construções avançadas ficam desligadas. Linhas longas de texto didático não reprovam a verificação.

Quem estuda não precisa instalar nem executar o Ruff.

## Integração contínua

O arquivo `.github/workflows/validacao.yml` roda em push e pull request. Ele verifica a sintaxe, executa os testes encontrados e roda o Ruff. Não usa segredos, não publica pacote e não cria release.

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
