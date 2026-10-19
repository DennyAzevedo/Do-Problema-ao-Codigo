# Convenções de código

Estas convenções orientam os exemplos do livro e as ferramentas do autor. Elas favorecem programas introdutórios, claros e independentes.

## Idioma

O texto escrito para quem estuda fica em português brasileiro:

- nomes de arquivos didáticos;
- variáveis e funções;
- comentários e docstrings;
- mensagens exibidas pelos programas.

Identificadores e caminhos não usam acentos, espaços nem caracteres especiais. Prefira `preco_final` a um nome acentuado, e `calcular_compra.py` a um nome com espaço.

Os nomes exigidos pelo ecossistema permanecem como estão: `README.md`, `.gitignore`, `.python-version`, `pyproject.toml` e `.github/workflows`.

## Forma dos programas de exemplo

- Um exemplo resolve um problema pequeno e pode ser executado sozinho.
- A biblioteca padrão é suficiente para os exemplos básicos.
- Uma biblioteca externa só entra quando o capítulo tiver uma justificativa pedagógica registrada no `LEIA-ME.md`.
- Não antecipar funções, classes, testes ou arquivos nos capítulos em que esses assuntos ainda não foram estudados.
- O Capítulo 10 pode dividir a solução em funções. A refatoração formal permanece no Capítulo 18.
- O Capítulo 11 pode introduzir um objeto simples para representar um conceito do problema. Não introduzir arquitetura orientada a objetos.
- `print` é adequado quando o programa apresenta um resultado a quem estuda.
- Anotações de tipo são opcionais. Não são exigidas nos exemplos introdutórios.
- Comentários explicam uma decisão do problema. Não repetem o que a linha já mostra.

## Nomes

- Funções e variáveis em `snake_case`: `calcular_total`, `quantidade`.
- Constantes com nome estável em maiúsculas: `ALIQUOTA`.
- Classes, quando o capítulo as usar, em `PascalCase`: `Produto`.
- Arquivos de exemplo e de exercício em `snake_case`, sem acento.
- Arquivos de teste começam com `teste_`.

Escolha nomes do domínio do problema. Um exemplo sobre compra usa `preco` e `desconto`, não `x` e `y`, salvo quando o capítulo estiver justamente discutindo um nome ruim.

## Testes e versões

- Testes ficam em `testes/` do capítulo, ou em `testes/` na raiz quando não pertencerem a um capítulo.
- Um teste verifica resultado, caso limite ou regressão. Não depende de rede nem de relógio.
- Quando um capítulo comparar ou refatorar uma solução, as versões anteriores permanecem em arquivos distintos, com nomes que indiquem a ordem, como `solucao_v1.py` e `solucao_v2.py`.

## Ferramentas do autor

O Ruff verifica o código durante o desenvolvimento. A configuração está em `pyproject.toml` e usa apenas regras compatíveis com exemplos introdutórios. Quem estuda o livro não precisa executá-lo.

A formatação automática é opcional. O critério obrigatório do autor é `ruff check`, descrito no guia de desenvolvimento.

## Editores

VS Code, Cursor, PyCharm ou outro editor compatível com Python servem para trabalhar neste repositório. Não há configuração obrigatória de editor. Se uma configuração de workspace for adicionada no futuro, ela deve permanecer opcional e registrada neste documento.
