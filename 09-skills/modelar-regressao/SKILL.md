---
name: modelar-regressao
description: Escolher, ajustar, diagnosticar, validar e interpretar modelos de regressão para desfechos contínuos, binários, ordinais, nominais, contagens, taxas, proporções, quantis, duração e dados agrupados ou repetidos. Usar para regressão linear e generalizada, modelos robustos, quantílicos, mistos, GEE, sobrevivência, regularização, splines, interações, efeitos marginais, inferência ou previsão baseada em regressão. Distinguir finalidade associativa, preditiva e causal; verificar especificação, resíduos, influência, multicolinearidade, calibração e estabilidade. Priorizar Python, usar SQL na preparação e recorrer a R somente quando não houver solução viável em Python.
---

# Modelar regressão

## Objetivo

Construir um modelo coerente com o desfecho, o desenho dos dados e a finalidade da análise. Estimar relações e incertezas, diagnosticar falhas de especificação e interpretar resultados na escala substantiva sem converter coeficientes associativos em efeitos causais.

Usar `orientar-analise-estatistica` quando o modelo integrar um estudo maior, `formular-testes-de-hipotese` para contrastes inferenciais e a futura especialidade causal quando o objetivo for efeito de intervenção.

## Definir a finalidade

Classificar o objetivo:

- descrição de relações condicionais;
- inferência sobre parâmetros ou contrastes;
- ajuste de confundidores em desenho causal identificado;
- previsão fora da amostra;
- estimação de heterogeneidade;
- explicação de variação;
- geração de cenários.

Registrar população, unidade de análise, desfecho, preditores, estimando, horizonte, dependências, amostragem e decisão. Não usar o mesmo critério de seleção para todas as finalidades.

## Identificar a estrutura do desfecho

Escolher família e link segundo o processo gerador:

- contínuo sem restrição;
- contínuo positivo ou assimétrico;
- binário;
- ordinal;
- nominal;
- contagem;
- taxa com exposição;
- proporção ou fração;
- quantil;
- tempo até evento;
- semicontínuo, inflado em zero ou truncado.

Consultar [familias-e-links.md](references/familias-e-links.md).

Não transformar um desfecho apenas para forçar OLS quando uma família adequada preservar melhor a interpretação.

## Respeitar o desenho

Identificar:

- observações independentes;
- medidas repetidas;
- clusters e hierarquias;
- efeitos fixos e aleatórios;
- autocorrelação temporal;
- dependência espacial;
- pesos amostrais;
- censura, truncamento e exposição.

Usar erros-padrão robustos, clusterizados, GEE, modelos mistos, painéis ou estruturas temporais conforme a fonte de dependência. Erros-padrão robustos não corrigem forma funcional errada, confundimento ou endogeneidade.

## Especificar o modelo

Definir com justificativa:

- termos principais;
- variáveis de ajuste;
- interações;
- não linearidades;
- transformações;
- offsets e exposições;
- efeitos de grupo;
- regularização;
- restrições ou monotonicidade, quando substantivamente necessárias.

Usar splines, polinômios fracionários ou transformações para relações não lineares. Evitar categorizar variáveis contínuas sem motivo operacional forte; isso reduz informação e pode criar cortes arbitrários.

Aplicar princípio de hierarquia: se incluir interação ou potência, manter os termos componentes necessários à interpretação.

## Separar seleção de variáveis por finalidade

Para inferência:

- selecionar covariáveis por teoria, desenho, DAG ou pré-especificação;
- evitar stepwise baseado apenas em valor-p;
- preservar variáveis necessárias ao estimando;
- contabilizar seleção quando ela afetar a inferência.

Para previsão:

- ajustar regularização e hiperparâmetros dentro da validação;
- avaliar generalização e calibração;
- aceitar variáveis úteis mesmo sem interpretação causal;
- prevenir leakage.

Para causalidade:

- não ajustar mediadores, colisores ou variáveis pós-tratamento sem justificar o estimando;
- não interpretar coeficiente como efeito causal sem identificação.

## Ajustar e comparar

Começar com baseline interpretável. Comparar modelos usando critérios compatíveis:

- likelihood, deviance, AIC ou BIC para objetivos e famílias apropriados;
- validação fora da amostra para previsão;
- testes de razão de verossimilhança para modelos aninhados regulares;
- contrastes e intervalos para inferência;
- calibração e decisão para risco;
- análise de sensibilidade para especificação.

Não selecionar por R² isoladamente. R² maior pode refletir complexidade, leakage ou variáveis irrelevantes à pergunta.

## Diagnosticar

Examinar conforme a família:

- forma funcional;
- resíduos e dependência;
- heterocedasticidade;
- overdispersion ou underdispersion;
- zero inflation;
- separação em logística;
- multicolinearidade e identificabilidade;
- leverage, influência e resíduos extremos;
- calibração;
- estabilidade entre amostras, grupos e períodos;
- convergência e singularidade em modelos mistos;
- proporcionalidade de hazards em sobrevivência.

Consultar [diagnosticos.md](references/diagnosticos.md).

Tratar testes diagnósticos como evidências complementares. Combinar gráficos, métricas, conhecimento do processo e sensibilidade.

## Quantificar incerteza

Escolher entre:

- erros-padrão model-based;
- erros robustos ou clusterizados;
- bootstrap na unidade independente;
- perfil de verossimilhança;
- intervalos preditivos;
- simulação de parâmetros;
- inferência pós-seleção, quando disponível e necessária.

Não usar bootstrap de linhas quando a unidade independente for cluster, pessoa ou bloco temporal.

## Interpretar na escala correta

Apresentar efeitos na escala original sempre que possível:

- mudança esperada no desfecho;
- diferença ou razão de riscos;
- odds ratio acompanhado de probabilidades ou efeitos marginais;
- razão de taxas;
- razão de hazards;
- diferença em quantis;
- contrastes preditos;
- efeitos condicionais em interações.

Consultar [interpretacao.md](references/interpretacao.md).

Não interpretar odds ratio como risco relativo. Não interpretar coeficiente de interação apenas pelo seu valor-p; mostrar efeitos condicionais e incerteza.

## Validar

Para previsão, separar treino, validação e teste de acordo com tempo, grupos e processo de implantação. Avaliar:

- erro e discriminação;
- calibração;
- estabilidade;
- desempenho por subgrupos;
- incerteza;
- utilidade para decisão.

Para inferência, verificar robustez a especificações plausíveis, observações influentes, formas funcionais, codificações, ausências e erros-padrão.

## Implementar

Priorizar:

- SQL para preparar unidade de análise, exposições, agregações e categorias;
- Pandas, Polars ou PySpark para organização;
- Statsmodels para OLS, GLM, GEE, modelos mistos disponíveis, quantílica e diagnósticos;
- Scikit-learn para pipelines, regularização e validação preditiva;
- Lifelines ou scikit-survival para sobrevivência;
- PyGAM, Patsy ou splines do ecossistema científico para não linearidade;
- NumPy, SciPy e Matplotlib/Seaborn para diagnóstico.

Recorrer a R somente quando a estrutura necessária não tiver implementação viável e confiável em Python, explicando a limitação.

## Entregar em quatro camadas

Apresentar:

1. fundamento acadêmico da família, link, estimando e pressupostos;
2. procedimento técnico de especificação, ajuste, diagnóstico e validação;
3. interpretação prática de magnitudes, incerteza e decisão;
4. código documentado com objetivo, entradas, processamento, saída esperada e interpretação.

Encerrar com:

- finalidade e população;
- equação ou especificação;
- família e link;
- estimativas e intervalos;
- diagnósticos;
- validação e comparação;
- interpretação na escala substantiva;
- limitações, sensibilidade e conclusões não permitidas.
