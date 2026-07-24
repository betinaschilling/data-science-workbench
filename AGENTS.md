# Instruções canônicas para agentes

Este arquivo governa qualquer agente que trabalhe neste repositório. Antes de criar, mover, revisar ou concluir um trabalho, leia este arquivo, o `README.md` da raiz e o `README.md` da área envolvida.

O repositório é um workbench de aprendizagem e estudos analíticos. Ele não representa um único sistema de produção.

## 1. Estrutura oficial

As pastas numeradas expressam ordem de navegação e responsabilidade:

| Ordem | Pasta | Responsabilidade |
|---|---|---|
| 00 | `00-catalog/` | Inventário e estado dos ativos |
| 01 | `01-projects/` | Ciclo de vida dos estudos |
| 02 | `02-learning/` | Trilhas e exercícios de aprendizagem |
| 03 | `03-engineering/` | Práticas de dados e engenharia analítica |
| 04 | `04-knowledge/` | Conhecimento permanente e reutilizável |
| 05 | `05-templates/` | Modelos para iniciar novos trabalhos |
| 06 | `06-packages/` | Código Python compartilhado e testado |
| 07 | `07-archive/` | Conteúdo histórico preservado |
| 08 | `08-docs/` | Metodologia, decisões, padrões e roadmap |

As pastas técnicas `.codex/` e `.github/` não recebem numeração e não devem ser renomeadas.

Não crie uma nova pasta de primeiro nível sem uma decisão registrada em `08-docs/02-decisions/`.

## 2. Agentes e responsabilidades

- `lider_projeto_analitico`: coordena o ciclo, verifica gates e propõe promoções.
- `revisor_cientifico_analitico`: revisa de forma independente e somente leitura; não promove nem corrige o próprio objeto revisado.
- `mentor_ciencia_de_dados`: orienta aprendizagem e pode propor projetos, mas não declara um estudo concluído sem os gates aplicáveis.
- Qualquer outro agente deve seguir este arquivo, mesmo que suas instruções locais sejam menos específicas.

Conflitos entre instruções devem ser resolvidos nesta ordem: pedido explícito da usuária, segurança e integridade dos dados, este `AGENTS.md`, documentação local, convenções gerais.

## 3. Ciclo obrigatório dos projetos

O único fluxo normal é:

`01-projects/01-incubating/` → `01-projects/02-active/` → `01-projects/03-completed/`

A numeração indica sequência, não prioridade.

Regras invariáveis:

1. Todo projeto novo começa em `01-incubating/`.
2. Não é permitido criar um projeto diretamente em `02-active/` ou `03-completed/`.
3. Não é permitido saltar etapas.
4. Promoção significa mover o mesmo diretório do projeto; não duplicar versões entre estados.
5. Toda promoção exige evidências, atualização do catálogo e registro da decisão.
6. Um agente pode recomendar uma promoção, mas escolhas metodológicas materiais e a conclusão final exigem aprovação humana.
7. Se um gate não estiver satisfeito, o projeto permanece no estado atual e a pendência deve ser registrada.
8. Retorno a um estado anterior é permitido quando uma revisão encontrar problema material; registre o motivo e o plano de correção.

## 4. Manifesto mínimo do projeto

Cada projeto deve conter `project.yaml` com, no mínimo:

```yaml
name: nome-do-projeto
title: Título legível
status: incubating
owner: Cheila
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
decision: decisão que o estudo pretende apoiar
question: pergunta analítica principal
population: população do estudo
unit_of_analysis: unidade de análise
time_scope: período e horizonte
data_sources: []
method_family: null
success_criteria: []
risks: []
human_approvals: []
review_status: pending
```

Valores válidos para `status`: `incubating`, `active` e `completed`. O valor deve coincidir com a pasta física.

Também devem existir, proporcionalmente ao projeto:

- `README.md`: objetivo, contexto, uso e estado atual;
- `data/`: referências ou instruções, sem versionar dados grandes ou sensíveis;
- `notebooks/`: exploração e narrativas executáveis;
- `src/`: código reutilizável do projeto;
- `tests/`: verificações relevantes;
- `reports/`: resultados e comunicação;
- `decisions/`: escolhas metodológicas e aprovações;
- `references/`: fontes acadêmicas ou técnicas.

Não crie diretórios vazios sem necessidade; use apenas os componentes aplicáveis.

## 5. Gate de entrada — Incubating

Um item pode existir em `01-incubating/` quando houver:

- título e motivação;
- problema ou oportunidade inicial;
- possível decisão ou aprendizado esperado;
- responsável;
- dúvidas e dependências conhecidas.

Neste estado, hipóteses, fontes e métodos podem estar incompletos. Não apresente resultados exploratórios como conclusões.

## 6. Promoção — Incubating para Active

Promova somente quando todos os itens aplicáveis estiverem atendidos:

- decisão e pergunta analítica formalizadas;
- população, unidade de análise, período e granularidade definidos;
- fontes identificadas e acesso confirmado, ou dados simulados explicitamente declarados;
- critérios de sucesso técnicos e de negócio definidos;
- método inicial compatível com a pergunta;
- plano por etapas, entregáveis e dependências;
- riscos de qualidade, viés, leakage, privacidade e causalidade registrados;
- responsável e próximo marco definidos;
- `project.yaml`, `README.md` e catálogo atualizados;
- aprovação humana registrada para escolhas materiais já realizadas.

Procedimento:

1. Verifique o checklist e registre pendências.
2. Atualize `project.yaml.status` para `active`.
3. Atualize `updated_at` e o próximo marco.
4. Mova o diretório para `01-projects/02-active/`.
5. Atualize a entrada em `00-catalog/`.
6. Registre a promoção em `decisions/` ou `08-docs/02-decisions/`.
7. Valide que não restou cópia em `01-incubating/`.

## 7. Gate de execução — Active

Enquanto estiver em `02-active/`, o agente deve:

- auditar os dados antes de inferência ou modelagem;
- preservar dados brutos;
- documentar joins, filtros, imputações, exclusões e outliers;
- impedir vazamento e respeitar disponibilidade temporal;
- separar descrição, inferência, previsão, causalidade, simulação e prescrição;
- estabelecer baseline e estratégia de validação;
- registrar experimentos, métricas, falhas e mudanças de escopo;
- manter código reproduzível e dependências declaradas;
- solicitar aprovação humana nos gates definidos;
- manter `project.yaml` e catálogo sincronizados.

Nunca descreva código não executado como validado nem ausência de evidência como evidência de ausência.

## 8. Promoção — Active para Completed

Promova somente quando todos os itens aplicáveis estiverem atendidos:

- pergunta respondida ou encerrada com justificativa;
- dados e transformações documentados;
- código relevante executado e verificações concluídas;
- modelo, análise ou experimento validado com método adequado;
- resultados reproduzíveis a partir das instruções;
- conclusões separadas em sustentadas, não sustentadas e não verificáveis;
- limitações, incertezas e riscos residuais documentados;
- interpretação técnica e implicação de negócio proporcionais à evidência;
- revisão independente concluída;
- achados bloqueadores e altos resolvidos ou formalmente aceitos pela usuária;
- decisão final e aprovação humana registradas;
- ativos reutilizáveis extraídos para `04-knowledge/`, `05-templates/` ou `06-packages/`, quando pertinente;
- catálogo e documentação atualizados.

Procedimento:

1. Execute o checklist final.
2. Atualize `project.yaml.status` para `completed`.
3. Registre data, parecer da revisão e decisão final.
4. Mova o diretório para `01-projects/03-completed/`.
5. Atualize `00-catalog/`.
6. Registre a promoção.
7. Valide que não restou cópia em `02-active/`.

`completed` significa encerrado e auditável, não necessariamente bem-sucedido. Estudos inconclusivos podem ser concluídos se a impossibilidade e suas causas estiverem documentadas.

## 9. Arquivo não é estado de projeto

`07-archive/` preserva conteúdo histórico migrado ou substituído. Não é a etapa seguinte de `completed`.

Para arquivar material:

- preserve autoria, contexto e origem;
- registre de qual repositório ou versão veio;
- indique limitações e se o conteúdo está obsoleto;
- não reescreva silenciosamente resultados históricos;
- confirme a migração antes de arquivar o repositório de origem;
- nunca apague histórico sem pedido explícito da usuária.

## 10. Aprendizagem, conhecimento, templates e pacotes

- `02-learning/` contém trilhas, exercícios e progresso de aprendizagem; não deve virar depósito de projetos.
- `03-engineering/` contém práticas e componentes de engenharia ainda ligados ao aprendizado ou demonstração.
- `04-knowledge/` recebe sínteses estáveis e independentes de um projeto específico.
- `05-templates/` recebe estruturas genéricas, sem dados ou resultados de um projeto real.
- `06-packages/` recebe código reutilizável com interface clara, documentação e testes proporcionais.

Extrair um ativo não significa remover sua referência do projeto de origem. Registre a ligação no catálogo.

## 11. Linguagem, método e aprovação humana

- Python é a linguagem analítica padrão.
- SQL é preferido para preparação e transformação relacional.
- R só deve ser usado quando não houver solução viável e confiável em Python, com justificativa.
- Nunca alterar dados brutos.
- Nunca imputar, excluir observações ou remover outliers silenciosamente.
- Nunca embaralhar séries temporais.
- Escolha do desenho causal, mudança de população ou target, aceitação de leakage ou viés material e seleção do modelo final exigem aprovação humana.

## 12. Checklist obrigatório antes de encerrar uma tarefa

Antes de declarar uma tarefa concluída, todo agente deve informar:

- pasta e estado afetados;
- arquivos criados, alterados ou movidos;
- verificações executadas e seus resultados;
- decisões e aprovações registradas;
- riscos, limitações e pendências;
- próxima promoção possível e gates ainda faltantes.

Se não houver evidência verificável, escreva `não verificado`; não presuma sucesso.
