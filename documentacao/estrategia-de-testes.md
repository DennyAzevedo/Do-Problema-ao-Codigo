# Estratégia de testes

Os testes protegem os exemplos do autor e, a partir do Capítulo 15, também ensinam verificação. Quem estuda não precisa executar esta suíte para acompanhar os capítulos anteriores.

## Ferramenta

Os testes usam `unittest`, da biblioteca padrão. Não há dependência externa de teste.

O executor do repositório é:

```bash
python3 ferramentas/executar_testes.py
```

Ele procura arquivos `teste_*.py` nestes lugares:

- `capitulos/capitulo-NN/testes/`
- `testes/`, na raiz

Dentro de cada arquivo, os métodos de teste começam com `teste_`. Esse prefixo é reconhecido pelo `unittest`.

A descoberta não trata pasta vazia como teste aprovado. Sem arquivos de teste, a saída é:

```text
Nenhum teste foi encontrado.
```

O comando termina com código 0. Essa saída não significa que uma suíte foi aprovada. Significa que ainda não há testes.

Se existir arquivo `teste_*.py` sem nenhum caso de `unittest`, o comando termina com código 1 e informa que os arquivos não foram aprovados.

Falhas de carregamento, asserções e erros também terminam com código diferente de zero.

## O que cada teste verifica

- **Resultado.** Para uma entrada conhecida, a saída ou o valor retornado é o esperado.
- **Caso limite.** Coleção vazia, zero, fronteira de uma regra, último elemento e condição de parada entram na suíte quando o capítulo já trabalha esses casos.
- **Regressão.** Depois de uma correção ou de uma refatoração, os casos anteriores continuam valendo.
- **Determinismo.** O teste produz o mesmo resultado em qualquer máquina, sem rede, sem data atual e sem serviço externo.

Não criar testes artificiais apenas para popular uma pasta. Um teste nasce junto do exemplo ou do defeito que precisa proteger.

## Testes do autor e ensino de testes

O autor pode escrever testes desde os primeiros exemplos com código. Esses testes são ferramenta de desenvolvimento.

O livro ensina testes no Capítulo 15. Até lá, o material didático não apresenta `unittest` como conteúdo da lição.

O Capítulo 16 usa testes para confirmar que um defeito foi corrigido. O Capítulo 18 executa os mesmos testes antes e depois da refatoração, com as versões anteriores preservadas.

## Onde o teste importa um exemplo

Não há módulo compartilhado do repositório. Quando um teste precisar alcançar um exemplo do próprio capítulo, o arquivo de teste inclui a pasta daquele exemplo no caminho de importação antes de importá-lo:

```python
import sys
from pathlib import Path

CAPITULO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CAPITULO / "exemplos"))
```

O restante do arquivo define casos reais de `unittest` para o exemplo daquele capítulo.

## Comunicação e dados

No Capítulo 14, a verificação automática usa respostas locais ou simuladas, guardadas no capítulo. Um teste não consulta um serviço real.

Dados lidos pelos testes ficam no capítulo, ou em `dados/` quando forem compartilhados. O teste referencia o arquivo por caminho relativo à sua localização, para funcionar a partir de qualquer diretório corrente.

## Integração contínua

O workflow `.github/workflows/validacao.yml` executa este mesmo comando em push e pull request. Enquanto não houver testes, a etapa informa a ausência e segue. Quando houver testes, uma falha interrompe a validação.
