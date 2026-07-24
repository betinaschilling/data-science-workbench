---
name: planejar-experimentos
description: Desenhar, dimensionar, executar, monitorar e analisar experimentos controlados, incluindo A/B tests, randomização individual ou por cluster, desenhos fatoriais, crossover, switchback, stepped-wedge, testes sequenciais e experimentos com interferência. Usar para definir hipótese, estimando, unidade de randomização, métricas primárias e guardrails, MDE, poder, amostra, duração, alocação, estratificação, regras de parada, checagens de randomização, intenção de tratar, não adesão, múltiplas comparações e decisão de rollout. Prevenir peeking, sample ratio mismatch e contaminação. Priorizar Python, usar SQL na preparação e recorrer a R somente quando não houver solução viável em Python.
---

# Planejar experimentos

## Objetivo

Projetar um experimento que produza uma comparação causal válida, operacionalmente executável e capaz de detectar uma mudança relevante. Pré-especificar decisões essenciais antes da exposição e analisar conforme a unidade de randomização.

Usar `analisar-causalidade` para estimandos e validade causal, `formular-testes-de-hipotese` para inferência e `orientar-analise-estatistica` para integrar o estudo.

## Formular a decisão

Definir:

- decisão que o experimento apoiará;
- intervenção e controle;
- população elegível;
- unidade de randomização, exposição e análise;
- estimando principal;
- janela de exposição e maturação do desfecho;
- efeito mínimo relevante;
- critérios de sucesso, segurança e rollout.

Não iniciar um teste apenas para “ver se muda alguma coisa”. Relacionar cada métrica a uma hipótese e decisão.

## Escolher o desenho

Consultar [desenhos-experimentais.md](references/desenhos-experimentais.md).

Considerar:

- A/B ou A/B/n;
- randomização individual;
- cluster randomization;
- estratificação, blocking ou matched pairs;
- fatorial completo ou fracionário;
- crossover;
- switchback;
- stepped-wedge;
- multi-armed bandit quando o objetivo de aprendizado e regret justificar;
- desenho sequencial pré-especificado.

Escolher a unidade de randomização para reduzir interferência e contaminação, sem ignorar perda de poder por clusterização.

## Definir métricas

Organizar:

- uma métrica primária;
- métricas secundárias;
- guardrails;
- métricas de qualidade da exposição;
- métricas de longo prazo;
- métricas exploratórias.

Definir numerador, denominador, janela, população, tratamento de extremos, atraso e fonte. Congelar a versão lógica antes do teste.

Não trocar métrica primária após observar resultados. Não usar métricas intermediárias como substitutas sem evidência de relação com o desfecho relevante.

## Definir o estimando e a análise

Priorizar intenção de tratar para efeito da oferta ou atribuição. Definir, quando necessário:

- per-protocol;
- treatment-on-the-treated;
- complier average causal effect;
- efeitos por cluster;
- efeitos de interação;
- heterogeneidade pré-especificada.

Não excluir não aderentes do ITT. Usar instrumentação da atribuição ou métodos causais apropriados quando estimar efeito da adesão.

## Dimensionar

Consultar [poder-amostra-e-duracao.md](references/poder-amostra-e-duracao.md).

Definir:

- baseline;
- MDE na escala original;
- variabilidade;
- alfa e poder;
- alocação;
- lados do teste;
- efeito de desenho;
- correlação pré-pós;
- perdas e não adesão;
- multiplicidade;
- duração mínima para cobrir ciclos relevantes.

Usar simulação quando houver clusters, métricas de razão, heavy tails, regras sequenciais, interferência ou desenho complexo.

Não escolher MDE apenas para caber na amostra disponível. Relatar o menor efeito detectável com os recursos reais e avaliar sua utilidade.

## Planejar randomização

Gerar atribuição reproduzível e auditável. Considerar:

- estratos pré-tratamento;
- balanceamento por tamanho;
- randomização em blocos;
- seed e versão;
- momento de entrada;
- persistência da variante;
- prevenção de re-randomização;
- regras para novas unidades.

Ocultar atribuição quando possível. Não rebalancear manualmente depois de observar desfechos.

## Preparar a instrumentação

Antes do início, validar:

- elegibilidade;
- exposição real;
- logging;
- timestamps;
- identificadores;
- persistência da variante;
- unidade de análise;
- duplicidades;
- atraso do desfecho;
- eventos de contaminação;
- funcionamento dos guardrails.

Executar A/A quando a infraestrutura, métrica ou randomização tiver risco relevante. Usar teste de qualidade de dados, não como ritual obrigatório.

## Monitorar sem inflar erro

Definir previamente:

- duração mínima;
- análises intermediárias;
- regra de parada por eficácia, futilidade ou segurança;
- alpha spending ou método sequencial;
- responsáveis;
- situações de interrupção operacional.

Não interromper por significância nominal repetidamente observada. Guardrails críticos podem justificar parada de segurança mesmo fora da hipótese primária, com documentação.

## Verificar integridade

Consultar [execucao-e-analise.md](references/execucao-e-analise.md).

Checar:

- sample ratio mismatch;
- equilíbrio de covariáveis pré-tratamento;
- exposição e contaminação;
- attrition diferencial;
- cobertura e atraso;
- duplicidades;
- sazonalidade e eventos;
- integridade dos clusters;
- novelty e carryover.

Investigar SRM antes de analisar efeitos. Não “corrigir” SRM apenas reponderando sem entender a causa.

## Analisar

Usar método compatível com randomização e estimando:

- diferença de médias ou proporções;
- regressão com ajuste pré-tratamento;
- CUPED ou ANCOVA;
- erros clusterizados;
- randomization inference;
- modelos mistos ou GEE;
- análise sequencial pré-planejada;
- contraste fatorial;
- modelos para métricas de razão.

Aplicar o mesmo conjunto de regras a grupos. Reportar efeitos absolutos, relativos, intervalos e tamanho amostral.

## Tratar múltiplos testes

Controlar a família primária de hipóteses. Usar Holm, Bonferroni, FDR, gatekeeping ou contrastes planejados conforme custo dos erros.

Rotular subgrupos e métricas pós-hoc como exploratórios. Não declarar personalização com base em uma interação não testada ou em significância separada dentro de grupos.

## Decidir

Separar:

- evidência estatística;
- magnitude prática;
- riscos nos guardrails;
- custo e viabilidade;
- heterogeneidade;
- incerteza residual;
- efeitos de longo prazo.

Permitir decisões como: lançar, não lançar, ampliar gradualmente, repetir, redesenhar ou coletar mais dados. Não exigir significância como única regra quando a decisão puder ser formulada por valor esperado e risco.

## Implementar

Priorizar:

- SQL para elegibilidade, exposição, métricas e coortes;
- Pandas, Polars ou PySpark para preparação;
- NumPy, SciPy e Statsmodels para dimensionamento e análise;
- Scikit-learn para covariate adjustment quando pré-especificado;
- simulação em Python para desenhos complexos;
- bibliotecas sequenciais ou causais auditáveis.

Recorrer a R somente quando o desenho ou estimador não tiver solução viável e confiável em Python.

## Entregar em quatro camadas

Apresentar:

1. fundamento acadêmico do desenho, estimando, poder e validade;
2. procedimento técnico de randomização, instrumentação, análise e monitoramento;
3. interpretação prática da decisão, ganho e riscos;
4. código documentado com objetivo, entradas, processamento, saída esperada e interpretação.

Encerrar com:

- protocolo do experimento;
- hipótese e estimando;
- desenho e randomização;
- métricas e guardrails;
- amostra, MDE e duração;
- plano de análise e parada;
- checagens de integridade;
- regra de decisão e plano de rollout.
