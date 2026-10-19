# Do Problema ao Código

**Algoritmos, Pensamento Computacional e Programação**

Autor: Denny Paulista Azevedo Filho.

Este repositório reúne os códigos, os exercícios, os dados, os testes e os materiais complementares do livro. O manuscrito oficial permanece no Google Drive.

O percurso de estudo segue esta sequência:

**Problema → compreensão → decomposição → algoritmo → implementação → teste → avaliação → melhoria.**

Python é a linguagem-base. O foco está nos fundamentos da programação, não na memorização da sintaxe.

## 1. Apresentação da obra

A obra introduz a programação a partir de problemas. Cada conceito aparece quando a solução precisa dele: representar uma informação, decidir um caminho, repetir uma operação, organizar muitos dados, dividir uma solução, guardar resultados, tratar falhas e verificar se a resposta está correta.

O livro tem 22 capítulos, organizados em nove partes. Os três primeiros capítulos trabalham o problema e o algoritmo antes do código. Os capítulos seguintes constroem, verificam e melhoram programas em Python. O Capítulo 21 reserva o projeto integrador. O Capítulo 22 trata da continuidade dos estudos.

## 2. Finalidade do repositório

Aqui ficam os materiais executáveis e de apoio que acompanham a leitura:

- programas completos dos capítulos;
- exercícios destinados a quem estuda;
- resoluções de referência, quando forem autorizadas;
- dados usados pelos exemplos;
- testes automatizados;
- diagramas e outros recursos visuais.

Nesta etapa o repositório está organizado e pronto para receber esses materiais. Os exemplos e os exercícios ainda não foram escritos.

Quem lê o livro não precisa conhecer Git, Ruff nem outras ferramentas profissionais para executar os programas. Basta o Python e a biblioteca padrão.

## 3. Organização dos capítulos

Os capítulos ficam em `capitulos/`. Cada pasta contém um `LEIA-ME.md` com o título oficial, a parte da obra, o objetivo geral e o estado do material.

| Capítulo | Título | Parte |
| --- | --- | --- |
| 1 | Um programa começa com um problema | I — Antes do Código |
| 2 | Transformando problemas em soluções | I — Antes do Código |
| 3 | Pensar para o computador — e não como um computador | I — Antes do Código |
| 4 | Quando o problema exige cálculo | II — Construindo Soluções |
| 5 | Quando a solução precisa decidir | II — Construindo Soluções |
| 6 | Quando fazer uma vez não basta | II — Construindo Soluções |
| 7 | Quando há muitos dados | III — Trabalhando com Muitos Dados |
| 8 | Encontrando o que importa | III — Trabalhando com Muitos Dados |
| 9 | Colocando informação em ordem | III — Trabalhando com Muitos Dados |
| 10 | Quando uma solução precisa ser dividida | IV — Dividindo Problemas Complexos |
| 11 | Dando forma aos dados | IV — Dividindo Problemas Complexos |
| 12 | Quando os dados precisam permanecer | V — Lidando com o Mundo Real |
| 13 | Quando as coisas não acontecem como esperado | V — Lidando com o Mundo Real |
| 14 | Quando programas precisam conversar | V — Lidando com o Mundo Real |
| 15 | Funciona mesmo? | VI — Verificando a Solução |
| 16 | Quando o programa não faz o que deveria | VI — Verificando a Solução |
| 17 | Uma solução correta pode ser uma solução ruim | VII — Construindo Soluções Melhores |
| 18 | Melhorando uma solução existente | VII — Construindo Soluções Melhores |
| 19 | Código não é trabalho individual | VIII — Programando no Mundo Atual |
| 20 | Programação assistida por Inteligência Artificial | VIII — Programando no Mundo Atual |
| 21 | Projetando e construindo uma solução completa | IX — Do Problema ao Sistema |
| 22 | Do código ao próximo problema | IX — Do Problema ao Sistema |

Dentro de um capítulo, as pastas abaixo passam a existir somente quando houver conteúdo para elas:

- `exemplos/` — programas completos;
- `exercicios/` — atividades de quem estuda;
- `solucoes/` — resoluções de referência;
- `testes/` — testes daquele capítulo;
- `dados/` — dados usados apenas naquele capítulo;
- `diagramas/` — fluxogramas e outros recursos visuais.

Outras pastas da raiz:

- `dados/` — dados compartilhados por mais de um capítulo, quando existirem;
- `documentacao/` — orientações para o autor e para colaboradores;
- `recursos/` — materiais de apoio que não pertencem a um único capítulo;
- `testes/` — testes gerais do repositório, quando existirem;
- `ferramentas/` — utilitários do desenvolvimento do autor.

O Capítulo 21 permanece reservado. A estrutura interna do projeto integrador será definida quando a solução estiver aprovada.

## 4. Requisitos mínimos

- Python 3.13.
- Um editor de texto ou um ambiente de programação capaz de editar arquivos `.py`.
- Um terminal para executar os programas.

Não é necessário instalar bibliotecas para acompanhar os exemplos básicos. Eles devem usar a biblioteca padrão do Python.

Git, Ruff, ambientes virtuais e integração contínua são recursos do autor. Quem estuda pode ignorá-los.

## 5. Instalação do Python

A versão de referência deste repositório é a **Python 3.13**.

1. Obtenha o Python 3.13 em [python.org/downloads](https://www.python.org/downloads/).
2. Durante a instalação, inclua o Python no `PATH` do sistema, quando o instalador oferecer essa opção.
3. Abra um terminal e confira a versão:

```bash
python3 --version
```

Em alguns sistemas Windows o comando disponível é `python` ou o lançador `py`:

```bash
py -3.13 --version
```

A instalação do Python usada para ler o livro pode ser a instalação normal do sistema ou a distribuição oficial. Este repositório não altera o Python global da máquina de quem desenvolve os materiais.

## 6. Execução direta de programas

Cada exemplo será um programa independente. Quando os arquivos existirem, a execução será feita a partir da pasta do repositório:

```bash
python3 capitulos/capitulo-04/exemplos/nome_do_programa.py
```

Substitua o caminho pelo arquivo indicado no capítulo. Se o comando `python3` não existir, use o comando que a instalação local disponibilizou, como `python` ou `py -3.13`.

Os programas leem e escrevem no terminal, ou usam arquivos colocados junto do próprio capítulo. Não há um aplicativo único para instalar nem um comando de inicialização do livro.

## 7. Utilização dos materiais complementares

Além dos programas, um capítulo pode trazer:

- descrições de problemas e algoritmos em linguagem natural;
- pseudocódigo e fluxogramas;
- conjuntos de dados em texto, CSV ou JSON;
- respostas locais usadas para simular uma comunicação entre programas;
- versões sucessivas de uma mesma solução, quando o capítulo compara ou melhora um programa.

Leia o `LEIA-ME.md` do capítulo antes de abrir os arquivos. Ele indica o que aquele material complementa e o que ainda está em preparação.

Dados usados por um único capítulo ficam na pasta `dados/` desse capítulo. Dados reutilizados ficam na pasta `dados/` da raiz, e somente quando essa reutilização existir.

## 8. Orientações básicas para exercícios

- Leia o problema até identificar entradas, regras e resultado esperado.
- Tente construir o algoritmo antes de procurar uma resolução pronta.
- Escreva e execute a sua solução. Compare o resultado com os casos pedidos no exercício.
- Quando existir uma pasta `solucoes/`, use-a depois da sua tentativa, como referência.
- Uma resolução de referência mostra um caminho correto. Outras soluções também podem estar corretas.
- Guarde a sua versão. Nos capítulos finais, comparar versões faz parte do aprendizado.

Não é preciso enviar os exercícios para um serviço externo nem instalar ferramentas além do Python.

## 9. Testes (opcional)

O ensino de testes automatizados pertence ao Capítulo 15. Antes disso, o autor pode guardar testes internos para proteger os exemplos, mas quem estuda não precisa executá-los para acompanhar o livro.

Quando houver testes, o autor os executa com:

```bash
python3 ferramentas/executar_testes.py
```

Se ainda não existir nenhum teste, o comando informa `Nenhum teste foi encontrado.` e termina sem declarar aprovação.

Os testes usam `unittest`, da biblioteca padrão. Eles devem ser determinísticos e independentes de serviços externos.

## 10. Licenciamento

O licenciamento da obra e deste repositório ainda não está definido. A presença dos arquivos aqui não autoriza cópia, adaptação ou redistribuição. A definição da licença será registrada pelo autor antes de qualquer publicação do material.

Colaboradores do manuscrito encontram o processo de trabalho em `documentacao/`.
