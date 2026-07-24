---
name: realizar-inferencia-bayesiana
description: Formular, ajustar, diagnosticar e interpretar modelos bayesianos para estimação, previsão e decisão sob incerteza. Usar quando conhecimento prévio precisar ser incorporado, a amostra for pequena, houver estrutura hierárquica, regularização probabilística, atualização sequencial, comparação de hipóteses, previsão posterior ou necessidade de probabilidades diretamente interpretáveis. Cobrir prior, verossimilhança, posterior, MCMC, inferência variacional, modelos hierárquicos, checks preditivos, comparação, sensibilidade e decisão. Priorizar Python, usar SQL na preparação e recorrer a R somente quando não houver solução viável em Python.
---

# Realizar inferência bayesiana

## Objetivo

Construir modelos probabilísticos coerentes com o processo gerador dos dados, quantificar incerteza e apoiar decisões sem reduzir a análise a uma estimativa pontual. Distinguir informação prévia, evidência observada e implicações posteriores.

Usar `auditar-dados-estatisticos` antes da modelagem e `validar-modelos-estatisticos` quando houver comparação preditiva.

## Formular o problema

Registrar:

- unidade de análise, população e horizonte;
- parâmetros, quantidades latentes e preditivas de interesse;
- estrutura de grupos, tempo, censura ou dependência;
- decisão apoiada e custo dos erros;
- informação prévia legítima e sua origem;
- estimando ou distribuição preditiva requerida.

Não escolher abordagem bayesiana apenas pela disponibilidade de software. Explicar qual vantagem substantiva ela oferece.

## Especificar o modelo

Definir explicitamente:

1. verossimilhança compatível com suporte e mecanismo do desfecho;
2. função de ligação e estrutura sistemática;
3. priors próprios, interpretáveis e na escala correta;
4. hierarquia e pooling quando houver grupos;
5. dependências temporais, espaciais ou multivariadas;
6. quantidades derivadas relevantes à decisão.

Executar prior predictive checks. Rejeitar priors que gerem valores impossíveis ou excessivamente implausíveis.

## Escolher a inferência

Preferir métodos de Monte Carlo quando a precisão posterior for importante:

- NUTS/HMC para modelos diferenciáveis;
- Gibbs ou Metropolis quando apropriado;
- SMC para atualização ou posteriores complexas;
- inferência variacional para escala, declarando aproximações;
- soluções conjugadas ou analíticas quando disponíveis.

Não tratar aproximação variacional como equivalente automático a MCMC. Comparar quando a decisão for sensível às caudas ou correlações posteriores.

## Diagnosticar

Para MCMC, verificar:

- cadeias e trace plots;
- R-hat;
- effective sample size;
- divergências;
- energia e geometria;
- autocorrelação;
- estabilidade entre inicializações;
- Monte Carlo standard error.

Não interpretar o posterior enquanto houver falhas materiais de convergência. Corrigir parametrização, escala, priors ou geometria antes de simplesmente aumentar iterações.

## Validar

Realizar:

- posterior predictive checks;
- calibração preditiva;
- validação fora da amostra quando houver objetivo preditivo;
- LOO-CV ou comparação adequada;
- análise de sensibilidade a priors;
- recuperação de parâmetros em modelos complexos;
- avaliação de identificabilidade;
- comparação com baseline simples.

Evitar usar Bayes factor sem examinar dependência dos priors. Não selecionar modelo apenas pelo menor LOO sem considerar incerteza, adequação e interpretabilidade.

## Interpretar

Reportar:

- distribuição posterior;
- média, mediana ou estimativa adequada;
- intervalo de credibilidade;
- probabilidade de direção;
- probabilidade de exceder limiar relevante;
- distribuição preditiva;
- heterogeneidade entre grupos;
- sensibilidade a priors e especificações.

Não traduzir intervalo de credibilidade como garantia de repetição do experimento. Não converter associação posterior em efeito causal sem identificação.

## Apoiar decisões

Quando houver ação, definir utilidade, perda ou custo e comparar decisões pela utilidade posterior esperada. Mostrar como a decisão muda sob cenários, priors e aversão ao risco.

Separar:

- incerteza sobre parâmetros;
- variabilidade futura;
- incerteza de modelo;
- incerteza não representada pelos dados.

## Implementar

Priorizar:

- SQL para construção da população analítica;
- Pandas, Polars ou PySpark para preparação;
- PyMC, Bambi ou NumPyro para modelagem;
- ArviZ para diagnóstico, comparação e visualização;
- Statsmodels ou Scikit-learn para baselines.

Usar sementes, coordenadas e nomes explícitos. Manter transformações dentro do pipeline e preservar grupos e ordem temporal.

## Entregar em quatro camadas

Apresentar:

1. fundamento acadêmico do modelo, priors e inferência;
2. procedimento técnico de ajuste, diagnóstico e validação;
3. interpretação prática das probabilidades e decisões;
4. código documentado com objetivo, entradas, processamento, saída esperada e interpretação.

Encerrar com modelo, priors, diagnósticos, checks preditivos, sensibilidade, conclusão permitida, limitações e decisão recomendada.
