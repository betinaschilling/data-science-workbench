---
name: gerenciar-projeto-ponta-a-ponta
description: Planejar, coordenar, governar e encerrar projetos de dados, analytics, estatística, machine learning e engenharia desde a ideia até a entrega auditável. Usar para criar roadmap, backlog, marcos, dependências, responsabilidades, riscos, critérios de aceite, gates, registros de decisão, status, promoções entre incubating, active e completed, handoffs entre agentes ou equipes e encerramento; integrar formulação, dados, engenharia, análise, validação, documentação e tradução para negócio sem substituir as skills especialistas. Exigir evidência para avanço, aprovação humana em decisões materiais e rastreabilidade entre objetivo, execução e resultado.
---

# Gerenciar projeto ponta a ponta

## Objetivo

Conduzir o projeto como um sistema de decisões e evidências, mantendo escopo, qualidade, responsabilidade e estado sincronizados.

## Inicialização

1. Ler as instruções do repositório e identificar a estrutura oficial.
2. Definir decisão, pergunta, valor esperado, responsável e partes interessadas.
3. Delimitar população, unidade, período, granularidade, dados e restrições.
4. Classificar o trabalho como descrição, inferência, previsão, causalidade, simulação, otimização ou engenharia.
5. Criar entregáveis, marcos, dependências, riscos e critérios de aceite.
6. Registrar o estado inicial e o próximo gate.

Usar `formular-problema-analitico` quando o problema ainda não estiver verificável e `desenhar-sistemas-e-fluxos` quando dependências ou responsabilidades precisarem ser visualizadas.

## Planejamento

Para cada etapa, registrar objetivo, saída verificável, responsável, revisor, entradas, dependências, skill necessária, critério de aceite, riscos, aprovação e status.

Não planejar por ferramentas. Planejar por decisões, evidências e entregáveis.

## Execução

1. Auditar dados e acessos antes de análise ou modelagem.
2. Preparar bases com rastreabilidade e sem leakage.
3. Acionar somente as especialidades necessárias.
4. Atualizar status, riscos, decisões e pendências após cada marco.
5. Comparar resultado com critério de aceite.
6. Bloquear avanço quando faltar evidência, aprovação ou dependência crítica.
7. Replanejar explicitamente mudanças de escopo, prazo, população, target ou método.

## Gates humanos

Exigir aprovação antes de imputar ou excluir observações; remover outliers; mudar população, granularidade, target, estimando ou horizonte; excluir grupos, períodos ou variáveis substantivas; aceitar leakage, viés ou limitação material; escolher desenho causal ou modelo final; promover ou encerrar projeto; transformar evidência em ação relevante.

Apresentar alternativas, evidências, consequências e recomendação.

## Promoções

Seguir a estrutura e os gates definidos no `AGENTS.md`. Nunca saltar estados, duplicar o projeto entre estados ou confundir arquivo histórico com conclusão.

Antes de promover, verificar critérios, atualizar manifesto e catálogo, registrar a decisão, mover o mesmo diretório e confirmar que não restou cópia no estado anterior.

## Encerramento

Exigir pergunta respondida ou impossibilidade justificada; validação e revisão independente; resultados reproduzíveis; conclusões, limitações e riscos; documentação; decisão e aprovação; ativos reutilizáveis extraídos; catálogo e estado atualizados.

Usar `documentar-projeto-analitico` e a revisão compatível com a natureza da entrega.

## Comunicação

Informar estado atual, concluído desde a última atualização, próximo marco, bloqueios, decisões pendentes, riscos, mudanças de escopo, evidências e gates faltantes.
