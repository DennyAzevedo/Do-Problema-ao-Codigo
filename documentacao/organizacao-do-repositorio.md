# Organização do repositório

Documento de trabalho do autor e de colaboradores. O manuscrito oficial permanece no Google Drive. Este arquivo descreve apenas o repositório técnico.

## Fonte dos títulos

O arquivo editorial `sumario_aprovado.md` não estava neste repositório nem nas pastas locais consultadas. Os títulos, as partes e os objetivos gerais dos `LEIA-ME.md` foram extraídos do sumário preliminar detalhado de `PropostaLivro_DoProblemaAoCodigo.docx`.

Esse sumário descreve 22 capítulos em nove partes e coincide com a progressão pedagógica desta preparação. Se a versão aprovada divergir, os `LEIA-ME.md` devem ser atualizados antes do desenvolvimento dos materiais. O sumário em si não é copiado para este repositório.

## Mapa

```text
capitulos/capitulo-01/ … capitulos/capitulo-22/
dados/
documentacao/
recursos/
testes/
ferramentas/
.github/workflows/
```

Cada capítulo começa com um `LEIA-ME.md`. As pastas internas surgem quando o material existir:

| Pasta | Uso |
| --- | --- |
| `exemplos/` | Programas completos do capítulo |
| `exercicios/` | Atividades de quem estuda |
| `solucoes/` | Resoluções de referência autorizadas |
| `testes/` | Testes daquele capítulo |
| `dados/` | Dados exclusivos do capítulo |
| `diagramas/` | Fluxogramas e figuras ligadas ao algoritmo |

Não criar essas pastas vazias em todos os capítulos.

## Onde colocar cada tipo de material

- Um programa usado em um único capítulo fica em `capitulos/capitulo-NN/exemplos/`.
- Um dado usado em um único capítulo fica em `capitulos/capitulo-NN/dados/`.
- Um dado compartilhado de fato fica em `dados/`, na raiz. Enquanto não houver compartilhamento, a pasta raiz permanece só com a orientação.
- Um diagrama fica em `diagramas/` do capítulo correspondente.
- Um teste fica junto do capítulo que protege. `testes/`, na raiz, recebe apenas verificações do repositório que não pertençam a um capítulo.
- `recursos/` guarda apoio transversal, como uma figura reutilizada ou uma nota de consulta. Não antecipar esse conteúdo.
- `ferramentas/` guarda utilitários do autor. O código dos capítulos não importa essa pasta.

Não criar um pacote Python do livro, nem um módulo compartilhado entre capítulos, enquanto um exemplo puder permanecer independente.

## Progressão e restrições de estrutura

| Capítulos | O que a pasta deve comportar | O que fica para depois |
| --- | --- | --- |
| 1–3 | Problemas, algoritmos em linguagem natural, pseudocódigo, fluxogramas e análises | Programas Python |
| 4–6 | Programas pequenos e independentes | Bibliotecas e módulos comuns |
| 7–9 | Coleções, buscas, ordenação e arquivos de dados da biblioteca padrão | Biblioteca externa sem justificativa pedagógica |
| 10 | Funções e modularização | Refatoração formal, reservada ao Capítulo 18 |
| 11 | Representação dos dados e introdução a objetos | Arquitetura orientada a objetos |
| 12–14 | Arquivos, CSV, JSON, validação, exceções e HTTP | Serviço externo obrigatório no Capítulo 14 |
| 15–16 | Testes, depuração e análise de defeitos | Ensinar testes antes do Capítulo 15 |
| 17–18 | Versões comparáveis da mesma solução | Apagar a versão anterior no Capítulo 18 |
| 19–20 | Git, versionamento e programação assistida por IA | Conta ou ferramenta externa para os exemplos básicos |
| 21 | Diretório reservado ao projeto integrador | Arquitetura, entidades, funcionalidades e dependências |
| 22 | Complementos e referências | Programas executáveis obrigatórios |

O Capítulo 14 deve poder ser verificado com respostas locais ou simuladas, guardadas no próprio capítulo.

No Capítulo 18, cada versão permanece no repositório para que a refatoração seja demonstrada com o comportamento preservado.

## O que este repositório não guarda

- o manuscrito integral;
- uma segunda cópia editorial do sumário;
- segredos, credenciais e configurações privadas de editor.

A preparação do ambiente do autor está em `guia-de-desenvolvimento.md`.
