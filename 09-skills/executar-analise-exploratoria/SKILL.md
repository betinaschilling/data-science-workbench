---
name: executar-analise-exploratoria
description: Executar análise exploratória de dados completa e orientada por perguntas, combinando estatística descritiva, visualizações, segmentações, relações bivariadas e multivariadas, padrões temporais, heterogeneidade e geração de hipóteses. Usar para compreender uma base, investigar distribuições e associações, comparar grupos, descobrir padrões, preparar modelagem ou produzir uma leitura inicial de negócio. Separar explicitamente descoberta exploratória de inferência confirmatória, evitar causalidade indevida e registrar hipóteses para validação posterior; priorizar Python, usar SQL na preparação e recorrer a R somente quando não houver solução viável em Python.
---

# Executar análise exploratória

## Objetivo

Compreender a estrutura empírica dos dados e transformar padrões observados em perguntas melhores, hipóteses testáveis e decisões sobre as próximas análises. Não converter descobertas produzidas no mesmo conjunto de dados em confirmação independente.

Usar `auditar-dados-estatisticos` antes ou durante a exploração quando a qualidade dos dados ainda não estiver estabelecida. Usar `orientar-analise-estatistica` quando a exploração fizer parte de um estudo maior.

## Definir o foco

Registrar:

- pergunta inicial e contexto de decisão;
- unidade de análise, população, período e segmentos;
- papéis das variáveis: identificador, alvo, exposição, covariável, tempo, grupo ou peso;
- granularidade e dependências conhecidas;
- descobertas esperadas e descobertas abertas;
- restrições de privacidade, representatividade e interpretação.

Evitar produzir todas as tabelas e gráficos possíveis. Priorizar explorações que possam mudar a compreensão do fenômeno, o desenho metodológico ou a decisão.

## Preparar sem distorcer

Confirmar esquema, chaves, duplicidades, cobertura, ausências, unidades e definições. Manter rastreabilidade entre dados brutos e transformados.

Não:

- excluir outliers silenciosamente;
- preencher ausências antes de compreender seu padrão;
- transformar variáveis apenas para produzir gráficos mais “bonitos”;
- misturar granularidades em correlações;
- usar agregações que criem paradoxo de Simpson sem examinar grupos;
- tratar zero como ausência ou ausência como zero sem regra confirmada.

## Explorar em camadas

### 1. Estrutura da amostra

Descrever:

- número de observações, entidades, períodos e grupos;
- cobertura e balanceamento;
- granularidade efetiva;
- frequência de categorias;
- ausências e filtros aplicados;
- diferenças entre população observada e pretendida.

### 2. Distribuições univariadas

Para variáveis numéricas, avaliar posição, dispersão, quantis, assimetria, caudas, multimodalidade, zeros e limites. Para categorias, avaliar frequência, cardinalidade, raridade e categorias ausentes.

Escolher medidas robustas quando distribuições forem assimétricas ou contaminadas. Não resumir toda variável numérica apenas por média e desvio-padrão.

### 3. Relações bivariadas

Escolher técnica segundo os tipos de variáveis:

- numérica × numérica: dispersão, curvas suaves, correlações e relações não lineares;
- numérica × categórica: distribuições, intervalos, efeitos padronizados e heterogeneidade;
- categórica × categórica: contingência, proporções condicionais e resíduos;
- variável × tempo: evolução, sazonalidade, eventos e mudanças;
- variável × espaço ou hierarquia: mapas ou comparações somente quando a localização e agregação forem válidas.

Consultar [relacoes-e-medidas.md](references/relacoes-e-medidas.md).

### 4. Estrutura multivariada

Investigar:

- correlações parciais e condicionais;
- redundância e multicolinearidade;
- interações e não linearidades;
- subgrupos e heterogeneidade;
- projeções de baixa dimensão quando úteis;
- observações influentes e regiões pouco cobertas do espaço de dados.

Não interpretar clusters, componentes ou embeddings como entidades naturais sem estabilidade, validade externa e significado substantivo.

### 5. Segmentos e decomposições

Comparar resultados globais e condicionais por grupos relevantes. Verificar:

- composição dos segmentos;
- tamanhos amostrais e incerteza;
- diferenças de escala e exposição;
- efeitos de mix;
- reversões de associação;
- concentração do resultado em poucas unidades;
- estabilidade entre períodos.

Padronizar denominadores quando totais refletirem apenas diferenças de tamanho, como número de lojas, clientes ou dias operados. Manter também os totais quando forem relevantes à decisão.

### 6. Estrutura temporal

Quando houver tempo, preservar sua ordem. Examinar cobertura, tendência, sazonalidade, calendário, mudanças de regime e autocorrelação antes de calcular associações.

Usar `analisar-series-temporais` para diagnóstico temporal aprofundado, previsão ou relações defasadas. Não usar correlação entre séries com tendência e sazonalidade compartilhadas como evidência de relação substantiva.

## Escolher visualizações

Escolher o menor conjunto de gráficos que responda às perguntas. Usar títulos declarativos, unidades, denominadores, período, tamanho amostral e fonte quando aplicável.

Consultar [visualizacoes.md](references/visualizacoes.md) para mapear perguntas a gráficos.

Evitar:

- eixo truncado que exagere diferenças sem aviso;
- dupla escala sem justificativa;
- pizza com muitas categorias;
- heatmap ilegível;
- sobreposição sem transparência ou amostragem;
- paleta que codifique ordem inexistente;
- suavização que esconda observações ou incerteza;
- dashboards ornamentais sem pergunta analítica.

## Quantificar associações

Reportar magnitude, direção, forma, incerteza descritiva e tamanho da amostra. Usar Pearson, Spearman, Kendall, Cramér's V, informação mútua ou medidas robustas conforme escala e estrutura.

Não selecionar apenas a associação mais forte entre muitas tentativas. Registrar o universo de comparações e tratar padrões descobertos como hipóteses.

Quando houver dependência por grupo, tempo, repetição ou desenho amostral, não usar intervalos ou testes que presumam observações independentes.

## Gerar e priorizar hipóteses

Converter cada descoberta relevante no formato:

| Elemento | Registro |
|---|---|
| Padrão observado | O que foi encontrado e em qual recorte |
| Explicações candidatas | Mecanismos, confundimento, artefato ou acaso |
| Evidência atual | Gráfico, métrica e cobertura |
| Fragilidade | Ausência, seleção, múltiplas buscas ou baixa amostra |
| Hipótese testável | Formulação que possa ser refutada |
| Próxima análise | Teste, modelo, novo dado ou experimento |
| Valor potencial | Decisão que a validação poderia apoiar |

Priorizar hipóteses por relevância, plausibilidade, risco de artefato e viabilidade de validação.

Consultar [exploracao-e-confirmacao.md](references/exploracao-e-confirmacao.md).

## Implementar

Priorizar:

- SQL para amostragem, agregações, denominadores e tabelas de apoio;
- Pandas, Polars ou PySpark para preparação e sumarização;
- NumPy e SciPy para medidas;
- Statsmodels para suavização e análises estatísticas auxiliares;
- Matplotlib, Seaborn, Plotly ou Altair para visualização;
- Scikit-learn somente quando técnicas multivariadas forem realmente úteis.

Usar amostragem reprodutível para visualização de bases grandes, mantendo cálculos agregados na base completa quando possível. Declarar qualquer amostragem.

## Entregar em quatro camadas

Apresentar:

1. fundamento acadêmico sobre distribuição, associação, heterogeneidade e limites exploratórios;
2. procedimento técnico com métricas, gráficos, segmentações e transformações;
3. interpretação prática sem extrapolar as evidências;
4. código documentado com objetivo, entradas, processamento, saída esperada e interpretação.

Encerrar com:

- panorama da base e de sua cobertura;
- cinco a dez achados priorizados, ou menos quando não houver evidência suficiente;
- hipóteses alternativas para cada achado importante;
- riscos de qualidade ou interpretação;
- hipóteses que merecem validação;
- métodos confirmatórios recomendados;
- perguntas que os dados atuais não conseguem responder.
