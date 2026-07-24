---
name: desenhar-sistemas-e-fluxos
description: Modelar e comunicar sistemas, arquiteturas, processos, fluxos de dados, jornadas analíticas e dependências por meio de diagramas e documentação estruturada. Usar para desenhar arquitetura atual ou futura, pipeline, DAG, processo de negócio, ciclo de vida de projeto, sequência entre agentes, integração entre fontes e consumidores, estados, decisões, responsabilidades ou controles; escolher entre fluxograma, sequência, estado, C4, arquitetura, ER, árvore, timeline ou tabela conforme a relação representada. Exigir escopo, atores, fronteiras, entradas, saídas, decisões, exceções e fonte de verdade; não inventar componentes nem usar diagramas quando uma lista simples for mais clara.
---

# Desenhar sistemas e fluxos

## Objetivo

Transformar uma descrição ambígua em uma representação verificável, pequena e útil para decisão, implementação ou alinhamento.

## Fluxo

1. Definir a pergunta que o desenho precisa responder.
2. Delimitar sistema, nível de detalhe, público e fronteiras.
3. Identificar entidades, atores, etapas, estados, dados, decisões e dependências.
4. Separar estado atual, estado proposto e hipótese.
5. Escolher a representação mínima adequada.
6. Produzir o desenho com legenda, premissas e pontos não verificados.
7. Validar direção, cardinalidade, sequência, ownership e exceções.
8. Revisar com a fonte de verdade antes de tratar o desenho como documentação.

## Escolher o formato

- Usar fluxograma para etapas, decisões e caminhos alternativos.
- Usar diagrama de sequência para interação ordenada entre atores ou serviços.
- Usar diagrama de estados para ciclos de vida e transições controladas.
- Usar C4 ou arquitetura para fronteiras, sistemas e dependências.
- Usar ER para entidades, chaves, cardinalidade e relacionamentos.
- Usar DAG para dependências acíclicas, pipelines e orquestração.
- Usar timeline para eventos e mudanças ao longo do tempo.
- Usar tabela para comparação ou mapeamento exato.

Não criar visualização se uma explicação curta for mais clara.

## Regras

- Dar nomes concretos aos nós e verbos às relações.
- Manter no máximo cinco nós na horizontal.
- Dividir desenhos densos por nível ou responsabilidade.
- Distinguir fluxo de dados, fluxo de controle e responsabilidade.
- Mostrar entradas, saídas, persistência, falhas e observabilidade quando aplicáveis.
- Não confundir ordem visual com ordem temporal.
- Não representar associação como causalidade.
- Marcar componentes propostos, externos ou não verificados.
- Manter identificadores consistentes entre desenho e documentação.

## Sistemas analíticos

Verificar origem, contrato e granularidade; ingestão, transformação, validação e armazenamento; disponibilidade temporal e leakage; treino, validação, registro, consumo e monitoramento; ownership; gates humanos; reprocessamento, rollback e falhas.

## Entrega

Entregar objetivo e escopo, diagrama ou tabela, legenda, premissas, elementos não verificados, riscos, lacunas, decisões abertas e descrição textual suficiente para acessibilidade.
