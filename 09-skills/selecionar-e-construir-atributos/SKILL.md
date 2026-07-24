---
name: selecionar-e-construir-atributos
description: Projetar, construir, avaliar e selecionar atributos para modelos estatísticos e de machine learning sem vazamento. Usar para feature engineering, lags, janelas, agregações, interações, transformações, encoding, seleção por regularização, mutual information, permutation, Boruta, estabilidade e ablation. Exigir disponibilidade point-in-time, significado substantivo, ajuste dentro da validação e utilidade fora da amostra. Priorizar SQL na construção estrutural e Python na seleção; não selecionar variáveis por SHAP ou correlação isoladamente.
---

# Selecionar e construir atributos

## Definir o contrato

Para cada atributo registrar significado, fonte, unidade, granularidade, instante de disponibilidade, transformação, risco de leakage e comportamento esperado.

Construir a partir do mecanismo e da decisão, não apenas de combinações automáticas.

## Construir

Considerar:

- transformações de escala e distribuição;
- interações e não linearidades;
- agregações históricas point-in-time;
- lags, rolling e expanding windows;
- frequência, recência e duração;
- calendários e eventos;
- encoding de categorias;
- representação de texto, imagem ou séries quando necessário.

Em tempo, usar somente passado disponível e deslocar janelas corretamente. Em grupos, evitar estatísticas calculadas com observações de validação ou teste.

## Controlar redundância

Verificar near-zero variance, duplicidade, correlação, multicolinearidade, cardinalidade, sparsidade e proxies do target. Não remover automaticamente variáveis correlacionadas quando efeitos conjuntos ou interpretação forem relevantes.

## Selecionar

Combinar conforme objetivo:

- conhecimento substantivo;
- filtros univariados dentro da validação;
- regularização;
- recursive feature elimination;
- permutation importance;
- mutual information;
- Boruta;
- seleção sequencial;
- estabilidade de seleção;
- ablation por grupos coerentes.

Não usar o conjunto de teste na seleção. Importância de árvore e SHAP não são critérios suficientes por favorecerem certas estruturas e refletirem o modelo ajustado.

## Validar

Avaliar:

- ganho incremental fora da amostra;
- estabilidade por folds, tempo e segmentos;
- sensibilidade a drift;
- custo de obtenção;
- latência;
- robustez a ausência;
- interpretabilidade;
- redundância com outras features;
- risco ético e de proxy.

Preferir conjunto menor quando o ganho adicional for instável ou irrelevante.

## Integrar ao pipeline

Aprender imputação, encoding, escala, redução e seleção somente no treino. Usar pipelines reproduzíveis, nomes rastreáveis e testes point-in-time.

Priorizar SQL para joins, agregações e snapshots; Python com Scikit-learn, Pandas, Polars, PySpark e bibliotecas confiáveis para transformações e seleção. R somente sem alternativa viável.

## Entregar

Apresentar catálogo de features, lógica temporal, métodos de seleção, desenho de validação, resultados de ablation, estabilidade, features rejeitadas, riscos e código documentado.

Não concluir que uma feature explica ou causa o target apenas porque melhora previsão.
