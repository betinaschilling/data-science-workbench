---
name: analisar-dados-multivariados
description: Analisar estruturas com múltiplas variáveis e desfechos por meio de redução de dimensionalidade, modelos latentes, ordenação, classificação discriminante e segmentação. Usar para PCA, análise fatorial exploratória ou confirmatória, correspondência, PLS, CCA, MANOVA, LDA/QDA, clustering, mistura gaussiana, métodos de distância, embeddings, visualização multivariada e construção de segmentos. Escolher escala, distância e método conforme o tipo dos dados; avaliar número de dimensões ou clusters, estabilidade, incerteza, validade externa e utilidade. Não tratar componentes, embeddings ou clusters como estruturas naturais sem validação. Priorizar Python, usar SQL na preparação e recorrer a R somente quando não houver solução viável em Python.
---

# Analisar dados multivariados

## Objetivo

Investigar como variáveis se organizam conjuntamente, resumir informação redundante, identificar dimensões latentes ou construir segmentações úteis. Distinguir visualização, descrição, inferência e decisão; exigir estabilidade e validade externa antes de nomear estruturas.

Usar `auditar-dados-estatisticos` para qualidade e `orientar-analise-estatistica` quando a análise fizer parte de um estudo maior.

## Definir o objetivo

Classificar a tarefa:

- resumir variáveis correlacionadas;
- descobrir ou confirmar construtos latentes;
- representar proximidade;
- segmentar observações;
- comparar vetores de desfechos;
- discriminar grupos conhecidos;
- relacionar dois blocos de variáveis;
- criar features para modelo posterior.

Registrar unidade de análise, tipos de variável, população, tamanho amostral, grupos, tempo, pesos e uso esperado da representação ou segmentação.

## Preparar os dados

Verificar:

- escalas e unidades;
- variáveis contínuas, ordinais, nominais, binárias e composicionais;
- assimetria, caudas e outliers;
- ausências;
- redundância e near-zero variance;
- dependência por grupo ou tempo;
- amostra suficiente;
- variáveis derivadas ou duplicadas.

Padronizar quando diferenças de unidade não representarem importância substantiva. Não padronizar mecanicamente dados composicionais, binários ou distâncias com semântica própria.

Aplicar imputação e transformação dentro da validação quando a representação alimentar tarefa preditiva.

## Escolher geometria e medida

Definir distância, similaridade ou matriz de associação conforme os dados:

- Euclidiana para geometria contínua compatível;
- Manhattan para maior robustez e alta dimensão;
- Mahalanobis com covariância estável;
- Gower para dados mistos;
- Jaccard para presença/ausência;
- cosine para direção;
- DTW para forma temporal;
- Aitchison para composições;
- correlações Pearson, Spearman, policórica ou tetra-córica conforme escala.

Não usar Euclidiana por padrão em variáveis mistas ou altamente correlacionadas.

## Reduzir dimensionalidade

Consultar [reducao-e-fatores.md](references/reducao-e-fatores.md).

Considerar:

- PCA;
- sparse ou robust PCA;
- análise fatorial exploratória;
- análise fatorial confirmatória;
- correspondência simples ou múltipla;
- PLS;
- canonical correlation;
- multidimensional scaling;
- UMAP ou t-SNE para visualização.

Escolher número de componentes ou fatores usando scree, parallel analysis, variância explicada, reconstrução, interpretabilidade e estabilidade.

Não interpretar t-SNE ou UMAP como preservação fiel de distâncias globais. Não usar embeddings visuais como prova de clusters.

## Analisar fatores

Para análise fatorial:

- justificar matriz de correlação;
- avaliar adequação;
- escolher método de extração;
- permitir correlação entre fatores quando plausível;
- comparar rotações;
- interpretar cargas, comunalidades e cross-loadings;
- avaliar confiabilidade sem depender apenas de alfa;
- validar estrutura em nova amostra ou CFA.

Não nomear fator apenas pelas variáveis de maior carga sem teoria e coerência.

## Segmentar

Consultar [clusterizacao.md](references/clusterizacao.md).

Considerar:

- k-means ou k-medoids;
- hierárquico;
- DBSCAN/HDBSCAN;
- Gaussian mixture;
- spectral clustering;
- latent class/profile;
- co-clustering;
- clustering temporal.

Escolher método pela forma esperada, ruído, densidade, escala, tamanho e necessidade de probabilidades.

Não escolher número de clusters apenas por silhouette. Avaliar estabilidade, separação, tamanhos, interpretação, ação e generalização.

## Comparar grupos multivariados

Usar MANOVA ou modelos multivariados quando a pergunta tratar o vetor de desfechos e os pressupostos forem adequados. Avaliar:

- independência;
- matriz de covariância;
- outliers multivariados;
- tamanho por grupo;
- testes globais;
- contrastes e análises posteriores com multiplicidade.

Não usar MANOVA apenas para evitar vários testes sem uma hipótese multivariada substantiva.

## Discriminar grupos conhecidos

Usar LDA, QDA, regressão multinomial ou métodos preditivos conforme objetivo e pressupostos. Separar análise discriminante de clustering: uma usa rótulos, a outra não.

Validar fora da amostra. Não interpretar boa separação no mesmo espaço usado para construir a projeção como generalização.

## Validar estruturas

Consultar [estabilidade-e-validade.md](references/estabilidade-e-validade.md).

Avaliar:

- bootstrap e subsampling;
- sensibilidade a escala, distância e algoritmo;
- estabilidade de cargas, componentes e memberships;
- concordância entre soluções;
- validação temporal ou externa;
- capacidade de reconstrução;
- validade convergente e discriminante;
- relação com resultados não usados na construção;
- utilidade operacional.

Se a estrutura desaparecer com pequenas perturbações, reportar instabilidade em vez de forçar rótulos.

## Interpretar e nomear

Descrever componentes por cargas e contribuição; clusters por distribuições e contrastes, não apenas médias. Mostrar heterogeneidade interna e sobreposição.

Validar nomes com conhecimento substantivo. Não usar rótulos normativos ou estigmatizantes. Distinguir segmento estatístico, persona narrativa e política de decisão.

## Implementar

Priorizar:

- SQL para unidade de análise e agregações;
- Pandas, Polars ou PySpark para preparação;
- NumPy e SciPy para álgebra e distâncias;
- Scikit-learn para PCA, clustering, mixtures, discriminantes e validação;
- FactorAnalyzer, semopy ou bibliotecas confiáveis para fatores/SEM;
- prince para correspondência;
- umap-learn e hdbscan quando adequados;
- Statsmodels para MANOVA e testes auxiliares.

Recorrer a R somente quando o método necessário não tiver implementação viável e confiável em Python.

## Entregar em quatro camadas

Apresentar:

1. fundamento acadêmico da geometria, método, pressupostos e finalidade;
2. procedimento técnico de preparação, ajuste, seleção e validação;
3. interpretação prática da estrutura e seu uso;
4. código documentado com objetivo, entradas, processamento, saída esperada e interpretação.

Encerrar com:

- objetivo multivariado;
- variáveis, escala e distância;
- método e hiperparâmetros;
- número de dimensões ou clusters;
- estabilidade e validade externa;
- interpretação;
- limitações;
- recomendação de uso ou rejeição da estrutura.
