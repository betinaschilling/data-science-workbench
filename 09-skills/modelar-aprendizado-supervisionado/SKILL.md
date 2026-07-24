---
name: modelar-aprendizado-supervisionado
description: Formular, treinar, ajustar, avaliar e interpretar modelos supervisionados para regressão preditiva, classificação, probabilidade, propensão, churn, risco, scoring e ranking. Usar quando houver target observado e o objetivo principal for generalizar para novas observações; selecionar loss, baseline, particionamento, features, algoritmo, calibração, threshold e métricas conforme custo e operação. Cobrir modelos lineares, árvores, boosting, ensembles e redes quando justificadas. Priorizar Python, usar SQL na preparação e não confundir previsão com inferência causal.
---

# Modelar aprendizado supervisionado

## Formular a tarefa

Definir target, unidade de previsão, população, horizonte, instante de decisão, disponibilidade das features e uso da saída. Classificar como regressão, classificação, probabilidade, ranking ou previsão de risco.

Definir custo dos erros, baseline e ganho mínimo útil antes do tuning.

## Preparar sem vazamento

Usar `preparar-dados-analiticos` e `selecionar-e-construir-atributos`. Separar treino, validação e teste antes de aprender imputação, encoding, escala ou seleção.

Respeitar tempo, grupos, indivíduos e hierarquias. Nunca usar informação indisponível no instante real da previsão.

## Construir baseline

Comparar com regra simples e operacional:

- média, mediana ou último valor;
- regressão linear ou logística;
- classe majoritária;
- score ou regra vigente;
- modelo sazonal ingênuo quando houver tempo.

Complexidade só é aceita com ganho estável e relevante.

## Selecionar modelos

Considerar conforme dados e restrições:

- modelos lineares regularizados;
- árvores e random forests;
- CatBoost, LightGBM ou XGBoost;
- ensembles;
- redes neurais quando escala e estrutura justificarem;
- modelos específicos para ranking, sobrevivência ou contagem.

Preservar monotonicidade, interpretabilidade, latência e restrições quando forem requisitos.

## Ajustar

Usar busca de hiperparâmetros dentro da validação. Limitar espaço pela lógica do modelo, controlar aleatoriedade e registrar configuração.

Tratar desbalanceamento pela função de custo, pesos, amostragem apenas no treino e métricas adequadas. Não otimizar acurácia por padrão.

## Avaliar

Usar `validar-modelos-estatisticos`. Avaliar:

- desempenho fora da amostra;
- incerteza das métricas;
- calibração;
- thresholds e curvas de custo;
- estabilidade por tempo e grupo;
- desempenho em segmentos críticos;
- análise de resíduos e erros;
- robustez a drift e perturbações;
- ablation de grupos de features.

Manter o teste intocado até a escolha final. Não selecionar modelo pelo melhor resultado isolado.

## Interpretar

Usar `explicar-modelos-e-resultados` quando disponível. Separar importância preditiva, efeito marginal, associação e causalidade. Conferir se explicações são estáveis e coerentes com a disponibilidade das features.

## Entregar

Apresentar:

1. problema, target e decisão;
2. desenho de validação e baseline;
3. pipeline e modelos;
4. métricas com incerteza e segmentações;
5. calibração, threshold e custo;
6. análise de erros;
7. explicabilidade e limitações;
8. recomendação ou rejeição do modelo;
9. código Python documentado e SQL de preparação quando necessário.

Não recomendar implantação sem avaliar dados, operação, monitoramento e risco, mesmo que a métrica seja alta.
