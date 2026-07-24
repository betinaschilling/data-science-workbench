# Identificação e DAGs

## Papéis das variáveis

| Papel | Relação | Conduta típica |
|---|---|---|
| Confundidor | causa tratamento e desfecho | ajustar se pré-tratamento e medido |
| Mediador | tratamento causa mediador, que causa desfecho | não ajustar para efeito total |
| Colisor | recebe setas de duas causas | evitar condicionar |
| Instrumento | afeta tratamento sem caminho direto ao desfecho | usar somente com suposições fortes |
| Modificador | altera magnitude do efeito | modelar heterogeneidade |
| Proxy | mede imperfeitamente variável relevante | avaliar erro de mensuração |
| Seleção | determina entrada ou observação | avaliar viés por condicionamento |

## Checklist

- Definir temporalidade de cada nó.
- Incluir causas comuns plausíveis, mesmo não observadas.
- Não construir DAG apenas a partir dos dados.
- Identificar conjunto de ajuste mínimo e alternativas válidas.
- Distinguir efeito total, direto e mediado.
- Avaliar seleção e censoring.
- Tornar explícitas variáveis não medidas.

## Identificação

Backdoor adjustment exige bloquear caminhos não causais sem bloquear o caminho de interesse. Frontdoor exige mediação completa e condições raramente triviais. Instrumentos exigem relevância, independência e exclusão. Quando nenhuma estratégia for defensável, não há ajuste algorítmico que produza causalidade.
