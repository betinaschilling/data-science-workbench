---
name: documentar-projeto-analitico
description: Criar e atualizar documentação técnica, metodológica e de negócio para análises, experimentos e modelos de ciência de dados. Usar para registrar objetivo, fontes, população, dicionário, transformações, hipóteses, decisões, código, validação, resultados, limitações, model cards, data cards, riscos e reprodução. Distinguir documentação executada de plano futuro, manter linhagem e conectar evidências às conclusões sem gerar arquivos auxiliares desnecessários.
---

# Documentar projeto analítico

## Princípio

Documentar para que outra pessoa consiga compreender, reproduzir, revisar e decidir. Derivar a documentação de artefatos reais; não inventar resultados, parâmetros ou validações.

## Definir escopo e público

Identificar fase do projeto, leitores, decisão e artefato necessário. Evitar um documento único excessivo quando públicos exigirem profundidades diferentes.

## Registrar contexto

Incluir:

- problema e decisão;
- perguntas e hipóteses;
- população, unidade, período e horizonte;
- escopo e exclusões;
- critérios de sucesso;
- responsáveis e decisões pendentes.

## Documentar dados

Registrar fontes, owners, chaves, granularidade, cobertura, atualização, dicionário, qualidade, filtros, joins, transformações, dados sensíveis e linhagem.

Distinguir dado bruto, intermediário e derivado. Não copiar segredos, credenciais ou amostras sensíveis.

## Documentar método

Explicar desenho, estimando ou target, particionamento, baseline, features, métodos, hiperparâmetros, pressupostos, diagnósticos, métricas e alternativas rejeitadas.

Registrar decisões com data lógica, justificativa, evidência, impacto e aprovação quando material.

## Documentar execução

Incluir ambiente, dependências essenciais, sementes, entradas, comandos ou ordem de notebooks, configurações e saídas. Separar:

- executado e verificado;
- planejado;
- bloqueado;
- descartado.

Não declarar reprodução sem testar quando o ambiente estiver disponível.

## Documentar resultados

Conectar tabela ou figura à pergunta. Reportar magnitude, incerteza, segmentos, estabilidade, erros e limitações. Manter resultados nulos ou contraditórios quando relevantes.

## Artefatos especializados

Quando aplicável, produzir:

- data card;
- model card;
- experiment report;
- decision log;
- risk register;
- ficha de métrica;
- guia de reprodução;
- relatório executivo;
- apêndice metodológico.

Criar apenas artefatos necessários ao uso real.

## Usar quatro camadas

Organizar, proporcionalmente:

1. fundamento acadêmico;
2. procedimento técnico;
3. interpretação de negócio;
4. código com objetivo, entradas, processamento, saída esperada e interpretação.

Evitar repetir o mesmo conteúdo entre camadas.

## Verificar qualidade

Conferir consistência entre documentação e código, nomes de colunas, métricas, versões, números e conclusões. Revisar links, caminhos e instruções. Identificar informação ausente em vez de completar por plausibilidade.

## Entregar

Fornecer documento navegável, conciso, rastreável e atualizado, com status, limitações e próximos passos. Se houver arquivo solicitado, usar o formato apropriado e verificar sua renderização.
