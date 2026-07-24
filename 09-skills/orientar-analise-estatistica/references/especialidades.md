# Catálogo de especialidades estatísticas

Consultar este catálogo ao decompor um estudo. Combinar somente as especialidades exigidas pela pergunta e pelos dados.

## 1. Auditoria estatística de dados

Usar para examinar unidade observacional, cobertura, duplicidades, valores ausentes, outliers, censura, viés de seleção, qualidade de mensuração e mudanças no processo gerador dos dados.

Possível skill futura: `auditar-dados-estatisticos`.

## 2. Análise exploratória

Usar para descrever distribuições, dispersão, assimetria, relações, segmentos, padrões incomuns e hipóteses geradoras. Marcar resultados exploratórios como tais e evitar confirmação no mesmo conjunto sem correção ou validação.

Possível skill futura: `executar-analise-exploratoria`.

## 3. Testes de hipótese e inferência

Usar para estimar diferenças ou associações com incerteza. Definir estimando, hipóteses, tamanho de efeito, intervalo de confiança, nível de significância, poder e multiplicidade antes de escolher teste paramétrico, não paramétrico, permutacional ou bootstrap.

Possível skill futura: `formular-testes-de-hipotese`.

## 4. Regressão e modelos estatísticos

Usar para modelar desfechos contínuos, binários, contagens, proporções, duração ou estruturas hierárquicas. Considerar modelos lineares, GLMs, modelos mistos, sobrevivência, quantílicos e robustos conforme o processo gerador.

Possível skill futura: `modelar-regressao`.

## 5. Séries temporais

Usar quando a ordem temporal, autocorrelação, tendência, sazonalidade, defasagens, intervenções ou previsão forem centrais. Preservar a ordem temporal, investigar estabilidade e usar backtesting ou walk-forward.

Possível skill futura: `analisar-series-temporais`.

## 6. Inferência causal

Usar quando a pergunta contiver efeito, impacto ou consequência de uma intervenção ou exposição. Definir tratamento, desfecho, estimando, população e janela temporal; explicitar DAG, confundidores, suposições de identificação, método e análises de sensibilidade.

Possível skill futura: `analisar-causalidade`.

## 7. Planejamento experimental

Usar para A/B tests, ensaios, fatoriais, randomização por grupos, testes sequenciais e experimentos com interferência. Definir unidade de randomização, métrica primária, MDE, poder, duração e regras de parada antes da execução.

Possível skill futura: `planejar-experimentos`.

## 8. Inferência bayesiana

Usar quando conhecimento prévio, atualização probabilística, modelos hierárquicos ou decisões sob incerteza justificarem a abordagem. Realizar checagens preditivas prévias e posteriores, diagnóstico das cadeias e análise de sensibilidade aos priors.

Possível skill futura: `realizar-inferencia-bayesiana`.

## 9. Análise multivariada e segmentação

Usar para estruturas de covariância, variáveis latentes, redução de dimensionalidade, agrupamento e múltiplos desfechos. Padronizar quando necessário, justificar distância ou similaridade e avaliar estabilidade dos componentes ou clusters.

Possível skill futura: `analisar-dados-multivariados`.

## 10. Validação de modelos

Usar para comparar modelos, estimar generalização, calibração, estabilidade, drift, incerteza e adequação à decisão. Escolher particionamento compatível com tempo, grupos e hierarquia e manter um conjunto final não usado na seleção quando possível.

Possível skill futura: `validar-modelos-estatisticos`.

## Regras de roteamento

- Combinar auditoria com toda análise que dependa de dados ainda não avaliados.
- Combinar séries temporais com causalidade quando tratamento e desfecho evoluírem no tempo.
- Combinar regressão com causalidade somente quando a especificação servir ao estimando causal e às suposições de identificação.
- Combinar validação de modelos com todo objetivo preditivo.
- Combinar planejamento experimental com testes de hipótese antes de coletar dados.
- Usar análise exploratória para compreender dados, sem apresentá-la como confirmação independente.
