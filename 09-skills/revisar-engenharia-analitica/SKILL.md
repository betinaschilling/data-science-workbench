---
name: revisar-engenharia-analitica
description: Revisar de forma independente soluções de engenharia de dados e analytics engineering, incluindo SQL, modelos dimensionais, ETL/ELT, pipelines, DAGs, notebooks, Spark, Databricks, BigQuery, transformações, contratos, qualidade, testes, observabilidade, segurança e custos. Usar para peer review, auditoria pré-merge, avaliação de arquitetura, validação de tabelas, jobs e fluxos ou diagnóstico de riscos antes de produção; verificar correção, idempotência, granularidade, chaves, cardinalidade, particionamento, incrementalidade, reprocessamento, lineage, performance e operabilidade. Emitir parecer por severidade e evidência sem implementar correções quando o pedido for apenas revisão.
---

# Revisar engenharia analítica

## Objetivo

Determinar se a solução é correta, reproduzível, segura, operável e sustentável, tentando encontrar falhas antes que se tornem incidentes ou dados incorretos.

## Postura

- Revisar independentemente do autor.
- Pedir evidências em vez de presumir comportamento.
- Não alterar a implementação quando o escopo for somente revisão.
- Separar defeito observado, risco potencial e preferência estilística.
- Não aprovar por ausência de erro visível.

## Fluxo

1. Definir escopo, ambiente, consumidores, SLA e criticidade.
2. Ler arquitetura, contratos, código, testes, execução e evidências.
3. Reconstruir origem, transformação, destino e dependências.
4. Verificar correção funcional e semântica.
5. Avaliar qualidade, reprocessamento, observabilidade, segurança e custo.
6. Executar verificações não destrutivas quando autorizadas.
7. Classificar achados e indicar correção e reteste.
8. Emitir parecer e riscos residuais.

## Checklist

### Dados e semântica

Verificar granularidade, chaves, cardinalidade, duplicidades, perda de linhas, tipos, timezone, unidades, regras de negócio, joins, filtros, nulos, deduplicação, contratos, evolução de schema e lineage.

### Pipeline

Verificar idempotência, determinismo, cargas full e incremental, late-arriving data, watermark, merge, upsert, exclusões, backfill, replay, retry, rollback, dependências, concorrência, atomicidade e recuperação.

### Qualidade e testes

Verificar schema, chaves, volume, completude, regras, reconciliação origem-destino, casos limite, falhas, dados de teste e prevenção de regressão.

### Performance e custo

Verificar particionamento, clustering, índices, pruning, shuffle, skew, materialização, tamanho de arquivos, leituras repetidas, paralelismo, memória e crescimento esperado.

### Operação, segurança e governança

Verificar logs, métricas, alertas, ownership, SLA, freshness, runbook, segredos, menor privilégio, dados pessoais, retenção, ambientes, configuração, dependências e decisões.

## Tecnologias

Em SQL, revisar plano, cardinalidade, filtros, janelas e incrementalidade. Em Spark, revisar shuffle, skew, particionamento, ações, cache e arquivos. Em orquestração, revisar dependências, retries, timeout, concorrência e backfill. Em notebooks, revisar estado implícito, ordem de execução e separação entre exploração e pipeline.

Priorizar SQL para transformações relacionais e Python para validação e automação.

## Achados e parecer

Classificar como bloqueador, alto, médio, baixo ou observação. Informar identificador, evidência, cenário, impacto, correção, reteste e status.

Finalizar como aprovado, aprovado com ressalvas, revisão necessária ou não confiável. Declarar o que não pôde ser verificado.
