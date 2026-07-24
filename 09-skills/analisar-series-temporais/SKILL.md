---
name: analisar-series-temporais
description: Conduzir análises completas de séries temporais, incluindo auditoria temporal, decomposição, tendência, sazonalidade, estacionaridade, autocorrelação, defasagens, intervenções, previsão pontual e probabilística, regressão temporal, modelos clássicos, machine learning, deep learning, modelos fundacionais e previsão hierárquica. Usar em dados ordenados no tempo, forecasting, demanda, receita, vendas, clima, sensores, economia, avaliação de intervenções temporais, comparação de modelos, backtesting, detecção de mudanças ou análise de relações defasadas. Preservar a ordem temporal, prevenir leakage, priorizar Python, usar SQL na preparação e recorrer a R somente quando não houver solução viável em Python.
---

# Analisar séries temporais

## Objetivo

Conduzir o ciclo temporal completo: compreender o processo gerador, auditar o eixo do tempo, selecionar a família metodológica, estimar, diagnosticar, validar fora da amostra e interpretar resultados sem confundir previsão, associação temporal e causalidade.

Se o estudo exigir coordenação com outras especialidades, usar também `orientar-analise-estatistica`.

## Delimitar o problema temporal

Identificar antes de modelar:

- variável-alvo e sua unidade;
- frequência observada e frequência da decisão;
- unidade ou série identificadora;
- horizonte, origem e cadência das previsões;
- disponibilidade real de cada variável no instante da previsão;
- sazonalidades, calendário, eventos, intervenções e mudanças conhecidas;
- necessidade de previsão pontual, intervalo, quantis, cenários ou efeito de intervenção;
- estrutura agregada, hierárquica, agrupada, painel ou séries relacionadas;
- custo dos diferentes tipos de erro.

Classificar o objetivo em uma ou mais rotas:

1. descrição e diagnóstico temporal;
2. inferência sobre relações e defasagens;
3. previsão;
4. detecção de intervenção ou mudança;
5. previsão hierárquica ou reconciliada;
6. avaliação causal temporal.

Não usar uma boa previsão como evidência automática de mecanismo ou causalidade.

## Auditar o eixo temporal

Verificar:

- parsing, fuso horário, calendário e ordenação;
- frequência real, datas ausentes, duplicidades e observações irregulares;
- início e fim de cobertura por série;
- zeros estruturais, censura, valores ausentes e períodos sem operação;
- mudanças de definição, fonte, loja, produto, sensor ou processo;
- granularidade incompatível entre alvo e variáveis exógenas;
- revisões retroativas e disponibilidade histórica das features;
- sobrevivência seletiva de séries e viés de cobertura.

Criar um calendário explícito quando a ausência de uma data tiver significado diferente de valor zero. Não imputar antes de compreender o mecanismo da ausência.

## Diagnosticar a estrutura

Analisar, conforme a pergunta:

- gráficos da série, distribuição por calendário e decomposição;
- tendência, sazonalidade múltipla, ciclos, feriados e eventos móveis;
- ACF, PACF, periodograma ou densidade espectral;
- quebras estruturais, mudanças de nível, variância e regime;
- estacionaridade e ordem de integração;
- autocorrelação e heterocedasticidade dos resíduos;
- relações contemporâneas e defasadas entre séries.

Usar ADF, KPSS ou outros testes como evidências complementares, não como decisões automáticas. Diferenciar somente quando a interpretação e o modelo exigirem; não aplicar `diff(1).diff(7)` como regra universal.

Consultar [diagnostico.md](references/diagnostico.md) para selecionar testes e transformações.

## Selecionar a família de modelos

Começar com baselines compatíveis com a frequência e a sazonalidade. Escolher modelos pela estrutura dos dados, horizonte, volume de séries, necessidade de explicabilidade, disponibilidade de covariáveis e restrições operacionais.

Considerar:

- ingenuidade, sazonal ingênuo e médias históricas;
- ETS, Theta, ARIMA/SARIMA/SARIMAX, modelos estruturais e espaço de estados;
- regressão dinâmica, funções de transferência, VAR/VECM e modelos de intervenção;
- Prophet, TBATS, MSTL e modelos de sazonalidade múltipla;
- CatBoost, LightGBM, XGBoost e modelos globais com features temporais;
- redes recorrentes, TCNs, N-BEATS/N-HiTS e Transformers temporais;
- modelos fundacionais como Chronos e TimesFM;
- modelos locais, globais, painel e hierárquicos;
- previsões probabilísticas, quantílicas e conformais.

Consultar [familias-de-modelos.md](references/familias-de-modelos.md) antes de escolher uma família não trivial.

Não presumir que o modelo mais complexo será melhor. Exigir comparação com baselines e avaliar custo, estabilidade e reprodutibilidade.

## Construir features sem vazamento

Gerar apenas informações disponíveis na origem da previsão:

- lags do alvo e das covariáveis;
- médias, somas, dispersões e extremos em janelas passadas;
- calendário, feriados, eventos e ciclo comercial conhecidos;
- preços, promoções ou planos realmente conhecidos antecipadamente;
- previsões ou cenários de variáveis exógenas futuras;
- codificações de série, grupo e hierarquia.

Aplicar deslocamento antes de janelas móveis quando necessário. Ajustar imputadores, escaladores, decomposições e seletores de features somente dentro de cada janela de treinamento.

Declarar como serão obtidos os valores futuros das covariáveis. Não avaliar um modelo com exógenas futuras observadas se elas não estarão disponíveis em produção.

## Validar temporalmente

Usar holdout temporal ou backtesting com origens móveis. Alinhar:

- horizonte de teste ao horizonte operacional;
- tamanho e expansão da janela ao regime esperado;
- número de folds à quantidade de dados e sazonalidades;
- refit à cadência real;
- gap ou embargo ao risco de contaminação;
- avaliação por série, horizonte, segmento e período crítico.

Comparar com baselines e reportar distribuição dos erros entre folds, não apenas média agregada. Para múltiplas séries, usar agregações ponderadas coerentes com o negócio e também examinar caudas.

Consultar [validacao-e-metricas.md](references/validacao-e-metricas.md).

## Diagnosticar o modelo

Verificar:

- resíduos sem estrutura temporal explorável;
- viés por horizonte, calendário, série, segmento e regime;
- estabilidade de parâmetros ou importância das features;
- calibração e cobertura de intervalos ou quantis;
- sensibilidade a janelas, lags, transformações e hiperparâmetros;
- degradação em eventos, mudanças estruturais e séries intermitentes;
- coerência entre níveis hierárquicos.

Quando os resíduos preservarem autocorrelação relevante, tratar o modelo como incompleto ou explicar por que isso não prejudica a decisão.

## Tratar hierarquias e múltiplas séries

Definir a matriz de agregação e distinguir estruturas hierárquicas de estruturas agrupadas. Comparar bottom-up, top-down, middle-out e reconciliação ótima, como MinT, quando aplicável.

Avaliar simultaneamente:

- acurácia em cada nível;
- coerência entre previsões;
- estabilidade para séries pequenas;
- pesos comerciais e custo de erro;
- impacto da reconciliação nos intervalos.

Não desagregar uma previsão agregada apenas por proporções históricas sem validar a estabilidade dessas proporções.

## Avaliar relações e intervenções temporais

Para relações defasadas, controlar tendência, sazonalidade e autocorrelação antes de interpretar correlação cruzada. Usar prewhitening quando adequado.

Tratar Granger como precedência preditiva condicional, não como causalidade substantiva. Para efeito causal, definir intervenção, contrafactual, confundidores, antecipação, spillovers e tendência prévia; combinar com a especialidade de inferência causal.

Considerar regressão segmentada, intervenção em espaço de estados, diferenças-em-diferenças temporais, controle sintético ou séries temporais interrompidas conforme o desenho.

## Implementar

Priorizar:

- Pandas, Polars ou PySpark para preparação;
- NumPy, SciPy e Statsmodels para diagnóstico e econometria;
- Scikit-learn, CatBoost, LightGBM e XGBoost para ML;
- StatsForecast, MLForecast, NeuralForecast ou sktime para fluxos temporais;
- PyTorch e bibliotecas especializadas para deep learning;
- HierarchicalForecast para reconciliação;
- SHAP ou métodos apropriados para explicabilidade, sem inferência causal indevida.

Usar SQL para extração, calendário, agregação e controles anteriores à modelagem. Recorrer a R somente se uma capacidade necessária não tiver implementação viável em Python e explicar essa exceção.

## Entregar em quatro camadas

Para cada etapa relevante, apresentar:

1. fundamento acadêmico;
2. procedimento técnico;
3. interpretação prática ou de negócio;
4. código documentado com objetivo, entradas, processamento, saída esperada e interpretação.

Encerrar com:

- resposta à pergunta temporal;
- modelo ou método escolhido e baseline;
- desenho de validação;
- métricas por horizonte e segmentos importantes;
- incerteza, diagnósticos e estabilidade;
- limitações e riscos de mudança de regime;
- estratégia de atualização, monitoramento e próximos passos.
