---
name: analisar-causalidade
description: Formular, identificar, estimar, diagnosticar e interpretar efeitos causais em dados experimentais e observacionais. Usar para perguntas de impacto, efeito de tratamento, política, campanha, preço, clima, intervenção ou exposição; construir DAGs, definir estimandos, selecionar conjuntos de ajuste e aplicar randomização, matching, propensity score, ponderação, g-computation, doubly robust, Double Machine Learning, diferenças-em-diferenças, event studies, controle sintético, regression discontinuity, variáveis instrumentais, séries temporais interrompidas e heterogeneidade causal. Exigir estratégia de identificação, temporalidade, overlap, falsificações e sensibilidade; não tratar correlação, Granger, SHAP ou desempenho preditivo como causalidade. Priorizar Python, usar SQL na preparação e recorrer a R somente quando não houver solução viável em Python.
---

# Analisar causalidade

## Objetivo

Responder qual seria a diferença no desfecho se a mesma população fosse exposta a alternativas distintas, deixando explícito por que o contrafactual não observado pode ser aproximado. Separar identificação causal, estimação estatística e interpretação substantiva.

Usar `orientar-analise-estatistica` para coordenar o estudo, `auditar-dados-estatisticos` para cobertura e mensuração, e `analisar-series-temporais` quando a estrutura temporal for central.

## Formular a pergunta causal

Definir:

- tratamento ou exposição;
- níveis ou versões do tratamento;
- desfecho;
- população-alvo;
- tempo zero, janela de exposição e janela de resultado;
- unidade de intervenção e unidade de análise;
- estimando: ATE, ATT, ATC, CATE, LATE, efeito total, direto ou mediado;
- intervenção hipotética ou política;
- interferência, spillovers e adesão.

Usar o framework de target trial quando útil: elegibilidade, estratégias, atribuição, seguimento, desfecho, estimando e análise.

Não usar “impacto” sem definir qual contraste, em quem e em qual horizonte.

## Construir a teoria causal

Representar conhecimento substantivo com DAG ou descrição causal equivalente. Classificar variáveis como:

- causa comum;
- mediador;
- colisor;
- proxy;
- instrumento;
- modificador de efeito;
- variável pós-tratamento;
- seleção ou censura.

Consultar [identificacao-e-dags.md](references/identificacao-e-dags.md).

Selecionar ajuste para bloquear backdoor paths sem abrir caminhos por colisores. Não escolher confundidores apenas por correlação, importância preditiva ou valor-p.

## Avaliar identificabilidade

Declarar as suposições necessárias:

- consistência e versões bem definidas;
- exchangeability ou ausência de confundimento não medido;
- positividade;
- não interferência ou estrutura explícita de interferência;
- temporalidade correta;
- mensuração suficiente;
- forma funcional quando necessária;
- suposições específicas do desenho.

Se as suposições forem implausíveis ou os dados não permitirem verificar suporte, restringir o estimando ou declarar que o efeito não é identificável.

## Escolher a estratégia

Consultar [desenhos-e-metodos.md](references/desenhos-e-metodos.md).

Priorizar, quando disponíveis:

1. experimento randomizado bem executado;
2. experimento natural ou regra de atribuição defensável;
3. desenho quase-experimental;
4. ajuste observacional com confundidores medidos;
5. análise associativa explicitamente rotulada quando identificação falhar.

Não escolher método pela sofisticação. Escolher pelo mecanismo de atribuição e pelas suposições que os dados e o contexto conseguem sustentar.

## Preparar os dados causais

Construir unidade de análise e linha do tempo sem usar informação futura. Verificar:

- elegibilidade antes do tratamento;
- covariáveis medidas antes da exposição;
- tratamento definido sem olhar o desfecho futuro;
- censoring e competing events;
- immortal time bias;
- duplicidades e múltiplos episódios;
- missingness diferencial;
- frequência e precisão da exposição;
- contaminação entre grupos;
- suporte comum.

Não ajustar variáveis criadas após o tratamento, salvo quando o estimando e o método exigirem tratamento explícito de mediação ou exposição variável no tempo.

## Estimar efeitos

Para ajuste observacional, considerar:

- outcome regression ou g-computation;
- propensity score matching;
- estratificação;
- inverse probability weighting;
- overlap weights;
- augmented IPW;
- TMLE quando houver implementação confiável;
- Double Machine Learning com cross-fitting;
- generalized propensity para tratamentos contínuos.

Verificar balanceamento depois do ajuste. Não usar apenas o C-statistic do propensity model. Não incluir o desfecho na estimação do propensity score.

Para tratamentos variáveis no tempo, considerar marginal structural models, g-formula paramétrica ou métodos apropriados ao confundimento dependente do tempo.

## Aplicar quase-experimentos

### Diferenças-em-diferenças

Definir grupos, tempo de adoção e janela. Examinar tendências prévias, antecipação, composição, spillovers e tratamento escalonado. Usar estimadores robustos à heterogeneidade quando two-way fixed effects for inadequado.

### Regression discontinuity

Verificar regra de cutoff, manipulação, continuidade das covariáveis, bandwidth, forma local e outros eventos no limiar. Priorizar estimativa local.

### Variáveis instrumentais

Defender relevância, independência, exclusão e monotonicidade quando LATE for o estimando. Reportar força do primeiro estágio e reconhecer que exclusão não é testável diretamente.

### Controle sintético

Definir donor pool, período pré-tratamento, qualidade do fit, contaminação e placebos. Não interpretar resultado sem mostrar a construção do contrafactual.

### Séries temporais interrompidas

Modelar nível, tendência, autocorrelação, sazonalidade, intervenções concorrentes e tempo suficiente antes/depois.

## Usar ML causal

Usar Double ML, causal forests, meta-learners ou learners ortogonais para nuisance functions, heterogeneidade ou tratamentos complexos depois de definir o estimando e a identificação.

Aplicar sample splitting e cross-fitting. Validar overlap, estabilidade e heterogeneidade fora da amostra quando possível.

Não usar SHAP, feature importance, PDP ou Granger como estimadores causais. Não interpretar uma causal forest como correção automática de confundimento não medido.

## Diagnosticar

Consultar [diagnosticos-e-sensibilidade.md](references/diagnosticos-e-sensibilidade.md).

Avaliar:

- balanceamento de covariáveis;
- overlap e pesos extremos;
- tamanho amostral efetivo;
- especificação;
- tendências prévias;
- placebos e negative controls;
- predição do contrafactual;
- influência de unidades;
- estabilidade por especificações;
- heterogeneidade;
- sensibilidade a confundimento não medido.

Não usar um único teste de falsificação como prova. Construir um conjunto coerente de evidências.

## Quantificar incerteza

Usar erros-padrão robustos ou clusterizados na unidade de atribuição, bootstrap que preserve o desenho, randomization inference, influência semiparamétrica ou procedimentos específicos do estimador.

Contabilizar estimação de nuisance functions, matching, pesos e seleção quando relevante. Não usar bootstrap ingênuo de linhas em dados agrupados ou temporais.

## Interpretar

Reportar:

- estimando e população;
- escala absoluta e relativa quando útil;
- intervalo de incerteza;
- horizonte;
- heterogeneidade pré-especificada;
- suposições;
- diagnósticos;
- população para a qual o efeito pode ser transportado.

Evitar “provar causalidade”. Usar linguagem proporcional: efeito identificado sob suposições, evidência compatível, análise quase-experimental ou associação quando identificação não for suficiente.

## Implementar

Priorizar:

- SQL para coortes, tempo zero, elegibilidade, exposições e painéis;
- Pandas, Polars ou PySpark para preparação;
- Statsmodels e linearmodels para econometria;
- DoWhy para explicitar estimando, identificação e refutações;
- EconML para Double ML e heterogeneidade;
- CausalML quando adequado e auditável;
- SciPy, Scikit-learn e NumPy para nuisance models;
- bibliotecas específicas de DiD, synthetic control ou RDD com implementação confiável.

Recorrer a R somente se o estimador necessário não tiver solução viável e validada em Python; declarar a exceção.

## Entregar em quatro camadas

Apresentar:

1. fundamento acadêmico do estimando, contrafactual, identificação e suposições;
2. procedimento técnico de desenho, estimação, diagnóstico e sensibilidade;
3. interpretação prática da magnitude e da decisão;
4. código documentado com objetivo, entradas, processamento, saída esperada e interpretação.

Encerrar com:

- pergunta causal e estimando;
- DAG ou teoria causal;
- estratégia de identificação;
- método e justificativa;
- efeito, incerteza e população;
- diagnósticos, placebos e sensibilidade;
- ameaças à validade;
- conclusão permitida;
- evidência adicional necessária para fortalecer a inferência.
