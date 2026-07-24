# Orientações para agentes

Este repositório é um workbench de aprendizagem e estudos analíticos, não um sistema único de produção.

## Agentes

- `lider_projeto_analitico`: coordena o ciclo, seleciona skills e controla gates.
- `revisor_cientifico_analitico`: realiza revisão independente e somente leitura.
- `mentor_ciencia_de_dados`: conduz aprendizagem, exercícios e projetos guiados.

## Fluxo padrão

1. Formular o problema e os critérios de sucesso.
2. Auditar fontes, população, granularidade e qualidade.
3. Preparar a base analítica sem vazamento.
4. Explorar e selecionar o método compatível com a pergunta.
5. Modelar, diagnosticar e validar.
6. Explicar resultados e traduzir evidências para decisão.
7. Documentar premissas, decisões, limitações e próximos passos.
8. Submeter conclusões relevantes a revisão independente.

## Regras

- Python é a linguagem analítica padrão; SQL é preferido para preparação.
- R só deve ser usado quando não houver solução viável e confiável em Python.
- Nunca alterar dados brutos.
- Nunca imputar, excluir observações ou remover outliers silenciosamente.
- Nunca embaralhar séries temporais.
- Associação, previsão e causalidade devem permanecer explicitamente separadas.
- Escolha do modelo final e decisões metodológicas materiais exigem revisão humana.
- Código não executado não pode ser descrito como validado.
