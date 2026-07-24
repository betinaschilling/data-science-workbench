---
name: modelar-aprendizado-nao-supervisionado
description: Desenvolver e validar soluções de machine learning sem target para segmentação operacional, descoberta de grupos, representação, similaridade, detecção de anomalias e novidade. Usar quando o objetivo for produzir memberships, scores, embeddings ou regras reutilizáveis para novas observações; escolher distância, representação, algoritmo e hiperparâmetros, avaliar estabilidade, generalização, validade externa e utilidade. Não usar para análise fatorial, MANOVA ou investigação multivariada clássica, que pertencem a analisar-dados-multivariados. Priorizar Python e SQL.
---

# Modelar aprendizado não supervisionado

## Fronteira

Usar esta skill quando o produto final precisar operar sobre dados novos: atribuir segmento, recuperar similares, gerar embedding ou sinalizar anomalia.

Usar `analisar-dados-multivariados` para compreender estrutura conjunta, fatores, componentes, geometria e inferência multivariada. Clustering exploratório pode começar lá; migra para esta skill quando virar solução reutilizável.

## Formular o produto

Definir:

- unidade e população;
- saída: cluster, probabilidade, score, embedding ou vizinhança;
- frequência de atualização;
- ação associada;
- restrições de tamanho, estabilidade, latência e interpretabilidade;
- critério externo de utilidade.

Não presumir que os dados contêm grupos naturais.

## Preparar representação

Escolher variáveis, escala, encoding, distância e redução conforme semântica. Tratar ausência e outliers dentro do pipeline. Evitar alta dimensionalidade irrelevante e features dominadas por volume.

Para séries, distinguir nível, tendência, sazonalidade, forma e distância temporal. Para dados mistos, não usar Euclidiana mecanicamente.

## Escolher tarefa e método

- segmentação: k-means, k-medoids, hierárquico, mixtures, HDBSCAN;
- anomalia: Isolation Forest, LOF, One-Class SVM, métodos robustos;
- representação: PCA preditiva, NMF, autoencoders, embeddings;
- similaridade: nearest neighbors, cosine, métricas aprendidas;
- novidade: modelos treinados em comportamento normal.

Usar redes apenas quando escala, dados e ganho justificarem.

## Selecionar solução

Não escolher número de clusters apenas por elbow ou silhouette. Combinar:

- estabilidade por bootstrap ou subsampling;
- sensibilidade a escala, features e algoritmo;
- separação e sobreposição;
- tamanhos mínimos;
- coerência temporal;
- capacidade de atribuir novos casos;
- validade externa;
- utilidade operacional.

Para anomalias, validar com rótulos parciais, revisão humana, dados sintéticos plausíveis e custo de alertas.

## Testar generalização

Separar períodos ou amostras quando possível. Ajustar preprocessamento somente no treino e avaliar:

- drift de representação;
- estabilidade dos perfis;
- concordância de memberships;
- taxa de novos casos;
- degradação de utilidade;
- sensibilidade a perturbações.

Uma visualização bonita não valida a solução.

## Interpretar

Descrever segmentos por distribuições, contrastes e heterogeneidade interna. Nomear somente após validação substantiva. Não transformar cluster em persona, causa ou política sem evidência adicional.

Para embeddings, explicitar o que a distância preserva e o que não preserva. Para anomalias, distinguir raro, erro, novidade e evento relevante.

## Entregar

Apresentar objetivo operacional, representação, método, seleção, estabilidade, validade externa, regra para novos casos, análise de falhas, limitações e código Python/SQL documentado.

Recomendar uso somente se a estrutura permanecer útil fora da amostra e houver ação proporcional ao grau de incerteza.
