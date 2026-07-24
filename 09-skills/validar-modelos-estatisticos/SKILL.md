---
name: validar-modelos-estatisticos
description: Validar e comparar modelos estatísticos e de machine learning para regressão, classificação, ranking, sobrevivência, séries temporais e previsões probabilísticas. Usar para definir particionamento, cross-validation, backtesting, baselines, métricas, calibração, incerteza, estabilidade, robustez, desempenho por grupos, drift, leakage, comparação estatística, limiares e utilidade para decisão. Simular o uso real, preservar dependências temporais e de grupo e separar seleção de avaliação final. Priorizar Python, usar SQL na preparação e recorrer a R somente quando não houver solução viável em Python.
---

# Validar modelos estatísticos

## Objetivo

Estimar com honestidade como um modelo se comportará fora dos dados usados para construí-lo e se seu desempenho é estável, calibrado e útil para a decisão. Tratar validação como desenho experimental do processo de modelagem, não como etapa final decorativa.

Usar `auditar-dados-estatisticos` para qualidade e leakage, `analisar-series-temporais` para backtesting temporal e `orientar-analise-estatistica` para integrar o parecer ao estudo.

## Definir o cenário de uso

Registrar:

- unidade prevista e população de implantação;
- alvo, horizonte e momento da decisão;
- informação disponível na predição;
- ação tomada a partir da saída;
- custo de falsos positivos, falsos negativos e erros grandes;
- frequência de atualização e retreinamento;
- grupos, períodos e regimes críticos;
- baseline atual e requisito mínimo de melhoria.

Validar no cenário que representa o uso real. Não aceitar uma divisão conveniente que torne treino e teste mais parecidos do que serão em produção.

## Construir o particionamento

Escolher entre:

- holdout aleatório estratificado;
- cross-validation;
- group split ou leave-one-group-out;
- divisão temporal;
- rolling ou expanding window;
- nested cross-validation;
- validação geográfica, por domínio ou período externo;
- bootstrap de desempenho.

Consultar [desenhos-de-validacao.md](references/desenhos-de-validacao.md).

Preservar entidade, grupo, tempo, hierarquia e origem do dado. Aplicar gap ou embargo quando janelas ou rótulos próximos puderem contaminar a avaliação.

## Isolar todo o aprendizado

Ajustar dentro de cada fold:

- imputação;
- escalonamento;
- codificação;
- balanceamento ou amostragem;
- seleção de features;
- redução de dimensionalidade;
- geração de features que aprendam com dados;
- calibração;
- escolha de limiar;
- hiperparâmetros;
- seleção de modelo ou ensemble.

Manter o conjunto final fora de todas essas escolhas. Não reutilizar o teste como placar iterativo.

## Definir baselines

Comparar com:

- regra simples;
- média, mediana ou prevalência;
- último valor ou sazonal ingênuo;
- modelo operacional atual;
- família estatística simples;
- modelo sem a feature ou bloco em avaliação.

Usar ablation para medir ganho incremental. Um modelo só é útil se superar uma alternativa relevante de maneira estável e material.

## Escolher métricas pela decisão

Consultar [metricas-por-tarefa.md](references/metricas-por-tarefa.md).

Avaliar múltiplas dimensões:

- discriminação ou ordenação;
- magnitude do erro;
- viés;
- calibração;
- cobertura de intervalos;
- desempenho nas caudas;
- utilidade ou custo esperado;
- estabilidade por fold, grupo e tempo.

Não escolher métrica apenas por convenção. Definir uma métrica principal e complementares antes de comparar extensamente os modelos.

## Avaliar classificação

Examinar:

- prevalência;
- ROC-AUC e PR-AUC;
- log loss e Brier score;
- calibração global e por faixa;
- sensibilidade, especificidade, precisão e NPV;
- matriz de confusão em limiares relevantes;
- curva de decisão, custo ou valor esperado;
- estabilidade por subgrupos.

Escolher limiar com dados de validação e função de custo. Não usar 0,5 automaticamente. Não reportar apenas acurácia em classes desbalanceadas.

## Avaliar regressão

Examinar:

- MAE, RMSE e métricas escaladas;
- bias e distribuição dos resíduos;
- erro relativo apenas quando denominadores forem adequados;
- desempenho por faixas do alvo;
- calibração entre previsto e observado;
- intervalos preditivos;
- estabilidade por segmentos.

Não depender apenas de R². Reportar erro na unidade do problema e comparar com variabilidade e tolerância operacional.

## Avaliar previsões probabilísticas

Examinar:

- proper scoring rules;
- pinball loss por quantil;
- CRPS;
- cobertura e largura de intervalos;
- calibração por quantil;
- sharpness;
- estabilidade da distribuição preditiva.

Não avaliar quantis isoladamente sem verificar monotonicidade e cobertura conjunta. Intervalos muito largos podem estar calibrados e ainda ser inúteis.

## Avaliar séries temporais

Usar múltiplas origens e horizonte compatível com a operação. Reportar desempenho por:

- horizonte;
- origem;
- calendário e eventos;
- série e hierarquia;
- volume;
- regime.

Não embaralhar o tempo nem usar exógenas futuras observadas quando elas não estarão disponíveis. Comparar com baselines sazonais.

## Comparar modelos

Usar diferenças pareadas no mesmo conjunto de folds, origens ou observações. Reportar:

- diferença média e mediana;
- intervalo de incerteza;
- frequência de vitória;
- estabilidade entre recortes;
- relevância prática;
- custo, latência e complexidade.

Considerar bootstrap pareado, permutation tests, Diebold–Mariano para previsões sob condições adequadas ou procedimentos de comparação múltipla. Não tratar folds como observações independentes sem avaliar a dependência.

## Avaliar calibração e incerteza

Consultar [calibracao-estabilidade-e-drift.md](references/calibracao-estabilidade-e-drift.md).

Distinguir:

- incerteza aleatória;
- incerteza de parâmetros;
- incerteza de modelo;
- mudança de domínio.

Calibrar apenas em dados separados do ajuste principal e reavaliar no teste. Usar Platt, isotônica, beta calibration, conformal ou métodos específicos conforme a tarefa.

## Avaliar grupos e riscos

Reportar desempenho por grupos substantivamente relevantes e por qualidade de cobertura. Verificar:

- diferença de erro;
- calibração;
- taxas de decisão;
- tamanhos amostrais;
- incerteza;
- interseções de grupos;
- impacto operacional.

Não ocultar grupos pequenos em uma média global. Também não concluir desigualdade com estimativas extremamente instáveis sem mostrar incerteza.

## Planejar monitoramento

Definir:

- distribuição de features e alvo;
- qualidade e disponibilidade de dados;
- estabilidade das previsões;
- desempenho atrasado;
- calibração;
- drift de população e conceito;
- limites de alerta;
- champion/challenger;
- gatilhos de investigação, recalibração e retreinamento.

Evitar retreinar automaticamente apenas porque uma métrica de drift ultrapassou um limiar; investigar impacto e causa.

## Implementar

Priorizar:

- SQL para construir coortes, cortes temporais e métricas operacionais;
- Pandas, Polars ou PySpark para preparação;
- Scikit-learn para pipelines, validação e calibração;
- Statsmodels e SciPy para inferência e comparação;
- libraries temporais para backtesting;
- MAPIE ou métodos conformais adequados para intervalos;
- Evidently ou ferramentas equivalentes quando monitoramento automatizado for útil.

Fixar sementes e registrar versões, folds, features, hiperparâmetros e baselines. Recorrer a R somente quando não houver implementação viável em Python.

## Entregar em quatro camadas

Apresentar:

1. fundamento acadêmico sobre generalização, calibração, incerteza e desenho;
2. procedimento técnico de particionamento, métricas, comparação e diagnóstico;
3. interpretação prática do ganho, risco e utilidade;
4. código documentado com objetivo, entradas, processamento, saída esperada e interpretação.

Encerrar com:

- cenário de uso e baseline;
- desenho de validação;
- métrica principal e complementares;
- resultado agregado e distribuição entre recortes;
- calibração, estabilidade e incerteza;
- desempenho por grupos;
- limitações e riscos;
- parecer: rejeitar, revisar, testar controladamente ou aprovar para o uso definido.
