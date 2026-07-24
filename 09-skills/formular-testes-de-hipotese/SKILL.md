---
name: formular-testes-de-hipotese
description: Formular, selecionar, executar e interpretar testes de hipótese e procedimentos inferenciais para médias, medianas, proporções, distribuições, associações, variâncias, contagens, dados pareados, grupos independentes, medidas repetidas e desenhos complexos. Usar para comparar grupos ou períodos, avaliar diferenças e associações, calcular tamanho de efeito, intervalos, poder e tamanho amostral, controlar multiplicidade, testar equivalência ou não inferioridade e escolher entre métodos paramétricos, robustos, não paramétricos, permutacionais ou bootstrap. Definir primeiro o estimando, o desenho e a dependência; não escolher testes apenas por normalidade. Priorizar Python, usar SQL na preparação e recorrer a R somente quando não houver solução viável em Python.
---

# Formular testes de hipótese

## Objetivo

Transformar uma pergunta substantiva em uma hipótese estatística coerente com o desenho dos dados, estimar a magnitude e a incerteza do efeito e apoiar uma decisão sem reduzir a conclusão a “significativo” ou “não significativo”.

Usar `executar-analise-exploratoria` para hipóteses ainda em descoberta e `orientar-analise-estatistica` quando a inferência fizer parte de um estudo maior.

## Definir antes de testar

Registrar:

- população-alvo e unidade de análise;
- desfecho, exposição ou grupos;
- estimando: diferença, razão, associação, quantil ou outra quantidade;
- direção da hipótese e justificativa para teste unilateral ou bilateral;
- independência, pareamento, repetição, clusters, estratos e pesos;
- família de comparações;
- nível de significância e intervalo;
- menor efeito relevante, quando aplicável;
- regra de decisão e consequência prática.

Escrever hipóteses nula e alternativa na escala do estimando. Não usar “há diferença” sem definir entre quais grupos, em qual métrica e população.

## Verificar o desenho

Classificar as observações como:

- independentes;
- pareadas;
- repetidas na mesma unidade;
- agrupadas ou hierárquicas;
- ordenadas no tempo;
- provenientes de amostra complexa;
- censuradas ou truncadas.

Tratar dependência incorreta como erro de desenho, não como detalhe do teste. Quando houver tempo, grupos ou hierarquia relevantes, usar métodos que preservem essa estrutura.

## Escolher o procedimento

Selecionar o método pelo estimando, desenho, escala, tamanho da amostra, distribuição dos erros e robustez necessária.

Consultar [selecao-de-testes.md](references/selecao-de-testes.md).

Considerar:

- testes t de Welch ou pareado;
- ANOVA de Welch, modelos lineares ou contrastes planejados;
- qui-quadrado, Fisher e testes de proporções;
- Mann–Whitney, Wilcoxon, Kruskal–Wallis e Friedman;
- testes de permutação;
- bootstrap paramétrico ou não paramétrico;
- métodos robustos para médias aparadas, quantis ou variâncias;
- modelos de regressão para ajuste e desenhos mais complexos;
- procedimentos de equivalência e não inferioridade.

Preferir Welch ao t clássico de variâncias iguais quando não houver razão sólida para assumir homocedasticidade.

## Avaliar pressupostos

Verificar os pressupostos que sustentam a distribuição do estimador ou a validade da reamostragem:

- independência ou estrutura de dependência;
- mecanismo de amostragem;
- forma e variância dos resíduos relevantes;
- tamanho das células e aproximações assintóticas;
- intercambiabilidade em permutação;
- unidades corretas de reamostragem no bootstrap;
- ausência de seleção pós-hoc não registrada.

Não exigir normalidade marginal dos dados quando o teste depende da distribuição do estimador ou dos resíduos. Não escolher automaticamente entre t e Mann–Whitney com base em Shapiro–Wilk.

Se os pressupostos falharem, considerar estimador robusto, transformação interpretável, reamostragem adequada, modelo explícito ou mudança do estimando.

## Estimar antes de decidir

Reportar:

- estimativa pontual;
- intervalo de confiança compatível;
- tamanho de efeito na escala original;
- tamanho de efeito padronizado quando útil;
- valor-p como evidência contínua;
- tamanho da amostra efetiva;
- método, pressupostos e ajustes;
- relevância prática.

Consultar [efeitos-poder-e-amostra.md](references/efeitos-poder-e-amostra.md).

Não interpretar valor-p como probabilidade de a hipótese nula ser verdadeira. Não confundir significância com importância. Não interpretar falha em rejeitar como equivalência ou ausência de efeito.

## Controlar multiplicidade

Definir a família de hipóteses segundo a pergunta científica ou decisão, não apenas segundo conveniência computacional.

Considerar:

- Bonferroni ou Holm para controle de FWER;
- Hochberg quando seus pressupostos forem plausíveis;
- Benjamini–Hochberg ou Benjamini–Yekutieli para FDR;
- contrastes planejados;
- procedimentos hierárquicos ou gatekeeping;
- testes globais antes de comparações específicas quando coerente;
- intervalos simultâneos.

Consultar [multiplicidade-e-flexibilidade.md](references/multiplicidade-e-flexibilidade.md).

Registrar análises exploratórias, desfechos múltiplos, subgrupos, janelas e transformações tentadas. Correção de valor-p não resolve totalmente seleção pós-hoc não documentada.

## Planejar poder e tamanho amostral

Definir antes da coleta:

- efeito mínimo relevante;
- variabilidade ou taxa de referência;
- alfa, poder e número de lados;
- desenho, alocação e correlação intraclasse;
- perdas, não adesão e multiplicidade;
- análise e estimador pretendidos.

Usar simulação quando fórmulas fechadas não representarem o desenho. Não calcular poder pós-hoc substituindo o efeito observado; interpretar intervalos e compatibilidade dos efeitos.

## Tratar equivalência e não inferioridade

Usar equivalência quando a pergunta for se o efeito está inteiramente dentro de margens consideradas desprezíveis. Usar não inferioridade quando apenas uma direção for relevante.

Definir margens com justificativa substantiva antes de observar os resultados. Aplicar TOST ou procedimento compatível e verificar se todo o intervalo relevante fica dentro das margens.

Não declarar equivalência apenas porque `p > α`.

## Usar reamostragem corretamente

No bootstrap, reamostrar na unidade independente: indivíduos, pares, clusters ou blocos temporais. Escolher intervalo percentile, basic, BCa ou bootstrap-t conforme viés e estabilidade.

Na permutação, permutar apenas sob o grupo de transformações permitido pela hipótese nula e pelo desenho. Preservar pares, blocos, clusters e estratos.

Usar sementes e quantidade de replicações compatível com a precisão desejada.

## Implementar

Priorizar:

- SQL para preparar grupos, unidades, exposições e denominadores;
- Pandas, Polars ou PySpark para organização;
- NumPy e SciPy para testes e reamostragem;
- Statsmodels para proporções, poder, contrastes e modelos;
- Pingouin ou funções especializadas quando forem transparentes e validadas;
- Scikit-learn apenas para utilitários pertinentes;
- simulação em Python para desenhos complexos.

Recorrer a R somente quando um procedimento necessário não tiver implementação viável e confiável em Python; explicar a exceção.

## Entregar em quatro camadas

Apresentar:

1. fundamento acadêmico do estimando, hipótese, erro e método;
2. procedimento técnico com desenho, pressupostos, cálculos e ajustes;
3. interpretação prática da magnitude, incerteza e decisão;
4. código documentado com objetivo, entradas, processamento, saída esperada e interpretação.

Encerrar com:

- pergunta e estimando;
- hipóteses formalizadas;
- teste ou modelo escolhido e justificativa;
- estimativa, intervalo, tamanho de efeito e valor-p;
- multiplicidade e poder quando relevantes;
- diagnóstico dos pressupostos;
- conclusão permitida e conclusão não permitida;
- implicação prática e próxima análise.
