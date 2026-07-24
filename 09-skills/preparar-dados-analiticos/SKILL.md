---
name: preparar-dados-analiticos
description: Construir bases analíticas corretas, rastreáveis e livres de vazamento a partir de fontes relacionais, arquivos ou camadas de dados. Usar para definir população e unidade de análise, integrar tabelas, validar joins e cardinalidade, deduplicar, filtrar, agregar, alinhar tempo, tratar tipos e ausências, criar snapshots e separar dados brutos de derivados antes de estatística ou machine learning. Priorizar SQL para extração e transformação estrutural, Python para preparação analítica e R somente quando não houver alternativa viável.
---

# Preparar dados analíticos

## Objetivo

Transformar fontes em uma tabela analítica cuja linha, população, tempo e significado sejam explícitos. Preservar dados brutos e tornar cada transformação reproduzível.

Usar `auditar-dados-estatisticos` para diagnosticar a qualidade das fontes. Preparação não corrige silenciosamente problemas de coleta.

## Definir o contrato da base

Registrar:

- população e critérios de elegibilidade;
- unidade de análise e chave candidata;
- granularidade temporal;
- período de observação e horizonte;
- target, exposições e features;
- momento de disponibilidade de cada campo;
- segmentações, pesos e hierarquias;
- número esperado de linhas e unicidade.

Não iniciar joins antes de definir o que cada linha representa.

## Inventariar fontes

Para cada fonte, documentar:

- responsável e camada;
- chave e cardinalidade;
- período e cobertura;
- timezone, frequência e latência;
- significado de ausências e zeros;
- versão, atualização e mudanças de schema;
- campos sensíveis e restrições de uso.

Preservar identificadores necessários à rastreabilidade sem expor dados sensíveis nas saídas.

## Construir em SQL

Priorizar SQL para:

- seleção de população;
- joins;
- filtros;
- deduplicação determinística;
- agregações;
- janelas;
- snapshots point-in-time;
- controles de integridade;
- materialização intermediária quando necessária.

Antes e depois de cada join, validar contagem de linhas, chaves distintas, duplicidade e soma de métricas aditivas. Não usar `DISTINCT` para ocultar erro de cardinalidade.

## Alinhar tempo

Definir:

- data do evento;
- data de processamento;
- data de disponibilidade;
- data de referência;
- timezone;
- calendário e frequência.

Garantir que features representem apenas informação disponível no instante da decisão. Para séries, construir grade temporal por unidade e distinguir ausência de evento, ausência de medição e ausência de cobertura.

## Tratar qualidade

Não imputar, remover outlier ou excluir população sem aprovação quando isso puder mudar inferência ou decisão.

Para cada tratamento:

- descrever mecanismo;
- preservar indicador de ausência quando relevante;
- ajustar transformações dentro da validação;
- comparar cenário tratado e não tratado;
- registrar linhas afetadas;
- verificar impacto por grupo e tempo.

Zeros não são automaticamente ausências. Outliers podem representar evento real, erro ou mudança de regime.

## Preparar em Python

Usar Pandas, Polars ou PySpark para:

- transformações analíticas;
- features dependentes do desenho;
- codificação e escalonamento dentro de pipelines;
- alinhamento de painéis;
- validações programáticas;
- amostras de desenvolvimento;
- objetos de treino, validação e teste.

Evitar mutações encadeadas e notebooks com estado implícito. Preferir funções com entradas, saídas e contratos claros.

## Separar conjuntos

Definir o particionamento antes de aprender imputadores, encoders, escalas ou seleção de atributos. Respeitar:

- ordem temporal;
- grupos e indivíduos;
- hierarquia;
- pareamento;
- distribuição operacional;
- conjunto de teste intocado.

Não embaralhar séries temporais nem permitir que a mesma entidade atravesse conjuntos quando isso superestimar generalização.

## Validar a saída

Executar controles:

- schema e tipos;
- chave única;
- domínio e faixa;
- completude;
- cobertura por grupo e tempo;
- reconciliação com fonte;
- invariantes de negócio;
- disponibilidade point-in-time;
- ausência de leakage;
- estabilidade de volume.

Falhar explicitamente em violações críticas. Não apenas imprimir alertas e continuar.

## Entregar

Apresentar:

1. contrato da base;
2. diagrama ou descrição de fontes e joins;
3. transformações e justificativas;
4. controles antes/depois;
5. decisões humanas;
6. riscos residuais;
7. SQL e Python documentados com objetivo, entradas, processamento, saída esperada e interpretação.

Não sobrescrever fontes brutas. Salvar derivados somente quando solicitado e com versão ou linhagem identificável.
