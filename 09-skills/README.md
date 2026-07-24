# 09 — Habilidades portáveis

Coleção canônica de habilidades da Cheila para projetos de dados, estatística, machine learning, engenharia analítica e decisão.

Cada habilidade vive em uma pasta com `SKILL.md` obrigatório e recursos opcionais. O formato é textual e pode ser usado por qualquer LLM capaz de receber instruções em Markdown.

## Uso rápido

1. Leia o `AGENTS.md` da raiz.
2. Consulte `manifest.yaml`.
3. Escolha o menor conjunto de habilidades necessário.
4. Leia integralmente o `SKILL.md` de cada habilidade escolhida.
5. Carregue referências somente quando forem necessárias.
6. Execute respeitando os gates, aprovações e regras do projeto.

## Domínios

### coordenação

- [gerenciar-projeto-ponta-a-ponta](gerenciar-projeto-ponta-a-ponta/SKILL.md)
- [orientar-analise-estatistica](orientar-analise-estatistica/SKILL.md)
- [formular-problema-analitico](formular-problema-analitico/SKILL.md)
- [documentar-projeto-analitico](documentar-projeto-analitico/SKILL.md)
- [desenhar-sistemas-e-fluxos](desenhar-sistemas-e-fluxos/SKILL.md)

### dados e engenharia

- [preparar-dados-analiticos](preparar-dados-analiticos/SKILL.md)
- [auditar-dados-estatisticos](auditar-dados-estatisticos/SKILL.md)
- [revisar-engenharia-analitica](revisar-engenharia-analitica/SKILL.md)

### estatística e inferência

- [executar-analise-exploratoria](executar-analise-exploratoria/SKILL.md)
- [formular-testes-de-hipotese](formular-testes-de-hipotese/SKILL.md)
- [modelar-regressao](modelar-regressao/SKILL.md)
- [analisar-dados-multivariados](analisar-dados-multivariados/SKILL.md)
- [realizar-inferencia-bayesiana](realizar-inferencia-bayesiana/SKILL.md)
- [planejar-experimentos](planejar-experimentos/SKILL.md)
- [analisar-causalidade](analisar-causalidade/SKILL.md)

### machine learning e séries temporais

- [modelar-aprendizado-supervisionado](modelar-aprendizado-supervisionado/SKILL.md)
- [modelar-aprendizado-nao-supervisionado](modelar-aprendizado-nao-supervisionado/SKILL.md)
- [selecionar-e-construir-atributos](selecionar-e-construir-atributos/SKILL.md)
- [analisar-series-temporais](analisar-series-temporais/SKILL.md)
- [validar-modelos-estatisticos](validar-modelos-estatisticos/SKILL.md)
- [explicar-modelos-e-resultados](explicar-modelos-e-resultados/SKILL.md)

### decisão e comunicação

- [simular-sistemas-e-cenarios](simular-sistemas-e-cenarios/SKILL.md)
- [otimizar-decisoes](otimizar-decisoes/SKILL.md)
- [traduzir-evidencias-para-negocio](traduzir-evidencias-para-negocio/SKILL.md)
- [revisar-estudo-analitico](revisar-estudo-analitico/SKILL.md)

## Compatibilidade

- `SKILL.md`: instrução independente de fornecedor.
- `references/`: conhecimento carregado sob demanda.
- `scripts/` e `assets/`: recursos reutilizáveis quando existentes.
- `agents/openai.yaml`: metadado opcional para OpenAI; pode ser ignorado por outros modelos.

Consulte [PORTABILITY.md](PORTABILITY.md) para integração com outros agentes.
